#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

char changeDefaultChars(char c) {
	switch(c) {
		case 'A': return '@';
		case 'S': return '$';
		case 'E': return '3';
		case 'I': return '!';
		case 'O': return '0'; 
		case ' ': return '#';
		default: return 0;
	}
}

char applyRotation(char c, int n) {
	return 'A' + ((c - 'A' + n) % 26);
}

int main(void) { 
	int rotationN;
	char string[52];

	do {
		scanf("%d", &rotationN);
		getchar();

		if (rotationN == 0) {
			break;
		}

		fgets(string, sizeof(string), stdin);
		string[strcspn(string, "\n")] = '\0';

		int stringLength = strlen(string);

		if (rotationN < 1 || rotationN > 20 || stringLength > 51 || stringLength < 1){
			printf("ERROR\n");
			continue;
		}

		for (int i=0; i<stringLength; i++) {
			char defaultChange = changeDefaultChars(string[i]);
			if (defaultChange) {
				putchar(defaultChange);
			} else if (isupper(string[i])) {
				printf("%c", applyRotation(string[i], rotationN));
			} else {
				putchar(string[i]);
			}
		}
		putchar('\n');
	} while(rotationN != 0);

	return 0;
}