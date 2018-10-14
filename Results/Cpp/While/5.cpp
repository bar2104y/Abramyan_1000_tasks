#include <iostream>

using namespace std;

main()
{
    int n,k=0;
    cout<<"N:";
    cin>>n;

    cout<<n;
    while (n != 1)
    {
        k++;
        n/=2;
    }
    cout<<" = 2^"<<k<<endl;
}