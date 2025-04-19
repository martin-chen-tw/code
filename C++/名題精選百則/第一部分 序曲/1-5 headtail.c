/*
題目:等值首尾和 20250305
目標:求x[]所有前段和後段和有值相同的量
要求:
盡量不要把前段和後段和算出來當作兩個以排列好大小的矩陣來計算，使用前後段和類似由小排到大的矩陣來處理
*/
#include<iostream>
//#include"..//liberary.h//array_operation.c"
int headtail(int x[], int len){
    len--;
    int count=0,fsum=x[0],bsum=x[len],i=0,j=0;
    //printf("起始狀態:\nfsum=%2d\tbsum=%2d\ti=%2d\tj=%2d\tcount=%2d\t\n",fsum,bsum,i,j,count);
    if(fsum==bsum)
            count++;
    while(i!=len||j!=len){    
        //printf("計算狀態:\n");
        if(fsum<=bsum){
            i++;
            fsum=fsum+x[i];}
        else{
            j++;
            bsum=bsum+x[len-j];}
        if(fsum==bsum)
            count++;
    //printf("fsum=%2d\tbsum=%2d\ti=%2d\tj=%2d\tcount=%2d\t\n",fsum,bsum,i,j,count);
    }
        return count;
        
}
int main(){

    int x[] = {3,6,2,1,4,5,2};
    printf("矩陣中，前後段和總共有%2d個為相同值",headtail(x,7));
    system("pause");
    return 0;
}