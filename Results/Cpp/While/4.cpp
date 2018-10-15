#include <iostream>

using namespace std;

main()
{
	int n;
	cout<<"N:";
	cin>>n;

	while (n % 3 == 0)
	{
		n /= 3;
	}
	cout<<(n ==1 ? "true":"false")<<endl;
}
