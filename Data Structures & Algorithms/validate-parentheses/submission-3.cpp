class Solution {
public:
    bool isValid(string s) {
        stack<char> q;
        for(char c: s){
            if(c == '[' || c == '{' || c == '('){
                q.push(c);
            }

            if(c == ']'){
                if(q.empty())return false;
                if(q.top() != '[')return false;
                q.pop();
            }
            if(c == '}'){
                if(q.empty())return false;
                if(q.top() != '{')return false;
                q.pop();
            }
            if(c == ')'){
                if(q.empty())return false;
                if(q.top() != '(')return false;
                q.pop();
            }
        }

        if(!q.empty())return false;
        return true;
    }
};
