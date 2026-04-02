class Solution {
public:
    void backTrack(int openN, int closeN, int n, vector<string>& res, string& stack){
        if(openN == closeN && openN == n){
            res.push_back(stack);
            return;
        }

        if(openN < n){
            stack += '(';
            backTrack(openN+1, closeN, n, res, stack);
            stack.pop_back();
        }
        if(closeN < openN){
            stack += ')';
            backTrack(openN, closeN+1, n, res, stack);
            stack.pop_back();
        }
    }

    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string stack;
        backTrack(0, 0, n, res, stack);
        return res;
    }
};
