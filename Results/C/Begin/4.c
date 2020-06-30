#include <stdio.h>
#include <stdlib.h>

//Длина окружности по диаметру

int main()
{
	float d;
	
	printf("D: ");
	scanf("%f", &d);
	
	printf("L = Pi*%f = %f", d,3.14*d);	
	
	return 0;
}
