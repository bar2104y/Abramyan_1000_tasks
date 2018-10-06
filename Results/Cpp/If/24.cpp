#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	float x,y;
	cout<<"f(x) = 2 * sin(x); x > 0\nf(x) = 6-x; x <= 0\n";
	cout<<"X:";
	cin>>x;

	if ( x > 0 )
		y = 2 * sin(x);
	else
		y = 6 - x;

	cout<< y <<endl;

	return 0;
}