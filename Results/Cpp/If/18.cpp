#include <iostream>

using namespace std;

int main()
{
	int a,b,c;
	cout<<"A,B,C:\n";
	cin>>a>>b>>c;

	if (a == b)
		cout<<3;
	else if (a == c)
		cout<<2;
	else
		cout<<1;

	cout<<endl;

	return 0;
}