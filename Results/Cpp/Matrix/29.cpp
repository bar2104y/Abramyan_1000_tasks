#include <iostream>

using namespace std;

int main(){
    int m,n;
    cout<<"(строки)  M: "; cin>>m;
    cout<<"(столбцы) N: "; cin>>n;
    
    int h[m][n];
    //h[строка][столбец]
    //М строк на M столбцов
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            h[i][j] = i*j;

    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++)
            cout<<h[i][j]<<"\t";
    cout<<endl;
    }
    int i,j;
    for ( i = 0; i<m; i++){
        float sr = 0;
        int s = 0;
        for (j = 0; j < n; j++)
            s += h[i][j];
        sr = s/n;
        int k = 0;
        for (j = 0; j < n; j++)
            if ( h[i][j] < sr )
                k += 1;
        cout<<"В строке "<< i<<" подходит "<<k<<" чсисел"<<endl;

    }

}