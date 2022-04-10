#include <bits/stdc++.h>

using namespace std;

void solve() {
    cout << "Enter n: ";
    int n; cin >> n;
    vector <int> a(n); 

    cout << "Enter array: ";
    double denominator = 0, even_cnt = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];

        if (a[i] % 2 == 1) {
            even_cnt++;
            denominator += 1 / a[i];
        }
    } 

    double H = even_cnt / denominator;
    int cnt = 0;
    for (auto x : a) if (x > H) cnt++;

    cout << endl << "Result: " << cnt;
}

int main() {
    setlocale(LC_ALL, "Russian");

    solve();
}