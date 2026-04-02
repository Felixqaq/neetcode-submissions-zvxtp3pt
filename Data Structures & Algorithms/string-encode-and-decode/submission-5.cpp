class Solution {
public:

    string encode(vector<string>& strs) {
        if(strs.empty())return "";
        string ans_str, size_str;

        for(string &s: strs){
            size_str += to_string(s.size()) + ',';
            ans_str += s;
        }
        return size_str + '#' + ans_str;
    }

    vector<string> decode(string s) {
        if (s.empty()) return {};
        vector<string> ans;
        vector<int> ssize;
        int i = 0;
        while(s[i]!='#'){
            string temp = "";
            while(s[i]!=','){
                temp+=s[i];
                i++;
            }
            ssize.push_back(stoi(temp));
            i++;
        }
        i++;
        for(int sz: ssize){
            ans.push_back(s.substr(i, sz));
            i+=sz;
        }
        return ans;
    }
};
