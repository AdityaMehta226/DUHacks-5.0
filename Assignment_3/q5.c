#include <stdio.h>
void main()
{
    printf("Enter A Number");
    int a[100][100],n,i,j1,j2;
    scanf("%d",&n);
    for(i=0;i<n;i++)//controls the row for array
    {
        for(j1=0;j1<=i;j1++)//controls the column for array
        {
            if(j1==0||j1==i)//first and last position stores 1 always
            {
                a[i][j1]=1;
            }
            else
            {
                a[i][j1]=a[i-1][j1-1]+a[i-1][j1];//Equation for the sum of elements in the previous row
            }
        }
    }
    for(i=1;i<=n;i++)
      {
          for(j1=n-i;j1>=1;j1--)//prints the space 
          {
              printf(" ");
          }
          for(j2=1;j2<=i;j2++)//prints the array
          {
            printf("%d ",a[i-1][j2-1]);
          }
         printf("\n");
      }
}