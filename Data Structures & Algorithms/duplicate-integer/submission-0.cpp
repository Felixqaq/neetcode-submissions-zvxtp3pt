class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> total;
        for(int i=0; i<nums.size(); i++){
            if(total.count(nums[i]))
                return true;
            total.insert(nums[i]);
        }
        return false;
    }
};
