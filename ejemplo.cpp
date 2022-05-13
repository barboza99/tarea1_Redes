#include <stdio.h>
#include <string.h>
#include <cstdio>
#include <iostream>

#define TAM 100

int main() {
	int i = 0, j = 0, d[] = {3, 5, 2};
	char b[TAM]{0};
	char c;
	FILE *fichero;
	fichero = fopen("datos.bin", "rb");
	
	while(!feof(fichero)){
		c = fgetc(fichero); 
		if ( c >= 65 && c <= 90 ) { 
			c -= d[j]; 
			if ( c < 65 )
				c = c - 64 + 90;
		} else if ( c == 126 ) 
			c = 32;
		b[i] = c; 
		i++;
		if( j < 2 ) 
			j++;
		else
			j = 0;
	}
	fclose(fichero);
	printf("%s", b);
	printf("\n Fin de programa");
	
	return 0;
}
