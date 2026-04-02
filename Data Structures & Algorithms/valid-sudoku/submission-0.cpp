class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

        for(int i=0; i<board.size(); i++){
            unordered_set<int> rowCount, colCount;
            for(int j=0; j<board.size(); j++){
                bool rowS=true, colS=true;
                if(board[i][j] != '.'){
                    int val = board[i][j];
                    auto rowResult = rowCount.insert(val);
                    rowS = rowResult.second;
                }
                if(board[j][i] != '.'){
                    int val = board[j][i];
                    auto colResult = colCount.insert(val);
                    colS = colResult.second;
                }
                if(!colS || !rowS)
                    return false;
            }
        }

        for(int i=0; i<9; i+=3){
            for(int j=0; j<9; j+=3){
                unordered_set<int> count;
                for(int k=i; k<i+3; k++){
                    for(int l=j; l<j+3; l++){
                        if(board[k][l]!='.'){
                            int val = board[k][l];
                            auto res = count.insert(val);
                            if(!res.second)return false;
                        }
                    }
                }
            }
        }

        return true;
    }

};
