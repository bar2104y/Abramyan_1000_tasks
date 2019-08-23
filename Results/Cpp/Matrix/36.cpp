#include <string>
#include <iostream> 
#include <ctime>

using namespace std;

void quickSort(int *numbers, int left, int right)
{
  int pivot;
  int l_hold = left;
  int r_hold = right;  
  pivot = numbers[left];
  while (left < right)  
  {
    while ((numbers[right] >= pivot) && (left < right))
      right--;  
    if (left != right)  
    {
      numbers[left] = numbers[right];  
      left++;  
    }
    while ((numbers[left] <= pivot) && (left < right))
      left++;  
    if (left != right)  
    {
      numbers[right] = numbers[left];  
      right--;  
    }
  }
  numbers[left] = pivot;
  pivot = left;
  left = l_hold;
  right = r_hold;
  if (left < pivot)
    quickSort(numbers, left, pivot - 1);
  if (right > pivot)
    quickSort(numbers, pivot + 1, right);
}

int main()
{
    srand(time(NULL));

    int m,n;
    int k = 0;
    cout<<"(строки)  M: "; cin>>m;
    cout<<"(столбцы) N: "; cin>>n;
    
    int h[m][n];
    //h[строка][столбец]
    //М строк на N столбцов
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            h[i][j] = rand() % 5;
            cout<<h[i][j]<<"\t";
        }
        cout<<endl;
    }

    for ( int i = 0; i<m; i++)
    {
        quickSort(h[i], 0, n-1);
    }
    cout<<endl;

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
            cout<<h[i][j]<<"\t";
        cout<<endl;
    }

    for (int i = 1; i < m; i++ ){
        bool f = true;
        for ( int j = 0; j < n; j++)
            if ( h[0][j] != h[i][j]) f = false;            
        
        if ( f ) k++;
    }
    cout<<k<<endl;
}