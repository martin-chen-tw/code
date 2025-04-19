/*
題目:  (日期)
目標:
要求:

*/
#include<iostream>
#include<string.h>
void trente(char *string){
    char data[4][10]; //第一層表示字母的狀態、第二層放26字母
    //data[0][i]表示字母種類
    //data[1][i]表示是否有此字母("0"表示無"1"表示有)
    //data[2][i]表示字母計算時的暫定值
    //data[3][i]表示字母的最終值
    char test[2][50];
    const char a = '+';
    inmemchrt* n = (string,a,strlen(string));
    memcpy(test[0],string,*n);
    printf("string 字串前五個字為%s",test[1]);
return ;
}
int main(){
    char string[100];
    printf("請輸入謎題:");
    scanf("%99s",string);
    trente(string);
    system("pause");
    return 0;
}