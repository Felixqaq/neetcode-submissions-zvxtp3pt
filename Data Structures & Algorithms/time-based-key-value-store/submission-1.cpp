class TimeMap {
public:
    unordered_map<string, vector<pair<string, int>>> map;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        map[key].push_back({value, timestamp});
    }
    
    string get(string key, int timestamp) {
        string res = "";
        vector<pair<string, int>> vec = map[key];
        int l = 0, r = vec.size()-1;
        while(l <= r){
            int mid = (r + l)/2;
            if(vec[mid].second <= timestamp){
                res = vec[mid].first;
                l = mid + 1;
            }else{
                r = mid - 1;
            }
        }
        
        return res;
    }
};
