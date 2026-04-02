class TimeMap {
public:
    unordered_map<string, vector<pair<string, int>>> map;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        map[key].push_back({value, timestamp});
    }
    
    string get(string key, int timestamp) {
        vector<pair<string, int>> vec = map[key];
        for(int i = vec.size()-1; i>=0; i--){
            pair<string, int> p = vec[i];
            if(p.second <= timestamp){
                return p.first;
            }
        }
        return "";
    }
};
