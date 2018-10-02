#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int a,n;
	cout<<"D (days): ";
	cin>>a;
	cout<<"N (days); ";
	cin>>n;

	a = ( a + n -1 ) % 7;
	a = fabs(a);

	cout<< a <<endl;

	return 0;
}