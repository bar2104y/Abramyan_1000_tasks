#include <iostream>

using namespace std;

int main(){
    int m;
    cout<<"(строки)    M: "; cin>>m;
    
    int h[m][m];
    //h[строка][столбец]
    //М строк на M столбцов
    for (int i = 0; i < m; i++)
        for (int j = 0; j < m; j++)
            h[i][j] = i*j;

    for (int i = 0; i < m; i++){
        for (int j = 0; j < m; j++)
            cout<<h[i][j]<<"\t";
    cout<<endl;
    }
    cout<<endl;

    for (int j = 0; j < m; j++){
        int i;
        for ( i = 0; i<m-j; i++)
            cout<<h[i][j]<<"\t";
        i -= 1;
        for (int k = j+1; k<m; k++)
            cout<<h[i][k]<<"\t";
        cout<<endl;
        
    }
}