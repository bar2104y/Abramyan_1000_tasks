#include <iostream>

using namespace std;

int main()
{
	int x,y;
	cout<<"X, Y:\n";
	cin>>x>>y;

	if ( x == 0 && y == 0 )
		cout<<0;
	else if ( x == 0 || y == 0 )
		cout<<1;
	else
		cout<<3;


	cout<<endl;

	return 0;
}