#include <stdio.h>
#include <stdlib.h>

//Найти среднее арифметическое a и b

int main()
{
	float a,b;
	
	printf("a: ");
	scanf("%f", &a);
	
	printf("b: ");
	scanf("%f", &b);
		
	printf("Res = (%f+%f)/2 = %f", a,b,(a+b)/2);	
	
	return 0;
}
