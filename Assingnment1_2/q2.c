#include <stdio.h>
void main()
{
    int r;
    for(r=1;r<=2;r++)
    {
        printf("Enter the lower limit and upper limit");
        int l,u,c=0,i,j;
        scanf("%d%d",&l,&u);
        printf("Prime Numbers Are\n");
         if(u>l)
          {
            for(i=l;i<=u;i++)
            {
               for(j=1;j<=i;j++)
               {
                 if(i>=j)
                 {
                    if(i%j==0)
                    {
                        c++;
                    }
                 }
               }
               if(c==2)
                 {
                    printf("%d\n",i);
                    c=0;
                 }
                 else
                 {
                    c=0;
                 }
            }
          }
    }
}