/*
題目:兩陣列最短距離 20250305
目標:查詢兩陣列中各一個元素相差值最小者
要求:
不要f[m],g[n]查詢m*n次(算出所有的距離)，運用已排好大小性質
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
        //printf("這次當這次的nf為%d\tng為%d\tf[nf]為%d\tg[ng]為%d\t其tmp為%d\tdiff為%d\n",nf,ng,f[nf],g[ng],tmp,diff);
    }
return diff;
}
int main(){
    int f[]={1,3,5,7,9},g[]={2,6,8};
    printf("兩陣列中各一個元素相差值最小者為%d\n",mindist(f,g,5,3));
    system("pause");
    return 0;
}