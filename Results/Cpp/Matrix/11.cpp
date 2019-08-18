#include <iostream>

using namespace std;

int main(){
    int m,n;
    cout<<"(строки)    M: "; cin>>m;
    cout<<"(столбцы)   N: "; cin>>n;
    
    int h[m][n];
    //h[строка][столбец]
    //М строк на N столбцов
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            h[i][j] = i*j;

    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++)
            cout<<h[i][j]<<"\t";
    cout<<endl;
    }
    cout<<endl;

    for (int i = 0; i<m; i++){
        if ( i%2 == 0)
        {
            for ( int j = 0; j < n; j++)
                cout<<h[i][j]<<"\t";
            cout<<endl;
        } else
        {
            for ( int j = n-1; j >= 0; j--)
                cout<<h[i][j]<<"\t";
            cout<<endl;
        }
        

        
    }
        

}