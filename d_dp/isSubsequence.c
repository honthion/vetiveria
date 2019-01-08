#include<stdio.h>
#include<stdbool.h>

bool isSubsequence(char* s, char* t) {
    while(*t){
         s += *s == *t++;
        printf("%s\n",s);
    }

    return !*s;
}


int main(int argc,char * argv[]){

    char* s = "adbcedff";
    char* t ="abq";
    bool a = isSubsequence(s,t);
    printf("%d",a);


}
