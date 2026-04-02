class Solution {
public:
    int trap(vector<int>& height) {
        int total=0;
        int l=0, r=height.size()-1;
        int maxL = height[l], maxR = height[r];
        int temp;
        while(l<r){
            if(maxL>maxR){
                r--;
                temp = maxR - height[r];
                if(temp>0){
                    total+=temp;
                }else{
                    maxR = height[r];
                }
            }else{
                l++;
                temp = maxL - height[l];
                if(temp>0){
                    total+=temp;
                }else{
                    maxL = height[l];
                }
            }
        }
        return total;
    }
};
