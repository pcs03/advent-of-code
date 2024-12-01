#include "utils.h"
#include <algorithm>
#include <fstream>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>

int main() {
    std::ifstream t("./../../data/test01.txt");
    std::stringstream buffer;
    buffer << t.rdbuf();

    std::vector<std::string> input = aoc::split(buffer.str(), "\n\n");

    std::vector<int> summed_numbers;

    for (auto section : input) {
        std::vector<std::string> section_numbers = aoc::split(section, ",");

        int sum = 0;

        aoc::printvec(section_numbers);

        for (std::string number : section_numbers) {
            sum += std::stoi(number);
        }

        summed_numbers.push_back(sum);

    }

    aoc::printvec(summed_numbers);
}
