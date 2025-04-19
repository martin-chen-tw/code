#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int* sieve(int count, int* size_out) {
    int i, j;
    int count2 = (count % 2 == 1) ? count / 2 + 1 : count / 2; // odd numbers only
    int *str = (int *)malloc(sizeof(int) * count2);
    if (!str) {
        printf("Memory allocation failed\n");
        exit(1);
    }

    str[0] = 2;
    for (i = 1; i < count2; i++) {
        str[i] = 2 * i + 1; // Fill with odd numbers
    }

    // Sieve process
    for (i = 1; i < count2; i++) {
        if (str[i] == 0) continue;
        for (j = i + 1; j < count2; j++) {
            if (str[j] != 0 && str[j] % str[i] == 0) {
                str[j] = 0; // Mark multiples
            }
        }
    }

    // Compress primes to the front of array
    int *primes = (int *)malloc(sizeof(int) * count2);
    int index = 0;
    for (i = 0; i < count2; i++) {
        if (str[i] != 0) {
            primes[index++] = str[i];
        }
    }

    free(str);
    *size_out = index;
    return primes;
}

int main() {
    int count;
    printf("請輸入最大值數的尋找範圍: ");
    scanf("%d", &count);

    int prime_count = 0;
    int *primes = sieve(count, &prime_count);

    printf("\n質數為: ");
    for (int i = 0; i < prime_count; i++) {
        printf("%d ", primes[i]);
    }
    printf("\n");

    free(primes);
    return 0;
}