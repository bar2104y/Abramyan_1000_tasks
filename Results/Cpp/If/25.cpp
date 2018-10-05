#include <iostream>

using namespace std;

int main()
{
	int x,y;
	cout<<"X:";
	cin>>x;

	if ( x > 2 || x < 0-2 )
		y = 2 * x;
	else
		y = (0-3) - x;

	cout<< y <<endl;
	
	return 0;
}