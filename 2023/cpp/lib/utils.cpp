#include "utils.h"

namespace aoc {

void ltrim(std::string &string) {
    string.erase(string.begin(), std::find_if(string.begin(), string.end(),
                                              [](unsigned char ch) {
                                                  return !std::isspace(ch);
                                              }));
}

} // namespace aoc
