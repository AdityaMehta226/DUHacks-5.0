#include <stdio.h>
void main()
{
    int n,i,sum=0;
    printf("Enter A Number");
    scanf("%d",&n);
    printf("Factors of %d are as follows: \n",n);
    for (i=1;i<=n;i++)
    {
       if(n%i==0)
       {
        printf("%d ",i);
        sum+=i;
       }
    }
    printf("\nSum is: %d",sum); 
}