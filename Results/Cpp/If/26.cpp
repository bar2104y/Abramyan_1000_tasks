#include <iostream>

using namespace std;

int main()
{
	float x,y;
	cout<<"X:";
	cin>>x;

	if ( x <= 0 )
		y = 0 - x;
	else if ( x >= 2 )
		y = 4;
	else
		y = x*x;

	cout<< y <<endl;
	
	return 0;
}