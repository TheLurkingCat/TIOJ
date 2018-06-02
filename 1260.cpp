#include <iostream>
#include <stdint.h>
using namespace std;
bool prime[300000001];
int ans[300000001];
int a, primes=0, x;
uint64_t count=0, total=0;
int main() {
  fill(prime, prime+300000001, true);
  ans[0] = ans[1] = 0;
  prime[0] = prime[1] = false;
  for(int i=2; i<300000001; i++){
    ans[i] = primes + prime[i];
    if(prime[i]){
      primes++;
      for(uint64_t j = (uint64_t)i*i; j<300000001; j+=i){
        prime[j] = false;
      }
    }
  }
  cin >> a;
  while(a--){
    cin >> x;
    cout << ans[x] << '\n';
  }
  return 0;
}