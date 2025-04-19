/*
題目:等值數目 20250303
目標:給定兩陣列，求兩陣列間有多少相同的值
要求:兩陣列值各查一次
第一次未參考任何答案寫出來的
*/
#include <iostream>

int eq_count(int len, int f[], int g[]){
    int count=0,i=1,tmp=f[0],ng=0,nf=0;
    while (ng!=(len-1)&&nf!=(len-1)){//當i為奇數tmp指定為f[]，當i為偶數tmp指定為g[]
        if(i%2==1){
            if(tmp>g[ng])
                ng++;
            else if(tmp==g[ng]){
                ++count;
                ng++;
            }
            else{
                tmp=g[ng];
                i++;
            }
        }
        else{
            if(tmp>f[nf])
                nf++;
            else if(tmp==f[nf]){
                ++count;
                nf++;
            }
            else{
                tmp=f[nf];
                i++;
            }
            }
}        
    return count;
}
int main(){
    int f[]={1,3,4,7,9},g[]={3,5,7,8,10};
    printf("陣列中有%d個相同的值!",eq_count(5,f,g));
    system("pause");
    return 0;
}