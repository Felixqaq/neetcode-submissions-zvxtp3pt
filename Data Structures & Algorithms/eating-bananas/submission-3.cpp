class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int maxN = 0;
        
        for(int p: piles){
            maxN = max(maxN, p);
        }
        int l = 1, r = maxN; 
        int minNeedHour = maxN;
        while(l <= r){
            int mid = (r+l) / 2;
            int totalNeed = 0;
            for(int i=0; i<piles.size(); i++){
                double needHour = piles[i];
                int need = ceil(needHour/mid);
                totalNeed += need;
            }

            if(totalNeed <= h){
                minNeedHour = min(minNeedHour, mid);
                r = mid - 1;
            }else{
                l = mid + 1;
            }

        }
        return minNeedHour;
    }
};
