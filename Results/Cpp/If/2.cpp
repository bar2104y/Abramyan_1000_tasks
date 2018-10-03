#include <iostream>

using namespace std;

int main()
{
	int a;
	cout<< "A: ";
	cin>>a;

	if ( a > 0 )
		a++;
	else
		a -= 2;

	cout<< a <<endl;
	return 0;
}