#include <iostream>

using namespace std;

int main(){
    int m,n,d;
    cout<<"M: "; cin>>m;
    cout<<"N: "; cin>>n;
    cout<<"D: "; cin>>d;
    cout<<n<<" чисел: ";
    
    int h[m][n];
    //h[строка][столбец]
    //М строк на N столбцов

    for (int i= 0; i < n; i++)
        cin>>h[0][i];
    
    for (int i = 1; i < m; i++)
        for (int j = 0; j < n; j++)
            h[i][j] = h[i-1][j] + d;

    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++)
            cout<<h[i][j]<<"\t";
    cout<<endl;
    }

}