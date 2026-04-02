class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> smap;
        for(auto &s: strs){
            string sortedS = s;
            sort(sortedS.begin(), sortedS.end());
            smap[sortedS].push_back(s);
        }
        vector<vector<string>> ans;
        for(auto &pair: smap){
            ans.push_back(pair.second);
        }
        return ans;
    }
};
