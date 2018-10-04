#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int a,b,s;
	cout<<"A: ";
	cin>>a;
	cout<<"B: ";
	cin>>b;

	if (a != b)
		if (a > b)
			s = a;
		else
			s = b;
	else 
		s = 0;

	cout<<s<<" "<<s<<endl;

	return 0;
}