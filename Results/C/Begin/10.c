#include <stdio.h>
#include <stdlib.h>

//Найти сумму, разность, частное и произведение a и b

int main()
{
	float a,b;
	
	printf("a: ");
	scanf("%f", &a);
	
	printf("b: ");
	scanf("%f", &b);
		
	printf("Differece = %f\n", a*a-b*b);	
	printf("Amount    = %f\n", a*a+b*b);
	printf("Division  = %f\n", a*a/b/b);
	printf("Multiply  = %f\n", a*a*b*b);
	
	return 0;
}
