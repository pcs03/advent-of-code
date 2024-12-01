#include "utils.h"

namespace aoc {

void ltrim(std::string &str) {
    str.erase(str.begin(),
              std::find_if(str.begin(), str.end(),
                           [](unsigned char ch) { return !std::isspace(ch); }));
}

void rtrim(std::string &str) {
    str.erase(std::find_if(str.rbegin(), str.rend(),
                           [](unsigned char ch) { return !std::isspace(ch); })
                  .base(),
              str.end());
};

void trim(std::string &str) {
    ltrim(str);
    rtrim(str);
}

std::vector<std::string> split(std::string source, std::string delim) {
    std::vector<std::string> result;

    size_t start = 0;
    size_t end = source.find(delim);

    while (end != std::string::npos) {
        auto sub = source.substr(start, end - start);
        result.push_back(sub);

        start = end + delim.length();
        end = source.find(delim, start);
    }

    auto sub = source.substr(start, end - start);
    result.push_back(sub);

    return result;
}


} // namespace aoc
