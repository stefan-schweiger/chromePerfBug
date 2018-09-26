#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 220000
#define K 50000

int main()
{
    double duration;

    long sum = 0;

    // GENERATE
    clock_t t = clock();
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < K; j++) {
            sum += i - (j / 2);
        }
    }

    t = clock() - t;
    duration = (double)t / CLOCKS_PER_SEC * 1000;

    printf("%ld\n", sum);
    printf("%.2f\n", duration);

    return 0;
}
