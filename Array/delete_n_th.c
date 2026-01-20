#include <stdio.h>
void main()
{
    int a[100],l,r,n,occ=0,c=0,pos[100]={-1},occu;
    printf("Enter The Length Of An Array");
    scanf("%d",&l);
    printf("Enter All Elements");
    for(r=0;r<l;r++)
    {
        scanf("%d",&a[r]);
    }
    printf("Enter A Number And Its nth Occurance Which Should Be Deleted");
    scanf("%d %d",&n,&occu);
    for(r=0;r<l;r++)
    {
        if(a[r]==n)
        {
            pos[occ]=r;
            ++occ;
        }
    }
    for(r=pos[occu-1];r<l;r++)
    {
        a[r]=a[r+1];
    }
    for(r=0;r<l-1;r++)
    {
        printf("%d ",a[r]);
    }
}