#include <iostream>

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

	if ((a > b && c < b) || (a < b && c > b))
		cout<<b;
	else if ((b>c && c>a) || (b<c && c<a))
		cout<<c;
	else
		cout<<a;

	cout<<endl;

	return 0;
}