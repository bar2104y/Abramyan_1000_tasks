#include <iostream>

using namespace std;

int main()
{
	int x;
	cout<<"X:";
	cin>>x;

	if ( x % 4 == 0 && !( x % 100 == 0 && x % 400 != 0 ) )
		cout<<366;
	else
		cout<<365;

	cout<<endl;
	
	return 0;
}