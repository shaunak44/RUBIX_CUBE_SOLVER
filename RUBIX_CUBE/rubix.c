#include<stdio.h>
#include <stdlib.h>
/*
white - 0
green - 1
yellow 2
orange - 3
red - 4
blue - 5
4 is centrepiece in naming
*/
#define w 0
#define g 1
#define y 2
#define o 3
#define r 4
#define b 5

void swap(int *a, int *c) {
    int tmp = 0;
    tmp = *a;
    *a = *c;
    *c = tmp;
}
void print(int** colour)
{
    int i, j;
    for (i = 0; i < 6; i++) {
        for (j = 0; j < 9; j++) {
            printf("%d  ", colour[i][j]);
        }
        printf("\n");
    }
}
void RotateCW(int **color, int choice) {
    if (choice == g) {
        //for face
        //corner pieces
	swap(&color[1][0], &color[1][2]);
        swap(&color[1][2], &color[1][6]);
        swap(&color[1][2], &color[1][8]);
        //edge pieces
        swap(&color[1][1], &color[1][5]);
        swap(&color[1][3], &color[1][5]);
        swap(&color[1][7], &color[1][5]);

        //for outer edge
        swap(&color[0][5], &color[4][5]);
        swap(&color[3][7], &color[4][5]);
        swap(&color[2][3], &color[4][5]);

        swap(&color[2][0], &color[3][8]);
        swap(&color[4][8], &color[3][8]);
        swap(&color[0][8], &color[3][8]);

        swap(&color[4][2], &color[2][6]);
        swap(&color[0][2], &color[2][6]);
        swap(&color[3][2], &color[2][6]);
    }
    else if (choice == b) {

        //for face
        //corner pieces

        swap(&color[5][0], &color[5][2]);
        swap(&color[5][2], &color[5][6]);
        swap(&color[5][2], &color[5][8]);
        //edge pieces
        swap(&color[5][1], &color[5][5]);
        swap(&color[5][3], &color[5][5]);
        swap(&color[5][7], &color[5][5]);

        //for outer edge
        swap(&color[4][3], &color[0][3]);
        swap(&color[2][5], &color[0][3]);
        swap(&color[3][3], &color[0][3]);

        swap(&color[4][0], &color[0][0]);
        swap(&color[2][8], &color[0][0]);
        swap(&color[3][0], &color[0][0]);

        swap(&color[4][6], &color[0][6]);
        swap(&color[2][2], &color[0][6]);
        swap(&color[3][6], &color[0][6]);
    }
    else if (choice == r) {

        //for face
        //corner pieces

        swap(&color[4][0], &color[4][2]);
        swap(&color[4][2], &color[4][6]);
        swap(&color[4][2], &color[4][8]);
        //edge pieces
        swap(&color[4][1], &color[4][5]);
        swap(&color[4][3], &color[4][5]);
        swap(&color[4][7], &color[4][5]);

        //for outer edge
        swap(&color[1][1], &color[0][1]);
        swap(&color[2][1], &color[0][1]);
        swap(&color[5][1], &color[0][1]);

        swap(&color[1][2], &color[0][2]);
        swap(&color[2][2], &color[0][2]);
        swap(&color[5][2], &color[0][2]);

        swap(&color[1][0], &color[0][0]);
        swap(&color[2][0], &color[0][0]);
        swap(&color[5][0], &color[0][0]);
    }
    else if (choice == o) {

        //for face
        //corner pieces

        swap(&color[3][0], &color[3][2]);
        swap(&color[3][2], &color[3][6]);
        swap(&color[3][2], &color[3][8]);
        //edge pieces
        swap(&color[3][1], &color[3][5]);
        swap(&color[3][3], &color[3][5]);
        swap(&color[3][7], &color[3][5]);

        //for outer edge
        swap(&color[5][7], &color[0][7]);
        swap(&color[2][7], &color[0][7]);
        swap(&color[1][7], &color[0][7]);

        swap(&color[5][6], &color[0][6]);
        swap(&color[2][6], &color[0][6]);
        swap(&color[1][6], &color[0][6]);

        swap(&color[5][8], &color[0][8]);
        swap(&color[2][8], &color[0][8]);
        swap(&color[1][8], &color[0][8]);
    }
    else if(choice == y) {
	// for faces:
	// corner pieces
  	swap(&color[2][0], &color[2][2]);  	
  	swap(&color[2][2], &color[2][6]);  	
  	swap(&color[2][2], &color[2][8]);
	//edge pieces
  	swap(&color[2][1], &color[2][5]);  	
  	swap(&color[2][3], &color[2][5]);  	
  	swap(&color[2][7], &color[2][5]); 	
	//outer edge
  	swap(&color[4][1], &color[5][3]);  	
  	swap(&color[4][1], &color[3][7]);  	
  	swap(&color[4][1], &color[1][5]);  	
  	
	swap(&color[4][2], &color[5][0]);  	
  	swap(&color[4][2], &color[3][6]);  	
  	swap(&color[4][2], &color[1][8]);  	
  	
	swap(&color[4][0], &color[5][6]);  	
  	swap(&color[4][0], &color[3][8]);  	
  	swap(&color[4][0], &color[1][2]);  	
		
    }
    else if(choice == w) {
	// for faces:
	// corner pieces
  	swap(&color[0][0], &color[0][2]);  	
  	swap(&color[0][2], &color[0][6]);  	
  	swap(&color[0][2], &color[0][8]);
	//edge pieces
  	swap(&color[0][1], &color[0][5]);  	
  	swap(&color[0][3], &color[0][5]);  	
  	swap(&color[0][7], &color[0][5]); 	
	//outer edge
  	swap(&color[4][7], &color[1][3]);  	
  	swap(&color[4][7], &color[3][1]);  	
  	swap(&color[4][7], &color[5][5]);  	
  	
	swap(&color[4][6], &color[1][0]);  	
  	swap(&color[4][6], &color[3][2]);  	
  	swap(&color[4][6], &color[5][8]);  	
  	
	swap(&color[4][8], &color[1][6]);  	
  	swap(&color[4][8], &color[3][0]);  	
  	swap(&color[4][8], &color[5][2]);  	
    	
    }
}
void white_wrong_orientation(int **color, int front, int left, int right) {
	RotateCW((int **)color, front);
	RotateCW((int **)color, y);
	RotateCW((int **)color, y);
	RotateCW((int **)color, y);
	RotateCW((int **)color, right);
	RotateCW((int **)color, y);
}
void white_bottom_layer(int **color, int front, int left, int right) {
	RotateCW((int **)color, front);
	RotateCW((int **)color, front);
	RotateCW((int **)color, front);
	RotateCW((int **)color, right);
	RotateCW((int **)color, right);
	RotateCW((int **)color, right);
	RotateCW((int **)color, w);
	RotateCW((int **)color, w);
	RotateCW((int **)color, w);
	RotateCW((int **)color, right);
	RotateCW((int **)color, front);
	RotateCW((int **)color, front);	
}
void white_middle_layer(int **color, int front, int left, int right) {
	RotateCW((int **)color, right);
	RotateCW((int **)color, right);
	RotateCW((int **)color, right);
	RotateCW((int **)color, w);
	RotateCW((int **)color, w);
	RotateCW((int **)color, w);
	RotateCW((int **)color, right);
	RotateCW((int **)color, front);
	RotateCW((int **)color, front);	
}
int main() {
	int **input;
	input = (int **)malloc(sizeof(int *) * 6);
	for(int i = 0; i < 9; i++) {
		input[i] = (int *)malloc(sizeof(int) * 9);
	}
	for(int j = 0; j < 6; j++) {
		for(int k = 0; k < 9; k++) {
			input[j][k] = j;
			//printf("%d", input[j][k]);
		}
	}
	print((int **)input);
	RotateCW((int**)input, y);
	printf("\n\n");
	print((int **)input);
	return 0;
}
