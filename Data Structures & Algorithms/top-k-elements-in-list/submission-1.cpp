class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> countMap;
        for(int i=0; i<nums.size(); i++){
            countMap[nums[i]]++;
        }

        vector<vector<int>> bucket(nums.size()+1);

        for(const auto &pair: countMap){
            bucket[pair.second].push_back(pair.first);
        }

        vector<int> ans;
        for(int i=bucket.size()-1; i>0; i--){
            for(int i:bucket[i]){
                ans.push_back(i);

                if(ans.size()==k)
                    return ans;
            }
        }
        return ans;
    }
};
