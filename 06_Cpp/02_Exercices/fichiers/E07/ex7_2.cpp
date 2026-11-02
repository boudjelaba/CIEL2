#include <iostream>

int main() {
    int a{4};
    int b{9};
    int* p{&a};
    int& r{b};

    *p = *p + 1;
    p = &b;
    *p = *p * 2;
    r = r - 3;

    std::cout << a << ' ' << b << '\n';

    return 0;
}
