#include <iostream>

using namespace std;

int main()
{
	int x;
	cout<<"X:";
	cin>>x;

	if (x % 2 == 0)
		cout<< "Четное ";
	else
		cout<< "Нечетное ";

	if ( x < 100 )
		cout<<"двузначное";
	else
		cout<<"трехзначное";


	cout<<endl;
	
	return 0;
}