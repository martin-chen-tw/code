/*
�D��: Armstrong �� (202050309)
�ؼ�: ��J�@�ӼƦr�A�P�_�O�_��armstrong��
�n�D:
���Ϋ��ơB���
*/
#include<iostream>
void arms1(int num){
    int num_dig=1,tem_pow=10,sum=0,tmp=0,sumt=1,j;
/*check the number of digit*/
    while(((num/tem_pow)!=0)||((num%tem_pow)/(tem_pow/10)==0)){
        tem_pow*=10;
        ++num_dig;
    }
        //printf("number of digit is %d\n",num_dig);
    tem_pow = 1;
/*check whether the number is the Armstrong number.*/
    for(int i=0;i<num_dig;i++){
        //�쥻�O�ϥ�math.h����pow(),��ӵo�{pow()���~�t�A���ʪ����b�ؤ@��tmp�ܼƬۭ��[�isum��
        tmp=(num/tem_pow)-(10*(num/(10*tem_pow)));
        sumt=1;
        for(j=0;j<num_dig;j++)
            sumt*=tmp;
        sum+=sumt;
        tem_pow*=10;
        //printf("wheni=%d,sum=%d,num=%d,tem_pow=%d\n",i,sum,num,tem_pow);
    }
    if(sum==num)
        printf("\n%d is a Armstrong Number!\n",num);
    else
        printf("\n%d isn't a Armstrong Number!\n",num);
}
int main(){
    unsigned int num;
    printf("�п�J�Ʀr: ");
    scanf("%d",&num);
    arms1(num);
    system("pause");
    return 0;
}


