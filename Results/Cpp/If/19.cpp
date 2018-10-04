#include <iostream>

using namespace std;

int main()
{
	int a,b,c,d;
	cout<<"A,B,C,D:\n";
	cin>>a>>b>>c>>d;

	if (a == b == c)
		cout<<4;
	else if (a == c == d)
		cout<<2;
	else if ( a == b == d )
		cout<<3;
	else
		cout<<1;

	cout<<endl;

	return 0;
}