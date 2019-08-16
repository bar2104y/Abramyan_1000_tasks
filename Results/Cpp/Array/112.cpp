#include <iostream>

using namespace std;

int main()
{
	int n,tmp;
	cout<<"N:";
	cin>>n;

	int a[n];

	for ( int i = 0; i<n; i++)
		a[i] = n-i;

	for ( int i = 0; i < n-1; i++){
		for ( int j = i; j < n-1; j++){
			if (a[j] > a[j+1]){
				tmp = a[i];
				a[i] = a[j];
				a[j] = tmp;
			}
		}
	}

	for (int i =0 ; i < n; i++)
		cout<<a[i]<<"\n";


	return 0;
}