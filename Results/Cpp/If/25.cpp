#include <iostream>

using namespace std;

int main()
{
	int x,y;
	cout<<"f(x) = 2*x; x < -2 or x > 2\nf(x) = -3 * x; -2 =< x <= 2\n";
	cout<<"X:";
	cin>>x;

	if ( x > 2 || x < 0-2 )
		y = 2 * x;
	else
		y = (0-3) - x;

	cout<< y <<endl;
	
	return 0;
}