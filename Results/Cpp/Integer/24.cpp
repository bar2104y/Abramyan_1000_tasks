#include <iostream>
#include <cmath>

using namespace std;

int main()
{


	int a;
	cout<< "D (days): ";
	cin>>a;

	a = a % 7;
	a = fabs(a);

	cout<< a <<endl;


	return 0;
}