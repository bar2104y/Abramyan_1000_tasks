#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int a,b;
	cout<<"A: ";
	cin>>a;
	cout<<"B: ";
	cin>>b;

	if (a<b)
		swap(a,b);

	cout<<a<<" "<<b<<endl;

	return 0;
}