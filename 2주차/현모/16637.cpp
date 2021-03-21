#include<iostream>
#include<string>
#include <limits.h>


using namespace std;

struct Tree
{
    char op;
    int value;
   Tree* left;
   Tree* right;
};

typedef Tree* Treeptr;
string str;
int maxNum = INT_MIN;

int calc(string str){
    
    if(str.size() == 2) return static_cast<int>(str[1]) - '0';
    else if(str[2] == '+') return (static_cast<int>(str[1]) - '0') + (static_cast<int>(str[3]) - '0');
    else if(str[2] == '-') return (static_cast<int>(str[1]) - '0') - (static_cast<int>(str[3]) - '0');
    else if(str[2] == '*') return (static_cast<int>(str[1]) - '0') * (static_cast<int>(str[3]) - '0');
    return -1;   
}
int calc2(int n1, char op, int n2){
    if(op == '+') return n1 + n2;
    else if(op == '-') return n1 - n2;
    else if(op == '*') return n1 * n2;
    return -1;
}


Treeptr make_tree(int index, string data){
    if(index >= str.size()) return nullptr;
    Treeptr node = new Tree;
    string temp1, temp2;
    node->op = data[0];
    node->value = calc(data);
    node->right = nullptr;
    node->left = nullptr;

    
    node->right = new Tree;
    temp1 = str.substr(index+1, 4);
    node->right = make_tree(index+4, temp1);
    temp1.clear();
    
    node->left = new Tree;
    temp2 = str.substr(index+1, 2);
    node->left = make_tree(index+2, temp2);
    temp2.clear();
    
    return node;
}

void search(Treeptr node, int value){
    if(node){
        int v = calc2(value, node->op, node->value);
        search(node->left, v);
        if(!node->left){
            if(maxNum < v) maxNum = v;
        }
        search(node->right, v);
    }
}


int main(){
    int n;
    cin >> n;
    cin >> str;
    str = str;
    Treeptr root = make_tree(0, "+"+str.substr(0, 1));
    search(root, 0);

    cout << maxNum << endl;
    return 0;
}