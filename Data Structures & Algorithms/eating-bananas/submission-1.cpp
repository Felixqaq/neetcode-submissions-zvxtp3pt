class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int maxN = 0;
        for(int p: piles){
            maxN = max(maxN, p);
        }
        int l = 1, r = maxN;
        int res=maxN;
        while(l <= r){
            int mid = (r+l) / 2;
            int total = 0;
            for(int p: piles){
                double dp = p;
                int n = ceil(dp/mid);
                total += n;
            }
            if(total <= h){
                res = mid;
                r = mid - 1;
            }else{
                l = mid + 1;
            }

        }
        return res;
    }
};