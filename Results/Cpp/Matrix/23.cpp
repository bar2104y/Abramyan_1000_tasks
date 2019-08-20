#include <iostream>
using namespace std;

int main(){
	int m,n;
    cout<<"(строки)  M: "; cin>>m;
    cout<<"(столбцы) N: "; cin>>n;
    
    int h[m][n];
    //h[строка][столбец]
    //М строк на M столбцов
	for (int i = 0; i < m; i++){
		for (int j = 0; j < n; j++){
			h[i][j] = i*i*(j+1)+1;
			cout<<h[i][j]<<"\t";
        }
		cout<<endl;
    }

	for (int i = 0; i < m; i++){
        int min = 10001;
        for (int j = 0; j < n; j++)
            if ( h[i][j] < min ) min = h[i][j];
        
        cout<<"Минимальный элемент строки "<<i<<" : "<<min<<endl;
    }

}