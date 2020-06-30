#include <stdio.h>
#include <stdlib.h>

//Найти среднее геометрическое a и b

int main()
{
	float a,b;
	
	printf("a: ");
	scanf("%f", &a);
	
	printf("b: ");
	scanf("%f", &b);
		
	printf("Res = sqrt(%f*%f) = %f", a,b,sqrt(a*b));	
	
	return 0;
}
