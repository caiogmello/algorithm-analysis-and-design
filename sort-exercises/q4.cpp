#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main(){
    int n, m, x, i, j;

    cin >> n;
    

    for(i=0;i<n;i++) {
        cin >> m;
        vector<int> v;

        for(j=0;j<m;j++) {
            cin >> x;   
            v.push_back(x);
        }

        sort(v.begin(), v.end());

        for(j=0;j<(m-1);j++) {
            cout << v[j] << " ";
        }
        cout << v[v.size()-1] << '\n';

    }
}