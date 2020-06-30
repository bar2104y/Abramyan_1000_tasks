#include <stdio.h>
#include <stdlib.h>

//Длина окружности и площадь круга радиуса R

int main()
{
	float r;
	
	printf("R: ");
	scanf("%f", &r);
	
	printf("L = 2*Pi*%f = %f\nS = Pi*%f^2 = %f", r, 2*3.14*r, r, r*r*3.14);	
	
	return 0;
}
