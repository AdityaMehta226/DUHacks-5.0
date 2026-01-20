#include <stdio.h>
void main()
{
    char s[1000],ch;
    int l,i,v=0;
    printf("Enter The Length Of An Array");
    scanf("%d ",&l);
    for(i=0;i<l;i++)
    {
       ch=getchar();
       if(ch==65||ch==69||ch==73||ch==79||ch==85) 
       {
        ch+=32;
        s[i]=ch;
        ++v;
       }
       else if(ch==97||ch==101||ch==105||ch==111||ch==117)
       {
        ch-=32;
        s[i]=ch;
        ++v;
       }
       else
       {
        s[i]=ch;
       }
    }
    for(i=0;i<l;i++)
    {
        printf("%c",s[i]);
    }
    printf("\nVowels: %d",v);
    
}