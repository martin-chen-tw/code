/*
�D��:���ȭ����M 20250305
�ؼ�:�Dx[]�Ҧ��e�q�M��q�M���ȬۦP���q
�n�D:
�ɶq���n��e�q�M��q�M��X�ӷ�@��ӥH�ƦC�n�j�p���x�}�ӭp��A�ϥΫe��q�M�����Ѥp�ƨ�j���x�}�ӳB�z
*/
#include<iostream>
//#include"..//liberary.h//array_operation.c"
int headtail(int x[], int len){
    len--;
    int count=0,fsum=x[0],bsum=x[len],i=0,j=0;
    //printf("�_�l���A:\nfsum=%2d\tbsum=%2d\ti=%2d\tj=%2d\tcount=%2d\t\n",fsum,bsum,i,j,count);
    if(fsum==bsum)
            count++;
    while(i!=len||j!=len){    
        //printf("�p�⪬�A:\n");
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
    printf("�x�}���A�e��q�M�`�@��%2d�Ӭ��ۦP��",headtail(x,7));
    system("pause");
    return 0;
}