class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        vector<pair<int, int>> pair;
        int maxArea = 0;

        for(int i=0; i<heights.size(); i++){
            int start = i;
            while(!pair.empty() && heights[i] < pair.back().first){
                start = pair.back().second;
                int mul = i - pair.back().second;
                int area = pair.back().first * mul;
                maxArea = max(maxArea, area);
                pair.pop_back();
            }
            pair.push_back({heights[i], start});
        }

        int maxI = heights.size();
        for(auto p: pair){
            int area = p.first * (maxI - p.second);
            maxArea = max(maxArea, area);
        }
        return maxArea;
    }
};
