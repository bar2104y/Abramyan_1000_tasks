#include <stdio.h>
#include <stdlib.h>

//Найти объем и плющадь параллелипипеда

int main()
{
	float a,b,c;
	
	printf("a,b,c: ");
	scanf("%f %f %f", &a,&b,&c);
	
	printf("V = %.3f*%.3f*%.3f = %.3f\nS = 2*(%.3f*%.3f+%.3f*%.3f+%.3f*%.3f) = %.3f", a,b,c, a*b*c, a,b,b,c,a,c, 2*(a*b+b*c+c*a));	
	
	return 0;
}
