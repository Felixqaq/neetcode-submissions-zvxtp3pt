class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int size = nums.size()-1;
        vector<vector<int>> ans;

        for(int i=0; i<size; i++){
            if(nums[i]>0)break;
            if(i > 0 && nums[i] == nums[i-1])continue;

            int l = i+1, r = size;
            while(l<r){
                int sum = nums[i] + nums[l] + nums[r];
                if(sum == 0){
                    ans.push_back({nums[i], nums[l], nums[r]});
                    r--;
                    l++;
                    while(nums[l] == nums[l-1] && l<r)l++;
                }else if(sum > 0){
                    r--;
                }else{
                    l++;
                }
            }
            
        }
        return ans;
    }

};
