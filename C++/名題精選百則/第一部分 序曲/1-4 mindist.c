/*
�D��:��}�C�̵u�Z�� 20250305
�ؼ�:�d�ߨ�}�C���U�@�Ӥ����ۮt�ȳ̤p��
�n�D:
���nf[m],g[n]�d��m*n��(��X�Ҧ����Z��)�A�B�Τw�Ʀn�j�p�ʽ�
*/
#include<iostream>
int mindist(int f[],int g[],int flen, int glen){
    int ng=0,nf=0,diff= f[0]-g[0]>=0 ? f[0]-g[0] : g[0]-f[0],tmp;
    while((ng!=glen-1)||(nf!=flen-1)){
        if  (f[nf]>=g[ng]&&ng<glen)
            ng++;
        else if (nf<flen)
            nf++;
        tmp = f[nf]>=g[ng] ? f[nf]-g[ng] : g[ng]-f[nf];
        if(diff>tmp)
           diff=tmp; 
        //printf("�o����o����nf��%d\tng��%d\tf[nf]��%d\tg[ng]��%d\t��tmp��%d\tdiff��%d\n",nf,ng,f[nf],g[ng],tmp,diff);
    }
return diff;
}
int main(){
    int f[]={1,3,5,7,9},g[]={2,6,8};
    printf("��}�C���U�@�Ӥ����ۮt�ȳ̤p�̬�%d\n",mindist(f,g,5,3));
    system("pause");
    return 0;
}