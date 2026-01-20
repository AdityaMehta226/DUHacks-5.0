#include <stdio.h>
void main()
{
    for (int i=1;i<=6;i++)
    {
        for(int j=1;j<=i;j++)
        {
            if(i%2!=0)
            {
                (j%2==0)?printf("0 "):printf("1 ");
            }
            else
            {
                (j%2==0)?printf("1 "):printf("0 ");
            }
        }
        printf("\n");
    }
}