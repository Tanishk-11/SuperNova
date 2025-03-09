#include <bits/stdc++.h>
#include <vector>
using namespace std;

void dfs(vector<int>& ans, vector<int> adj[], vector<int>& vis, int start) {
        for (auto itr : adj[start]) {
            if (vis[itr] == 0) {
                ans.push_back(itr);
                vis[itr] = 1;
                dfs(ans,adj,vis,itr);
            }
        }
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> adj[n + 1];
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    vector<int> ans;
    vector<int> vis(n+1, 0);
    vis[1] = 1;
    ans.push_back(1);
    
    dfs(ans, adj, vis, 1);

    cout << "DFS traversal starting from vertex 1: ";
    for (int i = 0; i < n; i++) {
        cout << ans[i] << " ";
    }
    cout << endl;

    return 0;
}
