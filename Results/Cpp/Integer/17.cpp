#include <iostream>

using namespace std;

int main()
{
	unsigned int a,b;
	cout<< "A>999: ";
	cin>>a;

	a = (a % 1000)/100;

	cout<< a <<endl;

	return 0;
}