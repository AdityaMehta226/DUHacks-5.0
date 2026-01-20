#include <stdio.h>
void main()
{
    
    int n,sum=0,p=0,ng=0;
    for(int i=1;i<=10;i++)
    {
       printf("Enter A Number\n");
       scanf("%d",&n);
          if(n>0)
          {
            ++p;
            sum+=n;
          }
          else if(n<0)
          {
            ng++;
          }
       
    }
    printf("-------------------------\nSum is: %d\nTotal Positive Numbers: %d\nTotal Negative Numbers: %d",sum,p,ng);
}