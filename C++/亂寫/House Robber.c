#include <iostream>
#include <time.h>
template<int max_len, typename T>
int ini_set(T f[]){
    if(max_len<=0)
        return -1;
    srand(time(NULL));//砞﹚睹计贺
    double len = (rand()%max_len)+1;//ボ┬程Τmax_len程ぶΤ1
    for(int i=0;i<len;++i)
        f[i] = rand()%10000 +1;//ボ┬ず窥程琌10000程ぶ琌1
    return len;
    }

int Greedy_Algorithm(int f[],int len){//砆敖綟Τ
    int sum;
    return sum;
}
    int main(){
        int f[64];
        int len = ini_set<64>(f);
        
        
        return 0;
    }