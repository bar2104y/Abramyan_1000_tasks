#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int a,b,c;
	cout<<"A,B,C:\n";
	cin>>a>>b>>c;

	b = fabs(b-a);
	c = fabs(c-a);

	if ( c>b )
		cout<<"B; d(A; B) = "<<b;
	else
		cout<<"C; d(A; C) = "<<c;

	cout<<endl;

	return 0;
}