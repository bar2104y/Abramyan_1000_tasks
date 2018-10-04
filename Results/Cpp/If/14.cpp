#include <iostream>

using namespace std;

int main()
{
	int a,b,c,min,max;
	cout<<"A,B,C: ";
	cin>>a>>b>>c;

	if (a>c && a>b)
		max = a;
	else if (b>c && b>a)
		max = b;
	else
		max = c;

	if (a<c && a<b)
		min = a;
	else if (b<c && b<a)
		min = b;
	else
		min = c;


	cout<< min << " " << max << endl;

	return 0;
}