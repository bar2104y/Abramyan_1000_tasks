#include <iostream>

using namespace std;

int main(){
    int m,n,k;
    cout<<"(строки)   M: "; cin>>m;
    cout<<"(столбцы)  N: "; cin>>n;
    cout<<"(строка №) K: "; cin>>k;
    
    int h[m][n];
    //h[строка][столбец]
    //М строк на N столбцов
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            h[i][j] = i*j;

    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++)
            cout<<h[i][j]<<"\t";
    cout<<endl;
    }

    for (int j = 0; j<n; j++)
        cout<<h[k][j]<<"\t";
    cout<<endl;

}