#include <iostream>

using namespace std;

int main()
{
	float a;
	cout<<"Price: ";
	cin>>a;

	for ( int i = 1; i <= 10; i++ )
        cout<<i<<" kg = "<<a*i<<endl;

	return 0;
}