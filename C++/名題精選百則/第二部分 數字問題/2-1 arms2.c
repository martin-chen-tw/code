/*
�D��: Armstrong �� (202050309)
�ؼ�: �D�X��3��ƤU�Ҧ���armstrong��
�n�D:
���Ϋ��ơB���
*/
#include<iostream>
int arms1(int num){
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
    if(num==sum)
        return 1;
    else
        return 0;
}
void arms2(int num_dig){
unsigned int num = 1,sum = 1,i;
//����쥻pow���u�@
for(i=0;i<num_dig;i++)
    sum*=10;
for(i=1;i<sum;i++){
    //printf("when i=%d, arms1(i)=%d\n",i,arms1(i));
    if(arms1(i)==1)
        printf("%7d is an Armstrong number!\n",i);
}
}
int main (){
    unsigned int num;
    printf("�п�J�Ʀr(�ثe�̦h�u�䴩��7): ");
    scanf("%d",&num);
    arms2(num);
    system("pause");
    return 0;
}