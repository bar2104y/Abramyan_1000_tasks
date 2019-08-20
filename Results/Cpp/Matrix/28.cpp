#include <iostream>
using namespace std;

int main(){
	int m,n;
	cout<<"(строки)  M: "; cin>>m;
	cout<<"(столбцы) N: "; cin>>n;
	
	int h[m][n];
    int a[n];
	//h[строка][столбец]
	//М строк на M столбцов
	for (int i = 0; i < m; i++){
		for (int j = 0; j < n; j++){
			h[i][j] = i*j+1;
			cout<<h[i][j]<<"\t";
		}
		cout<<endl;
	}

	for ( int j = 0; j < n; j++){
		int max = 0;
		for (int i = 0; i < m; i++)
			if (h[i][j] > max) max = h[i][j];
        a[j] = max;
	}

    int min = a[0];
    for ( int j = 1; j < n; j++)
        if ( a[j] < min ) min = a[j];
    cout<<"Result: "<<min<<endl;
}