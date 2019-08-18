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

    for (int j = 0; j<n; j++){
        if ( j%2 == 1)
        {
            for ( int i = 0; i < m; i++)
                cout<<h[i][j]<<"\t";
            cout<<endl;
        } else
        {
            for ( int i = m-1; i >= 0; i--)
                cout<<h[i][j]<<"\t";
            cout<<endl;
        }
        

        
    }
        

}