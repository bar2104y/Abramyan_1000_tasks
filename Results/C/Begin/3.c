#include <stdio.h>
#include <stdlib.h>

//Периметр прямоугольника со сторонами а и b

int main()
{
	float a,b;
	printf("a: ");
	scanf("%f", &a);
	
	printf("b: ");
	scanf("%f", &b);
	
	printf("P = 2*(%f+%f) = %f", a,b,2*(a+b));	
	
	return 0;
}
