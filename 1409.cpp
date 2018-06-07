#include <stdint.h>
#include <algorithm>
#include <iostream>

using namespace std;

uint64_t arr[1000000];

int main(void) {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    uint64_t n, i;
    int64_t k;
    while (cin >> n) {
        for (i = 0; i < n; i++) {
            cin >> arr[i];
        }
        sort(arr, arr + n);
        k = arr[n - 1];
        i = 0;
        while (k >= 0 && i < n - 1) {
            k -= arr[i];
            i++;
        }
        if (k >= 0) {
            cout << "NO\n";
        } else {
            cout << "YES\n";
        }
    }
    return 0;
}