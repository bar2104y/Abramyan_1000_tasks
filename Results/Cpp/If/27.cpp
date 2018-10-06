#include <iostream>

using namespace std;

int main()
{
	float x,y;
	cout<<"f(x) = 0; x < 0\nf(x) = 1;";
	cout<<"X:";
	cin>>x;

	if ( x < 0 )
		y = 0;
	else if ( (0 <= x && x < 1) || 2 <= x && x < 3 )
		y = 1;
	else
		y = -1;

	cout<< y <<endl;
	
	return 0;
}