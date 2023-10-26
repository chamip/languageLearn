//最长递增子序列
 #include <algorithm>
1 3 2 7 6 5 4
1 1
3 2
2 2
7 3
6 3
5 3
4 3
void max_inc_len(std::vector<int> vc, int &res) {
    int n = vc.size();
    std::vector<int> d(n, 1);
    for (int i = 1; i < n; ++i) {
        for (int j = i - 1; j >= 0; --j) {
            if (vc[i] > vc[j]) {
                d[i] = max(d[j] + 1, d[i]);
            }
        }
    }
    res = *std::max_element(d.begin(), d.end());
    return ;
}