/*
�D��:�̱`���x 20250226
�ؼ�:�����@�Ӥw�Ʀn���Ǫ��}�C�A�ñq����X�̪������x
�n�D:
1.�ܼơB�ԭz�V�ֶV�n
2.�C�Ӱ}�C�u�Q�d�ߤ@��
�Ѧ� https://chuiwenchiu.wordpress.com/2007/03/26/�t��k���D1-1�G�̪����x/
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
int main(){//�ܼ��`�p5��
    int f[]={1,2,2,3,3,3,4,5,5,6};
    printf("�}�C���̪������x�O�Ʀr%d!",plateau<10>(f));
    system("pause");
    return 0;
}