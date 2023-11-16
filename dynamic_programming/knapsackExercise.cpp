#include <bits/stdc++.h>

using namespace std;

int memo[2020][2020];
int n,s;

const int INF = 0x3f3f3f;

int value[2020], wgt[2020];

int pd(int idx, int w) {

    if (w < 0) return -INF;
    if (idx == n) return 0;

    int& pdm = memo[idx][w];
    if (pdm!=-1) return pdm;

    pdm = max(pd(idx + 1, w - wgt[idx]) + value[idx], pd(idx + 1, w));

    return pdm;
}

int main() {

    cin >> s >> n;

    for(int i=0; i<n;i++) {
        cin >> wgt[i] >> value[i];
    }

    memset(memo, -1, sizeof(memo));

    cout << pd(0,s) << endl;

}