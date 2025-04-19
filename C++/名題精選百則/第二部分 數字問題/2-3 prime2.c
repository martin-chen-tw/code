/*
題目:求質數  (20250314)
目標:輸入max，找到max以下所有質數
要求:
1.使用規律，如2,3 的倍數絕對不是，因此質數存在於6n+1 6n+5 中，n屬於正整數
*/
/*更好的版本，原題目好像是要找n個質數，不小心理解成n前所有質數*/

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
printf("質數有:");
    for(i=0;i<prime_number;i++){
        printf("%d ",prime[i]);
    }
    return;
}
int main(){
    int max;
    printf("請輸入大於3的質數最大值:");
    scanf("%d",&max);
    prime2(max);
    system("pause");
    return 0;
}