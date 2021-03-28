#include<iostream>
#include<vector>

using namespace std;
enum State{
    horizontal,
    vertical,
    diagonal
};
enum Direction{
    dRight,
    dDown,
    dRD
};
int cnt = 0;
int n;
vector<vector<int> > v;

void move(int r, int c, int direction, int mState){
    if(direction == dRD){
        r++;
        c++;
        if(r > n-1 || c > n-1)return;
        if(v[r][c] == 1 || v[r-1][c] == 1 || v[r][c-1] == 1) return;
        mState = diagonal;
    }
    else if(direction == dRight){
        c++;
        if(r > n-1 || c > n-1)return;
        if(mState == vertical || v[r][c] == 1) return;
        mState = horizontal;
    }
    else if(direction == dDown){
        r++;
        if(r > n-1 || c > n-1)return;
        if(mState == horizontal || v[r][c] == 1)return;
        mState = vertical;
    }

    if(r == n-1 && c == n-1) {
        cnt++;
        return ;
    }
    move(r, c, dRight, mState);
    move(r, c, dDown, mState);
    move(r, c, dRD, mState);
    return ;
    
}

int main(){
    cin >> n;
    v.assign(n, vector<int>(n));
    for (auto &list : v){
        for(auto &i : list){
            cin >> i;
        }
    }
    move(0, 1, dRight, horizontal);
    move(0, 1, dRD, horizontal);
    cout << cnt << endl;

    return 0;
}