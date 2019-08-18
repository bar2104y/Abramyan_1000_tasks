#include <iostream>

using namespace std;

int main(){
    int m,n,d;
    cout<<"M: "; cin>>m;
    cout<<"N: "; cin>>n;
    cout<<"D: "; cin>>d;
    cout<<"M чисел: ";
    
    int h[m][n];
    //h[строка][столбец]
    //М строк на N столбцов

    for (int i= 0; i < m; i++){
        cin>>h[i][0];
    }
    
    for (int j = 1; j<n; j++)
        for (int i=0; i<m; i++)
            h[i][j] = h[i][j-1] +d;
    

    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++)
            cout<<h[i][j]<<"\t";
    cout<<endl;
    }

}