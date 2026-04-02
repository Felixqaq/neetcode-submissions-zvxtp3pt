class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> alset;
        int l = 0, r = 0;
        int res = 0;
        
        while (r < s.size()) {
            if (alset.find(s[r]) == alset.end()) {
                alset.insert(s[r]);
                res = max(res, r - l + 1);
                r++;
            } else {
                alset.erase(s[l]);
                l++;
            }
        }
        return res;
    }
};
