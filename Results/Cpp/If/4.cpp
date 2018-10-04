#include <iostream>

using namespace std;

int main()
{
	int a,k = 0;

	/*
	int b,c;
	cout<< "A: ";
	cin>>a;
	cout<< "B: ";
	cin>>b;
	cout<< "C: ";
	cin>>c;

	if ( a > 0 )
		k++;
	if ( b > 0 )
		k++;
	if ( c > 0 )
		k++;
	*/

	for (int i = 1; i <= 3; i++)
	{
		cout<< "N"<<i<<": ";
		cin>>a;
		if ( a > 0 )
			k++;
	}

	cout<< k <<endl;
	return 0;
}