#include <string>
#include <iostream> 
#include <ctime>

using namespace std;

void quickSort(int *numbers, int left, int right)
{
  int pivot; // разрешающий элемент
  int l_hold = left; //левая граница
  int r_hold = right; // правая граница
  pivot = numbers[left];
  while (left < right) // пока границы не сомкнутся
  {
    while ((numbers[right] >= pivot) && (left < right))
      right--; // сдвигаем правую границу пока элемент [right] больше [pivot]
    if (left != right) // если границы не сомкнулись
    {
      numbers[left] = numbers[right]; // перемещаем элемент [right] на место разрешающего
      left++; // сдвигаем левую границу вправо
    }
    while ((numbers[left] <= pivot) && (left < right))
      left++; // сдвигаем левую границу пока элемент [left] меньше [pivot]
    if (left != right) // если границы не сомкнулись
    {
      numbers[right] = numbers[left]; // перемещаем элемент [left] на место [right]
      right--; // сдвигаем правую границу вправо
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