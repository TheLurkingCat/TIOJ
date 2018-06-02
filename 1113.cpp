#include <algorithm>
#include <iostream>
#include <string>

using namespace std;
int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    string s;
    while (cin >> s) {
        sort(s.begin(), s.end());
        do {
            cout << s << '\n';
        } while (next_permutation(s.begin(), s.end()));
        cout << '\n';
    }
}
