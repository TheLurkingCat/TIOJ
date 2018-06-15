#include <stdint.h>
#include <iostream>
#define MAX 1000001
using namespace std;
bool prime[MAX];
int ans[MAX];
int a, primes = 0, x;
int main() {
    fill(prime, prime + MAX, true);
    ans[0] = ans[1] = 0;
    prime[0] = prime[1] = false;
    for (int i = 2; i < MAX; i++) {
        ans[i] = primes + prime[i];
        if (prime[i]) {
            cout << i << ',';
            primes++;
            for (uint64_t j = (uint64_t)i * i; j < MAX; j += i) {
                prime[j] = false;
            }
        }
    }
    cin >> a;
    while (a--) {
        cin >> x;
        cout << ans[x] << '\n';
    }
    return 0;
}