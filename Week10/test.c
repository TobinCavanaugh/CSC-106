#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>

#define uint uint64_t

uint factorial(uint a)
{
    if (a == 1)
    {
        return a;
    }

    return a * factorial(a - 1);
}

int main()
{

    printf("%" PRIu64 "\n", factorial(100));

    while (1)
    {
    }
}