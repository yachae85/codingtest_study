#include <iostream>
#include <vector>

using namespace std;

void sort_ascending(vector<int> &v, int index){
    for(int i = 0; i < v.size() - index-1; i++){
        v[index+i+1] = v[index+i] + 1;
    }
}

void printv(vector<int> v){
    for(auto n : v){
        printf("%d ", n);
    }
    printf("\n");
}

int main(){
    int n, k, index;
    cin >> n >> k;
    index = k-1;
    vector<int> v(k, 1);
    sort_ascending(v, 0);
    while (index >= -1)
    {
        for(int i = k-1; i > index;){
            for(int j = v[i]; j <= i+n-k+1; j++){
                if(i < k-1 && j >= v[i+1]){
                    i++;
                    continue;
                };
                v[i] = j;
                printv(v);
            }
            i--;
            if(i >= 0){
                v[i]++;
                sort_ascending(v, i);
            }
        }
        index--;
    }
    return 0;
}