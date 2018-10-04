#include <iostream>

using namespace std;

int main()
{
	int a,b;
	cout<<"A: ";
	cin>>a;
	cout<<"B: ";
	cin>>b;

	if (a>b)
		cout<<2;
	else if (b>a)
		cout<<1;
	else
		cout<<"A = B";

	cout<<endl;

	return 0;
}