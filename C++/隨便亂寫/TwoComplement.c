#include<stdlib.h>
#include<stdio.h>
#include<stdbool.h>
#include<string.h>
#define MAX_SIZE 100

void *twoComplement(char * str){
    int i = strlen(str),len;
    bool first_1 = false;
    len = i;
   while(i != 0){
            if(str[i-1] == '1'){
                str[i-1] = first_1 ? '0' : '1';
            }else if(str[i-1] == '0'){
                str[i-1] = first_1 ? '1' : '0';
            }
            
    if(str[i-1] == '1' && !first_1) first_1 = true;
        i--;
        printf("when i = %d, first_1 = %d str[i] = %c\n",i,first_1,str[i]);
    }
    return str;
}


int main (){
char * str = (char *)malloc(sizeof(char)*MAX_SIZE);
printf("Enter a binary number: ");
scanf("%s", str);
printf("The two's complement of %s is %s\n", str, (char *)twoComplement(str));
free(str);
system("pause");
return 0;
}