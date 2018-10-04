#include <iostream>

using namespace std;

int main()
{
	float a,b,c;
	cout<<"A,B,C:\n";
	cin>>a>>b>>c;

	if ((a < b && b < c) || (a > b && b > c) )
	{
		a *= 2;
		b *= 2;
		c *= 2;
	}
	else
	{
		a = 0-a;
		b = 0-b;
		c = 0-c;
	}

	cout<< a << " " << b << " " << c <<endl;

	return 0;
}