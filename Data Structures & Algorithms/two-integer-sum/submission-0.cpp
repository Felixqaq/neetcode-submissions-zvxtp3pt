class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> gap;
        for(int i=0; i<nums.size(); i++){
            int com = target - nums[i];
            if(gap.count(com) && gap[com]!=i){
                return {gap[com], i};
            }
            gap[nums[i]] = i;
        }
        return {};
    }
};
