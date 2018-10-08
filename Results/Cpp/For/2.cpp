#include <iostream>

using namespace std;

int main()
{
	int a,b;
	cout<<"A<B\nA: ";
	cin>>a;
	cout<<"B:";
	cin>>b;

	for ( int i = a; i <= b; i++ )
		cout<< i <<endl;

	return 0;
}