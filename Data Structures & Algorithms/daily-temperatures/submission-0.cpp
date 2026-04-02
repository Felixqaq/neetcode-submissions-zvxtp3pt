class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size(), 0);
        stack<pair<int, int>> stack;
        for(int i=0; i<temperatures.size(); i++){
            int t = temperatures[i];
            while(!stack.empty() && stack.top().first<t){
                int tempI = stack.top().second;
                stack.pop();
                res[tempI] = i-tempI;
            }
            stack.push(pair<int, int>{t, i});
        }
        return res;
    }
};
