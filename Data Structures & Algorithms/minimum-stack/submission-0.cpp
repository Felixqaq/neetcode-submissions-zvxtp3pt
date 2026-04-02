class MinStack {
private:
    stack<int> s, min_s;

public:
    MinStack() {
    }
    
    void push(int val) {
        s.push(val);
        if(min_s.empty()){
            min_s.push(val);
        }else{
            min_s.push(min(min_s.top(), val));
        }
    }
    
    void pop() {
        s.pop();
        min_s.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return min_s.top();
    }
};
