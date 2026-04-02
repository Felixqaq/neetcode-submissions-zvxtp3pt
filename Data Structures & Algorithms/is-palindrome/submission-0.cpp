class Solution {
public:
    bool isPalindrome(string s) {
        string fliterString = "";
        for(auto c: s){
            c = tolower(c);
            if(isalnum(c))fliterString+=c;
        }
        cout<<fliterString;
        int l = 0, r = fliterString.size()-1;
        while(l<r){
            if(fliterString[l]!=fliterString[r])
                return false;
            l++;
            r--;
        }
        return true;
    }
};
