#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int a,b,c,s = 0;
	cout<<"A,B,C:\n";
	cin>>a>>b>>c;

	if (a>b || a>c)
		s += a;
	if (c>a || c>b)
		s += c;
	if (b>a || b>c)
		s += b;

	cout<< s <<endl;

	return 0;
}