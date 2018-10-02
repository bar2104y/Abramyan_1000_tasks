#include <iostream>

using namespace std;

int main()
{
	int a,n;
	cout<<"Y (year): ";
	cin>>a;

	a = (( a-1 ) / 100) + 1;

	cout<< a <<endl;

	return 0;
}