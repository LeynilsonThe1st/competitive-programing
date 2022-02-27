#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);

    while (t != 0) {
        for(int i = 0; i < t; i++) {
            if (i == t-1)
                printf("%d\n", i+1);
            else
                printf("%d ",i+1);
        }
        scanf("%d", &t);
        if (t == 0)
            break;
    }
    return 0;
}



