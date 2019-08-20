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

    
    for (int i = 1; i < m; i+=2){
        int s = 0;
        for (int j = 0; j < n; j++){
            s += h[i][j];
        }
        cout<<"Ср. фарифметическое строки "<<i<<" : "<<s/n<<endl;
    }
    
    
}