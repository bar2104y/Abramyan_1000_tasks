#include <iostream>

using namespace std;

int main()
{
	unsigned int a,b;
	cout<< "A>999: ";
	cin>>a;

	a = (a % 10000)/1000;

	cout<< a <<endl;

	return 0;
}