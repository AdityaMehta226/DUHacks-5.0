#include <stdio.h>
void main()
{
    for (int i=1;i<=6;i++)
    {
        for(int j=1;j<=i;j++)
        {
            if(j%2==0)
            {
              printf("0 ");  
            }
            else
            {
               printf("1 ");
            }
        }
        printf("\n");
    }
}