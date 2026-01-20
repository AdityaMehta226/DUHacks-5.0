#include <stdio.h>
void main()
{
    char s[100][100],n,i,j;
    printf("Enter The Total Number Of Strings");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
      gets(s[i]);
    }
}