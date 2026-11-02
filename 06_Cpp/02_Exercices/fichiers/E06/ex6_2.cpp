#include <iostream>

int main() {
    unsigned int v{0xA5};

    std::cout << ((v >> 4) & 0xF) << ' ' << (v & 0xF) << '\n';
    std::cout << std::hex << (v ^ 0xFF) << std::dec << '\n';
    std::cout << static_cast<char>(0x41 + 2) << '\n';

    return 0;
}
