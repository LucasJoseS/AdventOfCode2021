#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  assert(argc == 2);
  int table[1000][1000] = {0};
  
  FILE *fp = fopen(argv[1], "r");
  assert(fp != NULL);

  while(ftell(fp) != 9267 && ftell(fp) != 109)
    {
      int x1, x2, y1, y2 = 0;
      fscanf(fp, "%d,%d -> %d,%d", &x1, &y1, &x2, &y2);

      if(x1 == x2 || y1 == y2)
	{
	  if(x1 == x2)
	    {
	      if(y1 > y2)
		{
		  while(y1 >= y2)
		    {
		      table[x1][y1]++;
		      y1--;
		    }
		}
	      else
		{
		  while(y1 <= y2)
		    {
		      table[x1][y1]++;
		      y1++;
		    }
		}
	    }

	  if (y1 == y2)
	    {
	      if(x1 > x2)
		{
		  while(x1 >= x2)
		    {
		      table[x1][y1]++;
		      x1--;
		    }
		}
	      else
		{
		  while(x1 <= x2)
		    {
		      table[x1][y1]++;
		      x1++;
		    }
		}
	    }
	}
      else
	{
	  if(x1 > x2 && y1 < y2)
	    {
	      while(x1 >= x2 && y1 <= y2)
		{
		  table[x1][y1]++;
		  x1--;
		  y1++;
		}
	    }
	  else if(x1 < x2 && y1 > y2)
	    {
	      while(x1 <= x2 && y1 >= y2)
		{
		  table[x1][y1]++;
		  x1++;
		  y1--;
		}
	    }
	  else if(x1 > x2 && y1 > y2)
	    {
	      while(x1 >= x2 && y1 >= y2)
		{
		  table[x1][y1]++;
		  x1--;
		  y1--;
		}
	    }
	  else if(x1 < x2 && y1 < y2)
	    {
	      while(x1 <= x2 && y1 <= y2)
		{
		  table[x1][y1]++;
		  x1++;
		  y1++;
		}
	    }
	  }
    }

  int count = 0;
  for(int i=0; i<1000; i++)
    {
      for(int j=0; j<1000; j++)
	{
	  printf("%d ", table[j][i]);
	  
	  if(table[j][i] >= 2)
	    {
	      count++;
	    }
	}
      printf("\n");
    }

  printf("%d\n", count);
}
  
