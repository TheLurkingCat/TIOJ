#include <iostream>
using namespace std;
int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    char now[72];
    int k, ans;
    bool getR, getG, getB, getY, getP;
    cin >> k;
    while (k--) {
        ans = 0;
        getR = getG = getB = getY = getP = true;
        for (int i = 0; i < 72; i++) {
            cin >> now[i];
        }
        for (int i = 0; i < 72; i++) {
            if (ans == 5) break;
            if (getR && now[i] == 'R') {
                ans++;
                getR = false;
            } else if (getG && now[i] == 'G') {
                ans++;
                getG = false;
            } else if (getB && now[i] == 'B') {
                ans++;
                getB = false;
            } else if (getY && now[i] == 'Y') {
                ans++;
                getY = false;
            } else if (getP && now[i] == 'P') {
                ans++;
                getP = false;
            }
        }
        cout << ans << '\n';
    }
}
