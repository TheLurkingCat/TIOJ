#include <iostream>

using namespace std;
void swp(string &str1, string &str2) {
    string tmp = str1;
    str1 = str2;
    str2 = str1;
}
string lcs(string &str1, string &str2) {
    if (str1.size() > str2.size()) {
        swp(str1, str2);
    }
    int min_size = str1.size();
    int *lcs_arr = new int[min_size + 1];
    for (int i = 0; i <= min_size; i++) {
        lcs_arr[i] = 0;
    }
    int str1_len = str1.size();
    int str2_len = str2.size();
    int lcs_max = 0;
    int pointer = 0;
    for (int i = 0; i < str2_len; i++) {
        for (int j = str1_len - 1; j >= 0; j--) {
            if (str1[j] == str2[i]) {
                lcs_arr[j + 1] = lcs_arr[j] + 1;
            } else {
                lcs_arr[j + 1] = 0;
            }
            if (lcs_arr[j + 1] > lcs_max) {
                lcs_max = lcs_arr[j + 1];
                pointer = j;
            }
        }
    }
    delete[] lcs_arr;
    string tmp;
    for (int k = pointer - lcs_max; k <= pointer; k++) {
        tmp += str1[k];
    }
    return tmp;
}
int main() {
    string a;
    string b;
    cin >> a;
    cin >> b;
    cout << lcs(a, b) << '\n';
    return 0;
}