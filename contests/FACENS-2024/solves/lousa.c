#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int main(void) {
	// A = largura
	// B = altura
	// C = distância até o sensor 1
	// D = distância até o sensor 2
	int a, b, c, d;
	
	while(1) {
		scanf("%d %d %d %d", &a, &b, &c, &d);
		if (a == 0 && b == 0 && c == 0 && d == 0) break;
		
		if (fabs(c - d) > a || (c + d) < a) {
			printf("DEFEITO\n");
			continue;
		}
		
		double angleCos = (a*a + c*c - d*d) / (2.0 * a * c);
		
		if (angleCos < -1) angleCos = -1;
		if (angleCos > 1) angleCos = 1;
		
		double angleValue = acos(angleCos);
		
		double x = c * cos(angleValue);
		double y = c * sin(angleValue);
		
		if (x < 0 || x > a || y < 0 || y > b) {
			printf("DEFEITO\n");
		}
		else {
			printf("%d %d\n", (int)round(x), (int)round(y));
		}
	}	
	
	return 0;
}
