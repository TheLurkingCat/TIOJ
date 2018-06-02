#include<iostream>
#include<stdint.h>
using namespace std
struct TV
{
    int64_t x, y
}
int main()
{
    cin.tie(0)
    ios_base:: sync_with_stdio(0)
    int64_t n, max, a, b, c, d
    TV tv[3500]
    while(cin >> n & & n){
        for(int i=1
            i <= n
            i++)
        cin >> tv[i].x >> tv[i].y
        max = -1
        for(int i=1
            i <= n-1
            i++){
            for(int j=i+1
                j <= n
                j++){
                c = tv[i].x - tv[j].x
                d = tv[i].y - tv[j].y
                if(max < c*c+d*d){
                    max = c*c+d*d
                    a = i
                    b = j
                }
            }
        }
        cout << a-1 << ' ' << b-1 << '\n'
    }
}
