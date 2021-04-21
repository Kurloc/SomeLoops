#include <stdio.h>
#include <time.h> 
#include <time.h>
     
clock_t start, end;
double cpu_time_used;


void main()
{
    start = clock();
    end = clock();
    int test[100000000];
    for (int i = 0; i < 100000000;i++) {
        if (i % 3 == 0) {
            test[i] = i;
        }
    }
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("fun() took %f seconds to execute \n", cpu_time_used);
}
