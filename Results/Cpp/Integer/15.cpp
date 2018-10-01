#include <iostream>

using namespace std;

int main()
{
	int a,b;
	cin>>a;
    
    b = a / 100;
    a = a % 100;

    cout<< a / 10 << b << a%10 <<endl;
    
	return 0;
}