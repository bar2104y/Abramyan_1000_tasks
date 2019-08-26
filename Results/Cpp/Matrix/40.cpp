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
            h[i][j] = rand() % 10;
            cout<<h[i][j]<<"\t";
        }
        cout<<endl;
    }
    cout<<endl;

    int max = 0;
    int ii = 0;
    for ( int i = 0; i<m; i++)
    {
        int k = 0;
        for ( int j = 0; j < n; j++ )
        {
            for ( int l = j+1; l < n; l++)
                if ( h[i][j] == h[i][l] )
                    k++;
            if ( k >= max ){
                max = k;
                ii = i;
            }
        }
    }
    
    cout<<ii<<endl;
}