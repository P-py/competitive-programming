#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

double truncate(double x, int n) {
    double factor = 1;
    for(int i = 0; i < n; i++) factor *= 10;
    return (int)(x * factor) / factor;
}

int main(void) {
	int n;
	
	do {
		scanf("%d", &n);
		if (n == 0) break;
		
		for (int i=0; i<n; i++) {
			char coord1[20], coord2[20];
			scanf("%s %s", coord1, coord2);
			
			double results[2];
			
			char *coords[] = {coord1, coord2};
			
			for (int j=0; j<2; j++){
				int g, m, s;
				char dir;
				
				sscanf(coords[j], "%dg%dm%ds%c", &g, &m, &s, &dir);
				
				double decimalValue = (g) + (m/60.0) + (s/3600.0);
				
				if (dir == 'S' || dir == 'W') {
					decimalValue *= -1;
				}
				
				results[j] = truncate(decimalValue, 2);
			}
			
			printf("%.2f %.2f\n", results[0], results[1]);
		}
	} while(n != 0);
	
	return 0;
}
