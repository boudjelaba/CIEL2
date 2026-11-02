#include <cstddef>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v{3, 1, 4};
    v.push_back(1);
    v.push_back(5);

    int total{0};
    for (std::size_t i = 1; i < v.size(); i += 2) {
        total += v[i];
    }

    std::cout << v.size() << ' ' << total << '\n';

    return 0;
}
