#include <stdio.h>
void main()
{
    int a[100][100],r,c,i,j,n,row[100],col[100],occ=0;
    printf("Enter The Number Of Rows And Columns\n");
    scanf("%d %d",&r,&c);
    printf("Enter All The Elements\n");
    for(i=0;i<r;i++)
    {
      for(j=0;j<c;j++)
      {
        scanf("%d",&a[i][j]);
      }
    }
    printf("Enter The Number To Be Searched\n");
    scanf("%d",&n);
    for(i=0;i<r;i++)
    {
      for(j=0;j<c;j++)
      {
        if(a[i][j]==n)
        {
          row[occ]=i+1;
          col[occ]=j+1;
          occ++;
        }
      }
    }
    printf("The Position Of %d is/are\n",n);
    for(i=0;i<occ;i++)
    {
      printf("Row: %d Column: %d\n",row[i],col[i]);
    }
}