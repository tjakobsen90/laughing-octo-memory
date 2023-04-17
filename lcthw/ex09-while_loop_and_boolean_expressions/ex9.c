#include <stdio.h>

int main(int argc, char *argv[])
{
    int i = 0;
    while (i < 25) {
        printf("%d\n", i);
        i++;
    }

    // need this to add a final newline
    printf("\n");

    int x = 25;
    while (x > -1) {
        printf("%d\n", x);
        x--;
    }

    // need this to add a final newline
    printf("\n");

    return 0;
}