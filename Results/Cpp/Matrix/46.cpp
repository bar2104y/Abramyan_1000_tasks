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

	for ( int i = 0; i<m; i++)
	{
		int ms = 0;
		int jj = 0;
		for ( int j = 0; j < n; j++ )
			if ( h[i][j] > ms )
			{
				ms = h[i][j];
				jj = j;
			}

		bool f = true;
		for (int k = 0; k<m; k++ )
			if (h[k][jj] < ms)
				f = false;
		
		if (f) cout<<ms<<endl;					
	}	
}