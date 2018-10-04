#include <iostream>

using namespace std;

int main()
{
	int a,b,s;
	cout<<"A: ";
	cin>>a;
	cout<<"B: ";
	cin>>b;
	
	if (a != b)
		s = a+b;
	else 
		s = 0;

	cout<<s<<" "<<s<<endl;

	return 0;
}