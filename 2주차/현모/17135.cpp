#include<iostream>
#include<vector>
#include<utility>
#include<cmath>

using namespace std;

void sort_ascending(vector<int> &v, int index){
    for(int i = 0; i < v.size() - index-1; i++){
        v[index+i+1] = v[index+i] + 1;
    }
}

int getDistance(int r1, int c1, int r2, int c2){
    return abs(r1-r2)+abs(c1-c2);
}


int getEnemy(vector<int> archer, int d, vector<vector<pair<int, int> > > v){
    int total(0);
    int index(v.size());
    int a, b;
    bool turnOver(false);
    while (index > 0)
    {
        for(auto c : archer){
            for(int i = 0; i < d; i++){
                for(int j = -i; j <= i; j++){
                    a = index-i+abs(j)-1;
                    b = c+j;
                    if(a < 0) continue;
                    if(b < 0) continue;
                    if(v[a][b].first == 1 && getDistance(a, b, index, c) <= d){
                        if(v[a][b].second == index){
                            turnOver = true;
                            break;
                        }
                        else if(v[a][b].second != -1) continue;
                        v[a][b].second = index;
                        total++;
                        turnOver = true;
                        break;
                    }
                }
                if(turnOver){
                    turnOver = false;
                    break;
                }
            }
        }
        index--;
    }
    return total;
}


int main(){
    int n, m, d;
    int index(2), temp(0), max(0);
    cin >> n >> m >> d;
    vector<vector<pair<int, int> > > mat(n, vector<pair<int, int> >(m, make_pair(0, -1)));
    vector<int> archer(3, 0);
    sort_ascending(archer, 0);
    
    for(auto &list : mat){
        for(auto &i : list){
            cin >> i.first;
        }
    }
    
    while (index >= -1)
    {
        for(int i = 2; i > index;){
            for(int j = archer[i]; j < i+m-2; j++){
                if(i < 2 && j >= archer[i+1]){
                    i++;
                    continue;
                };
                archer[i] = j;
                temp = getEnemy(archer, d, mat);
                if(max < temp) max = temp;
            }
            i--;
            if(i >= 0){
                archer[i]++;
                sort_ascending(archer, i);
            }
        }
        index--;
    }
    
    
    cout << max << endl;
    return 0;
}