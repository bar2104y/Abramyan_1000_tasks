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
    for ( j = 0; j < n; j++){
        float sr = 0;
        int s = 0;
        for (i = 0; i < m; i++)
            s += h[i][j];
        sr = s/m;
        cout<<sr;
        int k = 0;
        for (i = 0; i < m; i++)
            if ( h[i][j] > sr )
                k += 1;
        cout<<"В столбце "<< j<<" подходит "<<k<<" чсисел"<<endl;

    }

}