#include <iostream>

using namespace std;

int main()
{
	int x,y;
	cout<<"X, Y:\n";
	cin>>x>>y;

	if ( x > 0 )
		if ( y > 0 )
			cout<<1;
		else
			cout<<4;
	else
		if ( y > 0 )
			cout<<2;
		else
			cout<<3;

	cout<<endl;

	return 0;
}