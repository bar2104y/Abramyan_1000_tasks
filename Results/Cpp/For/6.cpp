#include <iostream>

using namespace std;

int main()
{
	float a,k;
	cout<<"Price: ";
	cin>>a;

	for ( float i = 1; i <= 10; i++ )
    {
        k = 1+ i/10;
        cout<<k<<" kg = "<<a*k<<endl;
    }
        

	return 0;
}