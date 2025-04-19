/*
題目:求質數  (20250314)
目標:輸入max，找到max以下所有質數
要求:
1.使用規律，如2,3 的倍數絕對不是，因此質數存在於6n+1 6n+5 中，n屬於正整數 

未完成品，不能輸入小於六的值，會有bug
*/
#include<iostream>
int prime(int max_count, int prime[]){
 
    prime[1] = max_count;
    return prime[];
}
int main(){
    int max_count,prime[50];
    printf("請輸入最大值需要多少個質數(至多50個):");
    scanf("%d",&max_count);
    system("pause");
    return 0;
}