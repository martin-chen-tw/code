/*
�D��:  (���)
�ؼ�:
�n�D:

*/
#include<iostream>
#include<string.h>
void trente(char *string){
    char data[4][10]; //�Ĥ@�h��ܦr�������A�B�ĤG�h��26�r��
    //data[0][i]��ܦr������
    //data[1][i]��ܬO�_�����r��("0"��ܵL"1"��ܦ�)
    //data[2][i]��ܦr���p��ɪ��ȩw��
    //data[3][i]��ܦr�����̲׭�
    char test[2][50];
    const char a = '+';
    inmemchrt* n = (string,a,strlen(string));
    memcpy(test[0],string,*n);
    printf("string �r��e���Ӧr��%s",test[1]);
return ;
}
int main(){
    char string[100];
    printf("�п�J���D:");
    scanf("%99s",string);
    trente(string);
    system("pause");
    return 0;
}