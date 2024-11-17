#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

const int MAXN = 3000;
const int MAXM = 100;

vector<int> tree[MAXN + 1];
int b[MAXN + 1], g[MAXN + 1];
int dp[MAXN + 1][MAXM + 1];
int temp[MAXM + 1];

void dfs(int node, int parent, int m) {
    memset(dp[node], 0, sizeof(dp[node]));
    int monkey_votes = b[node];
    int gorilla_votes = g[node];

    dp[node][1] = (gorilla_votes > monkey_votes) ? 1 : 0;

    for (int neighbor : tree[node]) {
        if (neighbor == parent) continue;

        dfs(neighbor, node, m);

        memcpy(temp, dp[node], sizeof(temp));

        for (int i = m; i >= 1; --i) {
            for (int j = 1; j < i; ++j) {
                temp[i] = max(temp[i], dp[node][i - j] + dp[neighbor][j]);
            }
        }

        memcpy(dp[node], temp, sizeof(temp));
    }
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, m;
        cin >> n >> m;

        for (int i = 1; i <= n; ++i) {
            tree[i].clear();
        }

        for (int i = 1; i <= n; ++i) {
            cin >> b[i];
        }

        for (int i = 1; i <= n; ++i) {
            cin >> g[i];
        }

        for (int i = 0; i < n - 1; ++i) {
            int u, v;
            cin >> u >> v;
            tree[u].push_back(v);
            tree[v].push_back(u);
        }

        dfs(1, -1, m);

        cout << dp[1][m] << endl;
    }

    return 0;
}
