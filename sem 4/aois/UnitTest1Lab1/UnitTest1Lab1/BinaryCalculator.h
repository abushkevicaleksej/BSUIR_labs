#pragma once
#include <string>
class BinaryCalculator {
public:
    std::string Add(std::string a, std::string b);

    std::string Multiply(std::string a, std::string b);

    std::string Subtract(std::string a, std::string b);
};

std::string toComplement(std::string binary);

std::string toTwosComplement(std::string binary);  

std::string fromTwosComplement(const std::string& twosComplement);

void deleteLeadingZeros(std::string& str);