#include <iostream>

using namespace std;

int main()
{
    float n,r=0;
	cout<<"N: ";
	cin>>n;

	for ( float i = 1; i <= n; i++ )
        r += 1 / i;

    cout<<r<<endl;
    
    return 0;
}