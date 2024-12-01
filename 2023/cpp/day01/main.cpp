#include <iostream>

int main() {

    std::string str = "    Hello, World!";

    aoc::ltrim(str);

    std::cout << str << std::endl;
}
