/*
�D��:��t�ư��D 20250227
�ؼ�:f[]���C�Ӥ�g[]�����j�������`�M
�Ѧ�: https://chuiwenchiu.wordpress.com/2007/03/25/�t��k���D1-2�G��t�ȼƥ�-2/
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