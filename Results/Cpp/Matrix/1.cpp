#include <iostream>

using namespace std;

int main(){
    int m,n;
    cout<<"M: "; cin>>m;
    cout<<"N: "; cin>>n;

    int h[n][m];

    for (int i = 0; i < m; i++){
        for (int j= 0; j < n; j++){
            h[i][j] = 10*i;
        }
    }

    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++)
            cout<<h[i][j]<<"\t";
    cout<<endl;
    }

}