#include <stdio.h>
void main()
{
    int a[100],occ=0,l,r,pos[100]={-1},num,ocu,n;
    printf("Enter The Length Of An Array");
    scanf("%d",&l);
    printf("Enter all %d elements",l);
    for(r=0;r<l;r++)//It Is L not 1.
    {
       scanf("%d",&a[r]); 
    }
    printf("Enter The nth Occurance Of A Number And That Number");
    scanf("%d %d",&ocu,&num);
    for(r=0;r<l;r++)
    {
        if(num==a[r])
        {
            pos[occ]=r;
            occ=occ+1;
        }
    }
    if(occ>=ocu)
    {
        for(r=l;r>=pos[ocu-1];r--)
        {
            a[r+1]=a[r];
        }
    printf("Enter The Number To Be Inserted");
    scanf("%d",&a[pos[ocu-1]]);
    }
     for(r=0;r<=l;r++) 
        {
            printf("%d ",a[r]);
        }
}