#pragma once

#include <algorithm>
#include <cctype>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>

namespace aoc {

void ltrim(std::string &str);
void rtrim(std::string &str);
void trim(std::string &str);
std::vector<std::string> split(std::string source, std::string delim);

template <typename T>
void printvec(std::vector<T>& vec) {
    for (const T& element : vec) {
        std::cout << element << ',';
    }

    std::cout << std::endl;
}

} // namespace aoc
