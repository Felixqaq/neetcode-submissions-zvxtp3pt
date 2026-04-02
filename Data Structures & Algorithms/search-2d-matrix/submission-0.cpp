class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = matrix.size(), col = matrix[0].size();
        int total = col * row;
        int l = 0, r = total-1;
        while(l <= r){
            int mid = (r-l)/2 + l;
            int i = mid / col;
            int j = mid % col;
            if(matrix[i][j] == target)return true;
            if(matrix[i][j] < target){
                l = mid + 1;
            }else{
                r = mid - 1;
            }
        }
        return false;
    }
};
