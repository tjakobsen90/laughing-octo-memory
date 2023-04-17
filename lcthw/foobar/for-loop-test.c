#include <stdio.h>

int main()
{
    int i = 0;

    printf("First value: %d\n", i);

    for (i = 0; i < 3; i++) {
        printf("%d\n", i);
    }

    printf("Last value: %d\n", i);

    return 0;
}