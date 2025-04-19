/*
肈ヘ:や皌计拜肈 20250227
ヘ夹:f[]い–ゑg[]じΩ计羆㎝
把σ: https://chuiwenchiu.wordpress.com/2007/03/25/簍衡猭拜肈1-2や皌计ヘ-2/
*/
#include<iostream>
template<int len_f,int len_g, typename T>
int gt_count(T f[],T g[]){
    int i,j,v,count=0;
    for(i=0;i<len_f;i++){
        v=f[i];
        for(j=0;j<len_g;j++){
            if(v>g[j])
            count++;
        }
    }
    return count;
}

int main(){
int f[]={1,3,5,7,9},g[]={2,3,4,7,8};
printf("%d",gt_count<5,5>(f,g));
system("pause");
return 0;
}