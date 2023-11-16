#include <bits/stdc++.h>

using namespace std;

int recursiveKnapsack(int I[], int v[], int w[], int n, int wgt){
    if (n == 0 || wgt == 0) 
        return 0;

    if (w[n-1] > wgt) 
        return recursiveKnapsack(I, v, w, n-1, wgt);

    return max(v[n-1] + recursiveKnapsack(I, v, w, n-1, wgt - w[n-1]), recursiveKnapsack(I, v, w, n-1, wgt));
}

int memo[2000][2000]; // matriz global

int pdRecursiveKnapsack(int I[], int v[], int w[], int n, int wgt){
    if (memo[n][wgt] == -1) {
        if (w[n] > wgt)
            memo[n][wgt] = pdRecursiveKnapsack(I, v, w, n-1, wgt);
        
        memo[n][wgt] = max(v[n] + pdRecursiveKnapsack(I, v, w, n-1, wgt - w[n]), pdRecursiveKnapsack(I, v, w, n-1, wgt));
    }

    return memo[n][wgt];
}

int pdKnapsack(int I[], int v[], int w[], int n, int wgt){
    for (int x = 0; x <= wgt; x++) {
        memo[0][x] = 0;
        for (int j = 1; j <= n; j++) {
            memo[j][x] = -1;
            memo[j][0] = 0;
        }
    }

    return pdRecursiveKnapsack(I, v, w, n, wgt);
}
