#include <stdio.h>
void main()
{
    int r,c,s;
    int a=4;
    for(r=1;r<=4;r++)
    {
      for(s=2*(r-1);s>=1;s--)
      {
        printf(" ");
      }
      for(c=1;c<=(2*a-1);c++)
      {
        printf("* ");
      }
      a--;
      printf("\n");
    }
}