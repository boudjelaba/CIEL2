#include <iostream>

int main() {
    int a{9};
    int b{4};
    double c{static_cast<double>(a) / b};

    std::cout << a / b << '\n';
    std::cout << a % b << '\n';
    std::cout << c << '\n';
    std::cout << static_cast<double>(a / b) << '\n';

    return 0;
}
