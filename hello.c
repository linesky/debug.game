#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void colors(){
    printf("\x1b[43;37m");
}

void movenext(char *c,int ii,char ios){
    int i=0;
    int cc=(int)ios;
    char *ccc;
    ccc=(char*)&cc;
    strcpy(c,"");
    
    for(i=0;i<ii;i++){
       strcat(c,ccc); 
    }
    printf("move ford\n");
    printf("%s\n",c);

}
void stops(){
    int i=0;
    i=i+1;
}

int main(){
    int i=0;
    char x[1024];
    for(i=0;i<10;i++){
        colors();
        movenext(x,i,'*');
        stops();
    }
    return 0;

}
