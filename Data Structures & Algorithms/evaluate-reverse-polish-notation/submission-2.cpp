class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stack;

        for(string c: tokens){
            if(c == "+"){
                int y = stack.top();
                stack.pop();
                int x = stack.top();
                stack.pop();
                stack.push(x+y);
            }else if(c == "-"){
                int y = stack.top();
                stack.pop();
                int x = stack.top();
                stack.pop();
                stack.push(x-y);
            }else if(c == "*"){
                int y = stack.top();
                stack.pop();
                int x = stack.top();
                stack.pop();
                stack.push(x*y);
            }else if(c == "/"){
                int y = stack.top();
                stack.pop();
                int x = stack.top();
                stack.pop();
                stack.push(x/y);
            }else{
                stack.push(stoi(c));
            }
        }
        return stack.top();
    }
};
