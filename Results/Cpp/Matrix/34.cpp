#include <string>
#include <iostream> 
#include <ctime>

using namespace std;

int main()
{
    srand(time(NULL));

    int m,n;
    cout<<"(строки)  M: "; cin>>m;
    cout<<"(столбцы) N: "; cin>>n;
    
    int h[m][n];
    //h[строка][столбец]
    //М строк на N столбцов
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            h[i][j] = rand() % 20;
            cout<<h[i][j]<<"\t";
        }
        cout<<endl;
    }

    for (int i = m-1; i >= 0; i--)
    {
        bool b = true;
        for (int j = 0; j < n; j++)
            if( h[i][j] % 2 == 1 ) b = false;
        
        if ( b ){
            cout<<i<<endl;
            return 0;
        }
    }
    cout<<404<<endl;
}