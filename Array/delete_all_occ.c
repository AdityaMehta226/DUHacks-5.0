#include <stdio.h>
void main()
{
    int a[100],l,r,n,occ=0,c=0,r2,pos[100]={-1};
    printf("Enter The Length Of An Array");
    scanf("%d",&l);
    printf("Enter All Elements");
    for(r=0;r<l;r++)
    {
        scanf("%d",&a[r]);
    }
    printf("Enter A Number Whose All Occurances Should Be Deleted");
    scanf("%d",&n);
    for(r=0;r<l;r++)
    {
        if(a[r]==n)
        {
            pos[occ]=r;
            ++occ;
        }
    }
   for(r2=0;r2<occ;r2++)
   {
    for (r=(pos[r2])-r2;r<(l-1);r++)
    {
        a[r]=a[(r+1)];
    }
    --l;
   }
   for(r=0;r<l;r++)
   {
     printf("%d ",a[r]);
   }
}