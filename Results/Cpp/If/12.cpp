#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int a,b,c;
	cout<<"A: ";
	cin>>a;
	cout<<"B: ";
	cin>>b;
	cout<<"C: ";
	cin>>c;

	if (a > b && a > c)
		cout<<a;
	else if ( c>b && c>a)
		cout<<c;
	else
		cout<<b;

	cout<<endl;

	return 0;
}