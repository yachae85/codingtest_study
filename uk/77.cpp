class Solution {
public:
    int N;
    int K;
    vector<int> ar;
    vector<vector<int>> arr;
    int used[21];
    
    void func(int c) {
        if(c == K) {
            arr.push_back(ar);
            return;
        }
        for(int i = 1; i <= N; i++) {
            if(used[i] == 0) {
                if(!ar.empty()) {
                    if(ar.back() < i) {
                        used[i] = 1;
                        ar.push_back(i);
                        func(c + 1);
                        ar.pop_back();
                        used[i] = 0;
                    }
                } else {
                    used[i] = 1;
                    ar.push_back(i);
                    func(c + 1);
                    ar.pop_back();
                    used[i] = 0;
                }
            }
        }
    }
    
    vector<vector<int>> combine(int n, int k) {
        N = n;
        K = k;
        func(0);
        return arr; 
    }
};