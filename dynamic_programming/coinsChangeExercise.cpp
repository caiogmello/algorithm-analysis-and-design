#include <bits/stdc++.h>

using namespace std;

int memo[51][251];
int n, m;

const int INF = 0x3f3f3f;

int c[51];

int pd(int idx, int val) {

    if (val < 0) return INF;
    if (idx == m) return (val == 0) ? 0 : INF;

    int& pdm = memo[idx][val];
    
    if(pdm != -1) 
        return pdm;
        
    pdm = min(1 + pd(idx, val - c[idx]), pd(idx + 1, val));

    return pdm;
}

int main(){

    cin >> n >> m;

    for(int i = 0; i< m; i++) {
        cin >> c[i];
    }

    memset(memo, -1, sizeof(memo));
    
    cout << pd(0,n);
}