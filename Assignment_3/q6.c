#include <stdio.h>
void main()
{
    int a[100][100],f[100],i,j,r,c,l=0,i2,found,count;
    printf("Enter The Total Number Of Rows And Column\n");
    scanf("%d %d",&r,&c);
    printf("Enter All Elements\n");
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    for(i=0;i<r;i++)
    {
       for(j=0;j<c;j++)
       {
        found=0;
         for(i2=0;i2<l;i2++)
         {
           if(f[i2]==a[i][j])
           {
             found=1;
             break;
           }
         }
         if(found==0)
         {
            f[l]=a[i][j];
            ++l;
         }

       }
    }
     count=0;
    for(i2=0;i2<l;i2++)
    {
      for(i=0;i<r;i++)
      {
        for(j=0;j<c;j++)
        {
          if(f[i2]==a[i][j])
          {
            count++;
          }
        }
      }
   printf("Number: %d Frequncy: %d\n",f[i2],count);
   count=0;
    } 
}