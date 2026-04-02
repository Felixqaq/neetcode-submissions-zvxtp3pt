class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int res = 0;
        unordered_set<int> store(nums.begin(), nums.end());

        int ans = 0;

        for(int num: nums){
            int length = 0, cur = num;
            while(store.find(cur)!= store.end()){
                length++;
                cur++;
            }
            ans = max(ans, length);
        }
        return ans;
    }
};
