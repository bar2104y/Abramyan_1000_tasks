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

    for ( int j = 0; j < n; j++){
        //int s = 0;
        long int mult = 1;
        for (int i = 0; i < m; i++){
            //s += h[i][j];
            mult *= h[i][j];
        }
        
        //cout<<"Сумма столбца "<<j<<" : "<<s<<endl;
        cout<<"Произведение столбца "<<j<<" : "<<mult<<endl;
    }
}