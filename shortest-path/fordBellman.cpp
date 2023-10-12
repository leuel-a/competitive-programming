#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    // Using a vector of tuple to store edges
    vector<tuple<int, int, int>> edges;

    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        edges.push_back(make_tuple(u, v, w));
    }

    // Using a map to represent distances
    map<int, int> distances;
    for (int i = 1; i <= n; ++i) {
        distances[i] = 30000;
    }
    distances[1] = 0;

    for (int i = 0; i < n - 1; ++i) {
        for (const auto& [u, v, w] : edges) {
            if (distances[u] != 30000 && distances[u] + w < distances[v]) {
                distances[v] = distances[u] + w;
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << distances[i] << " ";
    }

    return 0;
}
