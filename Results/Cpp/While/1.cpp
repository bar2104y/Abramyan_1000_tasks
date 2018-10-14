#include <iostream>

using namespace std;

main()
{
	int a,b;
	cout<<"A<B\nA, B:\n";
	cin>>a>>b;

	while (a >= b)
	{
		a -= b;
	}

	cout<<a<<endl;
}