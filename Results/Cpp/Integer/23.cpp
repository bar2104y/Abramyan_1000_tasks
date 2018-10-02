#include <iostream>

using namespace std;

int main()
{
	unsigned int a,b;
	cout<< "A (sec): ";
	cin>>a;

	a = (a % 3600) / 60;

	cout<< a <<endl;

	return 0;
}