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
            h[i][j] = rand() % 5;
            cout<<h[i][j]<<"\t";
        }
        cout<<endl;
    }
    cout<<endl;

    int max = 0;
    int jj = 0;
    for ( int j = n; j >= 0; j--)
    {
        int k = 0;
        for ( int i = 0; i < m; i++ )
        {
            for ( int l = i+1; l < m; l++)
                if ( h[l][j] == h[i][j] )
                    k++;
            if ( k >= max ){
                max = k;
                jj = j;
            }
        }
    }
    
    cout<<jj<<endl;
}