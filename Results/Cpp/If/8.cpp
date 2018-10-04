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
		cout<<a<<" "<<b;
	else if (b>a)
		cout<<b<<" "<<a;
	else
		cout<<"A = B";

	cout<<endl;

	return 0;
}