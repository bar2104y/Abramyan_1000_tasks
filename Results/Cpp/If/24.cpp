#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	float x,y;
	cout<<"X:";
	cin>>x;

	if ( x > 0 )
		y = 2 * sin(x);
	else
		y = 6 - x;

	cout<< y <<endl;
	
	return 0;
}