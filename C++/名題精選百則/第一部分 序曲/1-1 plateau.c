/*
肈ヘ:程盽キ 20250226
ヘ夹:钡Μ逼抖皚眖いт程キ
璶―:
1.跑计痹瓃禫ぶ禫
2.–皚砆琩高Ω
把σ https://chuiwenchiu.wordpress.com/2007/03/26/簍衡猭拜肈1-1程キ/
*/
#include<iostream>
template<int len, typename T>
int plateau(T f[]){
    int max=1,i,max_number=0,count=1,v;
    v=f[0];
    for(i=1;i<len;++i){
        if(f[i]==v){
            ++count;
            continue;
            }
        if(count>max){
            max=count;
            max_number=f[i-1];}
            v=f[i];
            count=1;
    }
return max_number;
}
int main(){//跑计羆璸5
    int f[]={1,2,2,3,3,3,4,5,5,6};
    printf("皚い程キ琌计%d!",plateau<10>(f));
    system("pause");
    return 0;
}