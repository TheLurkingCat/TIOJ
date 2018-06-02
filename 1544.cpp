#include <iostream>
#include <string>
using namespace std;
int main() {
    string str1, str2;
    int t;
    cin >> t;
    while (t--) {
        cin >> str1 >> str2;
        if (str1.length() > str2.length()) {
            cout << "0\n";
        } else if (str1.length() < str2.length()) {
            cout << "1\n";
        } else {
            if (str1.compare(str2) > 0) {
                cout << "0\n";
            } else {
                cout << "1\n";
            }
        }
    }
    return 0;
}
