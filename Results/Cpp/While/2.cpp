#include <iostream>

using namespace std;

main()
{
	int a,b,k=0;
	cout<<"A<B\nA, B:\n";
	cin>>a>>b;

	while (a >= b)
	{
		a -= b;
		k++;
	}

	cout<<"in A - "<<k<<" B"<<endl;
}