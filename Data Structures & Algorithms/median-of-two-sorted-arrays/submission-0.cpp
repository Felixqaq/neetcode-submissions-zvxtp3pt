class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> sum;
        int i=0, j=0;
        while(i < nums1.size() && j < nums2.size()){
            if(nums1[i] > nums2[j]){
                sum.push_back(nums2[j]);
                j++;
            }else{
                sum.push_back(nums1[i]);
                i++;
            }
        }

        while(i < nums1.size()){
            sum.push_back(nums1[i]);
            i++;
        }

        while(j < nums2.size()){
            sum.push_back(nums2[j]);
            j++;
        }

        double res;
        int len = sum.size();

        if(len % 2 == 0){
            res = ((double)sum[len / 2] + (double)sum[len / 2 - 1]) / 2;
        }else{
            res = sum[len / 2];
        }

        return res;
    }
};
