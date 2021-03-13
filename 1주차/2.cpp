#include<iostream>
#include<string>

using namespace std;

int main(){
    string s;
    string str = "";
    cin >> s;
    int index(-1);
    for(int i = 0; i < s.size(); i++){
        index = str.find(s[i]);
        if(index == string::npos){
            if(s[i] < str.back()){
                for(int j = str.size()-1; j >= 0; j--){
                    if(s.substr(i).find(str[j]) != string::npos && s[i] < str[j]){
                        str.erase(str.begin()+j);
                    }
                    else break;
                }
            }
            
            str += s[i];
        }
        
    }
    

    cout << str << endl;

    return 0;
}