#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <stdbool.h>

#define N 10

void try_increment(int octps[N][N], int row, int col) {
  if(row < N && row >= 0 && col < N && col >= 0) {
    if(octps[row][col] != 0) {
      octps[row][col]++;
    }
  }
}

void increment_arround(int octps[N][N], int row, int col) {
  int drow = row-1;
  int urow = row+1;
  int pcol = col-1;
  int fcol = col+1;

  try_increment(octps, urow, pcol);
  try_increment(octps, urow, col);
  try_increment(octps, urow, fcol);
  try_increment(octps, row, fcol);
  try_increment(octps, drow, fcol);
  try_increment(octps, drow, col);
  try_increment(octps, drow, pcol);
  try_increment(octps, row, pcol);
}

void flash(int octps[N][N], int row, int col) {
  octps[row][col] = 0;
  increment_arround(octps, row, col);
}

int main(int argc,  char **argv)
{
  assert(argc == 2);
  FILE *fp = fopen(argv[1], "r");
  if(fp == NULL) { printf("File not found\n"); exit(1); }

  int octopus[N][N];
  int counter_steps = 0;
  int aux;
  bool all_is_zero = true;

  for(int r=0; r<N; r++) {
    for(int c=0; c<N; c++) {
      fscanf(fp, "%lc", &aux);
      octopus[r][c] = aux - 48;
    }
    fscanf(fp, "\n");
  }

  do {
    for(int row=0; row<N; row++) {
      for(int col=0; col<N; col++) {
        octopus[row][col]++;
      }
    }

    bool try_flash = true;
    while(try_flash) {
      try_flash = false;
        
      for(int row=0; row<N; row++) {
        for(int col=0; col<N; col++) {
          if(octopus[row][col] > 9) {
            flash(octopus, row, col);
            try_flash = true;
          }
        }
      }
    }

    all_is_zero = true;
    for(int row=0; row<N; row++) {
      for(int col=0;  col<N; col++) {
        if(octopus[row][col] != 0) {
          all_is_zero = false;
        }
      }
    }

    counter_steps++;
  } while(!all_is_zero);

  for(int row=0; row<N; row++) { for(int col=0; col<N; col++) { printf("%d ", octopus[row][col]); } printf("\n"); }
  printf("%d\n", counter_steps);
}
