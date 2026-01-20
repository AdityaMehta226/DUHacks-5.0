#include <stdio.h>
void main()
{
    int d,sum=0,n;
    printf("Armstrong Numbers are:\n");
    for(int i=1;i<=1000;i++)
    {
      n=i;
      if(i<10)
      {
        printf("%d\n",i);
      }
      else if(i<100 && i>=10)
      {
        for(int j=1;j<=2;j++)
        {
          sum=sum+((n%10)*(n%10));
          n/=10;
        }
        if(sum==i)
        {
          printf("%d\n",i);
          sum=0;
        }
        else
        {
          sum=0;
        }
      }
      else if(i<1000 && i>=100)
      {
        for(int j=1;j<=3;j++)
        {
          sum+=((n%10)*(n%10)*(n%10));
          n/=10;
        }
        if(sum==i)
        {
          printf("%d\n",i);
          sum=0;
        }
        else
        {
          sum=0;
        }
      }
    }
}