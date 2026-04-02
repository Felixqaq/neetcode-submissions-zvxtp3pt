class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l=0, r=heights.size()-1;
        int ans = 0;
        while(l<r){
            int height = min(heights[l], heights[r]);
            int tank = height*(r-l);
            ans = max(ans, tank);
            if(heights[l]> heights[r]){
                r--;
            }else{
                l++;
            }
        }
        return ans;
    }
};
