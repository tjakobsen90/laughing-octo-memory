#include <stdio.h>

int main(int argc, char *argv[])
{
    // create two arrays we care about

    // A single block of memory
    int ages[] = { 23, 43, 12, 89, 2 };

    // An array of char pointers, each pointer points to a char so each string in its own block of memory
    char *names[] = {
        "Alan", "Frank",
        "Mary", "John", "Lisa"
    };

    // safely get the size of ages
    int count = sizeof(ages) / sizeof(int);
    int i = 0;

    // first way using indexing
    for (i = 0; i < count; i++)
    {
        printf("%s has %d years alive.\n", names[i], ages[i]);
    }

    printf("---\n");

    // set up the pointers to the start of the arrays

    // points to the block of memory where ages is
    int *cur_age = ages;

    // A pointer to a pointer, it points to an array of pointers (names)
    char **cur_name = names;

    // second way of using pointers, not a good way!
    for (i = 0; i < count; i++)
    {
        // *() means you need to retrieve the content of the pointer
        printf("%s is %d years old.\n", 
            *(cur_name + i), *(cur_age +i));
    }

    printf("---\n");

    // third way basically the same as the second, pointers are just arrays (but not the same!)
    // This is the preferred way, the compiler should handle the optimization
    for (i = 0; i < count; i++) {
        printf("%s is %d years old again.\n", cur_name[i], cur_age[i]);
    }

    printf("---\n");

    // fourth way with pointers in a stupid complex way
    for (cur_name = names, cur_age = ages;
            (cur_age - ages) < count; cur_name++, cur_age++) {
        printf("%s is %d years old again.\n", *cur_name, *cur_age);
    }

    printf("---\n");

    // Extra's
    // Pointers and array are almost interchangable, you can place pointers into an array
    // End of everystring contains the null-byte: \0 (x\00)

    // Create a pointer to the address (ex: 78A1A298) of height, not its value (100)
    int height = 100;
    int *cur_height = &height;

    return 0;
}