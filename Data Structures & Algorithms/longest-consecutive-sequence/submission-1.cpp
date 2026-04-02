class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> store(nums.begin(), nums.end());
        int max_n = 0;
        for(int num: nums){
            int cur = num, count = 0;
            while(store.find(cur) != store.end()){
                cur++;
                count++;
            }
            max_n = max(count, max_n);
        }
        return max_n;
    }
};
