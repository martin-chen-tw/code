/*
�D��:�D���  (20250314)
�ؼ�:��Jmax�A���max�H�U�Ҧ����
�n�D:
1.�ϥγW�ߡA�p2,3 �����Ƶ��藍�O�A�]����Ʀs�b��6n+1 6n+5 ���An�ݩ󥿾��
*/
/*��n�������A���D�ئn���O�n��n�ӽ�ơA���p�߲z�Ѧ�n�e�Ҧ����*/

#include<iostream>
#include<math.h>
void prime2(int max_number){
int prime[20000]={2,3},prime_number=2,tmp,i,j,k,num;
float sqrt_number;
for(i=3;i<=max_number;i+=6){
    for(k=0;k<2;k++){
        tmp = 0;
        num = ((k==0)?(i+2):(i+4));
        sqrt_number=sqrt((float)num);
    for(j=0;j<prime_number;j++){
        if(prime[j]>sqrt_number) 
            break;
        if(num % prime[j] == 0) { 
            tmp = 1; break; }
        }
        if(tmp==0)
            prime[prime_number++]=num;
    }
}
while(prime[prime_number - 1] > max_number) {
    prime_number--;
}
printf("��Ʀ�:");
    for(i=0;i<prime_number;i++){
        printf("%d ",prime[i]);
    }
    return;
}
int main(){
    int max;
    printf("�п�J�j��3����Ƴ̤j��:");
    scanf("%d",&max);
    prime2(max);
    system("pause");
    return 0;
}