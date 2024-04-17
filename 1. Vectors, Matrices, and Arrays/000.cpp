#include <stdio.h>
#include <math.h>

long long fall(int N){
    if (N==0){
        return 1;
    }else{
        return N*fall(N-1);
    }
}
int main(){
    float git;
    scanf("%f", &git);
    float a[10];
    float sum = 0;
    for (int i = 0;i<10;i++){
        a[i] = pow(2, i)*fall(i)*fall(i)/fall(2*i+1);
        sum += a[i];
        if (a[i]<git){
            break;
        }
    }
    printf("%f\n", sum*2);
    return 0;
}