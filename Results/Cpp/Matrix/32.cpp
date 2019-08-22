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
    //М строк на M столбцов
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            h[i][j] = -10 + rand() % 20;

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
            cout<<h[i][j]<<"\t";
        cout<<endl;
    }

    for (int i = 0; i < m; i++)
    {
        int p = 0; int o = 0;
        for ( int j = 0; j < n; j++)
            if ( h[i][j] > 0 )
                p++;
            else if (h[i][j] < 0)
                o++;
        
        if ( p == o )
        {
            cout<<i<<endl;
            return 0;
        }
            
    }
    cout<<"Не найдено"<<endl;
}