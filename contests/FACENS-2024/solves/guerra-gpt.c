#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_LEN 52  // 51 + 1 para o '\0'

char rotaciona_letra(char c, int n) {
    return ((c - 'A' + n) % 26) + 'A';
}

char substitui_caractere(char c) {
    switch (c) {
        case 'A': return '@';
        case 'S': return '$';
        case 'E': return '3';
        case 'I': return '!';
        case 'O': return '0';
        default: return 0; // Não substitui
    }
}

int main() {
    int n;
    char frase[MAX_LEN];

    while (1) {
        scanf("%d", &n);
        getchar(); // consumir o \n
        if (n == 0) break;

        fgets(frase, sizeof(frase), stdin);
        frase[strcspn(frase, "\n")] = '\0'; // Remove o \n

        if (n < 1 || n > 20 || strlen(frase) > 51) {
            printf("ERROR\n");
            continue;
        }

        for (int i = 0; frase[i] != '\0'; i++) {
            char c = frase[i];

            if (c == ' ') {
                putchar('#');
            } else {
                char sub = substitui_caractere(c);
                if (sub) {
                    putchar(sub);
                } else if (isupper(c)) {
                    putchar(rotaciona_letra(c, n));
                } else {
                    putchar(c); // caso não previsto, mantém
                }
            }
        }
        printf("\n");
    }

    return 0;
}
