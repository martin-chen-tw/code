/*
�D��:���ȼƥ� 20250303
�ؼ�:���w��}�C�A�D��}�C�����h�֬ۦP����
�n�D:��}�C�ȦU�d�@��
�Ĥ@�����Ѧҥ��󵪮׼g�X�Ӫ�
*/
#include <iostream>

int eq_count(int len, int f[], int g[]){
    int count=0,i=1,tmp=f[0],ng=0,nf=0;
    while (ng!=(len-1)&&nf!=(len-1)){//��i���_��tmp���w��f[]�A��i������tmp���w��g[]
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
    printf("�}�C����%d�ӬۦP����!",eq_count(5,f,g));
    system("pause");
    return 0;
}