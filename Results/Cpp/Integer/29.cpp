#include <iostream>

using namespace std;

int main()
{
	int a,b,c;
	cout<<"A: ";
	cin>>a;
	cout<<"B: ";
	cin>>b;
	cout<<"C: ";
	cin>>c;

	int s = a*b;

	a = a/c;
	b = b/c;

	s = s - (a*b*c*c);

	cout<< "N: " << a*b << "\n";
	cout<< "S: " << s <<endl;



	return 0;
}