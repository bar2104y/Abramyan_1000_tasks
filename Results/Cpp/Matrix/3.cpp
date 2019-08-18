#include <iostream>

using namespace std;

int main(){
    int m,n;
    cout<<"M: "; cin>>m;
    cout<<"N: "; cin>>n;
    
    int h[n][m];
    int M[n];

    for (int i = 0; i < n; i++ ){
        cin>>M[i];
    }

    for (int i = 0; i < n; i++){
        for (int j= 0; j < m; j++){
            h[i][j] = M[i];
        }
    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++)
            cout<<h[i][j]<<"\t";
    cout<<endl;
    }

}