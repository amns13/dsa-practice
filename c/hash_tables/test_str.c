#include <stdio.h>
#include <string.h>

int main(void) {
    char *s1 = "aman";
    char *s2 = "";
    printf("%d\n", strcmp(s1, s2));
    printf("%d\n", strcmp("aman", ""));
    return 0;
}