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
            h[i][j] = (i+1)*(j+1);
            cout<<h[i][j]<<"\t";
        }
        cout<<endl;
    }

    int maxs = 0;
    int ii;
    for (int i = 0; i < m; i++){
        int s = 0;
        for (int j = 0; j < n; j++){
            s += h[i][j];
        }

        if (s > maxs){
            maxs = s;
            ii = i;
        }
    }

    cout<<"Сумма строки "<<ii<<" : "<<maxs<<endl;
    
    
}