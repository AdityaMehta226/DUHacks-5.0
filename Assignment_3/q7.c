#include <stdio.h>
void main()
{
    int a[5][3],r,c,l=1,sump=0,sums=0;
    for(r=0;r<5;r++)
    {
      for(c=0;c<3;c++)
      {
        printf("Enter The Sales Of Salesman %d For Product %d\n",r+1,c+1);
        scanf("%d",&a[r][c]);
      }
    }
    for(l=1;l<=2;l++)
    {
       if(l==1)
       {
         for(r=0;r<5;r++)
          {
           for(c=0;c<3;c++)
            {
              sump+=a[r][c];
            }
            printf("Sum Of Sales Products By Each Salesman %d is %d\n",r+1,sump);
          }
       }
       else
       {
        printf("---------------------------\n");
        for(r=0;r<3;r++)
        {
          for(c=0;c<5;c++)
          {
            sums+=a[c][r];
          }
          printf("Sum Of Sales Product %d is %d\n",r+1,sums);
          sums=0;
        }
       }
    }
}