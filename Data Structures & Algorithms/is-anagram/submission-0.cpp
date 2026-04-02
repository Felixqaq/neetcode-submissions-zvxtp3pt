class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> charMap;
        for(int i=0; i<s.size(); i++){
            charMap[s[i]]++;
        }

        for(int i=0; i<t.size(); i++){
            charMap[t[i]]--;
        }

        for(const auto& pair : charMap){
            if(pair.second!=0)
                return false;
        }
        return true;

    }
};
