#include <iostream>

using namespace std;

int main(){
    int m;
    cout<<"M(нечетное): "; cin>>m;
    
    int h[m][m];
    //h[строка][столбец]
    //М строк на M столбцов
    for (int i = 0; i < m; i++)
        for (int j = 0; j < m; j++)
            h[i][j] = i*j;

    for (int i = 0; i < m; i++){
        for (int j = 0; j < m; j++)
            cout<<h[i][j]<<"\t";
    cout<<endl;
    }
    cout<<endl;

    int k,i,j;
    //K - номер круга
    for ( k = 0; k < m/2; k++){
        //Строка
        for (j = k; j < m-k; j++){
            cout<<h[k][j]<<" ";
        }
        j -= 1;
        //Колонка
        for ( i = k+1; i< m-k; i++){
            cout<<h[i][j]<<" ";
        }
        i-=1;
        //Нижняя строка в обратную сторону
        for (j = m-k-2; j>=k; j--)
            cout<<h[i][j]<<" ";
        j+=1;
        for( i = m-k-2; i > k; i--)
            cout<<h[i][j]<<" ";
        
        cout<<endl;


    }
    cout<<h[m/2][m/2]<<endl;
}