#include <iostream>

using namespace std;

int main()
{
	int a,k = 0, l = 0;

	for (int i = 1; i <= 3; i++)
	{
		cout<< "N"<<i<<": ";
		cin>>a;
		if ( a > 0 )
			k++;
		else if ( a < 0)
			l++;
	}

	cout<< "N<0 :" << l << "\nN>0: " << k <<endl;
	return 0;
}