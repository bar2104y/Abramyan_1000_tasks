#include <iostream>

using namespace std;

int main()
{
	float x,y;
	cout<<"f(x) = -x; x <= 0\nf(x) = x^2; 0 < x < 2;\nf(x) = 4; x >= 2";
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