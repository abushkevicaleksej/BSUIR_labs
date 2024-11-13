#pragma once
#include "BinaryCalculator.h"
class BinaryNumber {
public:
    
    std::string GetValue();

    BinaryNumber(std::string value) : value(value) {}

    BinaryNumber operator+(BinaryNumber const& b);

    BinaryNumber operator*(BinaryNumber const& b);

    void removeLeadingZeros();

    void deleteLeadingZerosAfterDot();

    void makePositive();
    
    BinaryNumber operator/(const BinaryNumber& divisor) const;

    void makeNegative();

    BinaryNumber operator-(const BinaryNumber& divisor) const;

private:

    std::string value;
};

int binaryToDecimal(std::string binary);

std::string intToBinary(int n);

std::string addZeroBeforeNumber(const std::string& number);