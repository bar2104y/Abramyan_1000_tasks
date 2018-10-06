#include <iostream>

using namespace std;

int main()
{
	int x;
	cout<<"X:";
	cin>>x;

	if ( x < 0 )
		if (x % 2 == 0)
			cout<<"x < 0, x // 2";
		else
			cout<<"x < 0, x !// 2";
	else if (x == 0)
		cout<<"x = 0";
	else
		if ( x % 2 != 0 )
			cout<<"x > 0, x !// 2";
		else
			cout<<"x > 0, x // 2";
	cout<<endl;
	
	return 0;
}