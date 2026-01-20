#include <stdio.h>
void main()
{
  int a[100][100]={},r,c,max,min,i,j;
  printf("Enter The Number Of Row And Columns\n");
  scanf("%d %d",&r,&c);
  printf("Enter All Elements\n");
  for(i=0;i<r;i++)
  {
    for(j=0;j<c;j++)
    {
        scanf("%d",&a[i][j]);
    }
  }
  max=a[0][0];
  min=a[0][0];
  for(i=0;i<r;i++)
  {
    for(j=0;j<c;j++)
    {
       if(a[i][j]>max)
       {
        max=a[i][j];
       }
       else if(a[i][j]<min)
       {
        min=a[i][j];
       }
    }
  }
  printf("Max: %d Min: %d",max,min);
}