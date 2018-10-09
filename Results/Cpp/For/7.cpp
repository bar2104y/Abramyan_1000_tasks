#include <iostream>

using namespace std;

int main()
{
	int a,b,k=0;
	cout<<"A<B\nA: ";
	cin>>a;
    cout<<"B: ";
	cin>>b;

	for ( int i = a; i <= b; i++ )
        k += i;

    cout<<k<<endl;
    
    return 0;
}