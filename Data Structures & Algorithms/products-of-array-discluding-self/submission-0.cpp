class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        if(count(nums.begin(), nums.end(), 0) >= 2){
            return vector<int>(nums.size(), 0);
        }
        int total = 1;
        for(int n:nums){
            if(n != 0)
                total*=n;
        }

        vector<int> ans;
        if(count(nums.begin(), nums.end(), 0) == 1){
            for(int i=0; i<nums.size(); i++){
                if(nums[i] == 0)
                    ans.push_back(total);
                else
                    ans.push_back(0);
            }
        }else{
            for(int i=0; i<nums.size(); i++){
                ans.push_back(total/nums[i]);
            }
        }
        return ans;
    }
};
