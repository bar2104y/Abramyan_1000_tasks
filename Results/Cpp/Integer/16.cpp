#include <iostream>

using namespace std;

int main()
{
	int a,b;
	cin>>a;

 	b = a / 100;
	a = a % 100;

	cout<< b << a%10 << a/10 <<endl;

	return 0;
}