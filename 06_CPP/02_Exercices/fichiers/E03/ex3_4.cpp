#include <iostream>

int main() {
    double tension{12.0};

    if (tension < 11.0 && tension > 14.0) {
        std::cout << "Tension correcte\n";
    } else {
        std::cout << "Alarme\n";
    }

    return 0;
}
