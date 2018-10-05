#include <iostream>

using namespace std;

int main()
{
	int x1,y1,x2,y2,x3,y3,x4,y4;
	cout<<"X1, Y1:\n";
	cin>>x1>>y1;
	cout<<"X2, Y2:\n";
	cin>>x2>>y2;
	cout<<"X3, Y3:\n";
	cin>>x3>>y3;

	if ( x1 == x2 )
		x4 = x3;
	else if ( x1 == x3 )
		x4 = x2;
	else
		x4 = x1;

	if ( y1 == y2 )
		y4 = y3;
	else if ( y1 == y3 )
		y4 = y2;
	else
		y4 = y1;


	cout<< x4 << " " << y4 <<endl;

	return 0;
}