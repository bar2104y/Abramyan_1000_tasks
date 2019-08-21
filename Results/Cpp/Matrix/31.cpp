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
    float sr = 0;
    int s = 0;
    for ( j = 0; j < n; j++)
        for (i = 0; i < m; i++)
            s += h[i][j];
    
    sr = s/(m*n);
    float r = abs( h[0][0] - sr );
    int mm = 0; int nn = 0;
    for ( j = 0; j < n; j++)
        for (i = 0; i < m; i++)
            if ( abs( h[i][j] - sr ) < r){
                r = abs( h[i][j] - sr );
                mm = i;
                nn = j;
            }

    cout<<"M: "<<mm<<" N: "<<nn<<"; "<<h[mm][nn]<<endl;


}