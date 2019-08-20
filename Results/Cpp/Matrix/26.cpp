#include <iostream>
using namespace std;

int main(){
    int m,n;
    cout<<"(строки)  M: "; cin>>m;
    cout<<"(столбцы) N: "; cin>>n;
    
    int h[m][n];
    //h[строка][столбец]
    //М строк на M столбцов
    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            h[i][j] = i*j+1;
            cout<<h[i][j]<<"\t";
        }
        cout<<endl;
    }

    long int minm = 1000001;
    int jj = 0;
    for ( int j = 0; j < n; j++){
        long int mult = 1;
        for (int i = 0; i < m; i++){
            mult *= h[i][j];
        }
        if ( mult < minm ){
            minm = mult;
            jj = j;
        }
    }
    
    cout<<"Произведение столбца "<<jj<<" : "<<minm<<endl;
}