#include <iostream>

using namespace std;

int main()
{
	int a,b,k = 0;
	cout<<"A<B\nA: ";
	cin>>a;
	cout<<"B:";
	cin>>b;

	for ( int i = a+1; i < b; i++ ){
        cout<< i <<endl;
        k++;
    }

    cout<<"K = "<<k<<endl;

	return 0;
}