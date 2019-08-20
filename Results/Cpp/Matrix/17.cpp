#include <iostream>
using namespace std;

int main(){
    int m,n,k;
    cout<<"(строки)  M: "; cin>>m;
    cout<<"(столбцы) N: "; cin>>n;
    cout<<"          K: "; cin>>k;
    
    int h[m][n];
    //h[строка][столбец]
    //М строк на M столбцов
    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            h[i][j] = i*j;
            cout<<h[i][j]<<"\t";
        }
        cout<<endl;
    }

    int s = 0; int mult = 1;
    for (int j = 0; j < n; j++){
        s += h[k][j];
        mult *= h[k][j];
    }
    
    cout<<"Сумма строки "<<k<<" : "<<s<<endl;
    cout<<"Произведение строки "<<k<<" : "<<mult<<endl;
}