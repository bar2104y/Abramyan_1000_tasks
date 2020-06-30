#include <stdio.h>
#include <stdlib.h>

//Найти объем и плющадь куба

int main()
{
	float a;
	
	printf("a: ");
	scanf("%f", &a);
	
	printf("V = %f^3 = %f\nS = 6*%f^2 = %f", a, a*a*a, a, 6*a*a);	
	
	return 0;
}
