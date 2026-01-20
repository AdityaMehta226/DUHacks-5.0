#include <stdio.h>
void main()
{
  int mat[3][3],r,c,l,count=0;
  printf("Enter All 9 Elements\n");
  for(l=1;l<=3;l++)
  {
   for(r=0;r<3;r++)
    {
      for(c=0;c<3;c++)
      {
         if(l==1)
         {
          scanf("%d",&mat[r][c]);
         }
         else if(l==2)
         {
          if(count<3)
          {
           if(r!=c)
           {
            if(c==1&&r==0)
            {
              continue;
            }
            mat[r][c]=mat[r][c]+mat[c][r];
            mat[c][r]=mat[r][c]-mat[c][r];
           mat[r][c]=mat[r][c]-mat[c][r];
           count+=1;
           }
          } 
         }
         else if(l==3)
         {
           printf("%d ",mat[r][c]);
         }
      }
      if(l==3)
      {
        printf("\n");
      }
    }
  }
}