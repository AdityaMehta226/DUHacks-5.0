#include <stdio.h>
void main()
{
    int a[100][100],t[100][100],r,c,i,j,co=0;
    printf("Enter Dimensions Of Matrix\n");
    scanf("%d %d",&i,&j);
    if(i==j)
    {
      for(r=0;r<i;r++)
      {
        for(c=0;c<j;c++)
        {
            printf("Enter The Element Of Row: %d Column: %d\n",r+1,c+1);
            scanf("%d",&a[r][c]);
        }
      }
      for(r=0;r<i;r++)
      {
        for(c=0;c<j;c++)
        {
            if(r!=c)
            {
                if(a[r][c]!=a[c][r])
                {
                   co+=1;
                   break;
                }
            }
        }
        if(co==1)
        {
            printf("Not A Symmetric Matrix");
            break;
        }
      }
      if(co!=1)
      {
        printf("Symmetric Matrix");
      }
    }
    else
    {
       printf("Not A Symmetric Matrix Because The Matrix Should Be Square Matrix");
    }
}