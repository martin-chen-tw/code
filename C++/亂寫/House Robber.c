#include <iostream>
#include <time.h>
template<int max_len, typename T>
int ini_set(T f[]){
    if(max_len<=0)
        return -1;
    srand(time(NULL));//�]�w�üƺؤl
    double len = (rand()%max_len)+1;//��ܩФl�̦h��max_len�ӡA�̤֦�1��
    for(int i=0;i<len;++i)
        f[i] = rand()%10000 +1;//��ܩФl�������̦h�O10000�A�̤֬O1
    return len;
    }

int Greedy_Algorithm(int f[],int len){//�Q�����Τl�۾F�u�঳�@��
    int sum;
    return sum;
}
    int main(){
        int f[64];
        int len = ini_set<64>(f);
        
        
        return 0;
    }