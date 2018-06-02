#include <stdio.h>
#include "lib1044.h"
int main() {
    int left = 0, right, k, t;
    right = Initialize() + 1;
    while (left != (right - 1)) {
        t = (right + left) / 2;
        k = Guess(t);
        if (k) {
            right = t;
        } else {
            left = t;
        }
    }
    Report(right);
    return 0;
}