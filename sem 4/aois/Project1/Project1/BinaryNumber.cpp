#include "BinaryNumber.h"
#include <unordered_map>

std::string BinaryNumber::GetValue()
{
    return value;
}

BinaryNumber BinaryNumber::operator+(BinaryNumber const& b) {
    BinaryCalculator calculator;
    std::string a_complement = toTwosComplement(value);
    std::string b_complement = toTwosComplement(b.value);

    BinaryNumber result = calculator.Add(a_complement, b_complement);
    std::string result_str = result.value;
    if (result_str[0] == '0')
    {
        return result_str;
    }
    result_str = fromTwosComplement(result.value);
    return result_str;
}

BinaryNumber BinaryNumber::operator*(BinaryNumber const& b) {
    BinaryCalculator calculator;
    std::string product = calculator.Multiply(value, b.value);
    return BinaryNumber(product);
}

void BinaryNumber::removeLeadingZeros() {
    size_t firstOnePos = value.find_first_of('1');
    if (firstOnePos != std::string::npos) {
        value = value.substr(firstOnePos);
    }
    else {
        value = "0";
    }
}

void BinaryNumber::deleteLeadingZerosAfterDot() {
    size_t dotPos = value.find('.');
    if (dotPos != std::string::npos) {
        size_t pos = value.find_first_not_of('0', dotPos + 1);
        if (pos != std::string::npos) {
            value.erase(dotPos + 6, pos - dotPos - 6);
        }
    }
}

void BinaryNumber::makePositive()
{
    if (!value.empty() && value[0] == '1') {
        value[0] = '0';
    }
}

std::string addZeroBeforeNumber( std::string& number) {
    if (number.empty() || number[0] == '0') {
        return number;
    }
    else {
        return "0" + number;
    }
}


BinaryNumber BinaryNumber::operator/(const BinaryNumber& divisor) const {
    BinaryNumber dividendCopy = *this;
    BinaryNumber divisorCopy = divisor;
    bool isNegativeResult = false;
    bool nextDigitAdded = false;


    if (dividendCopy.value[0] == '1' && divisorCopy.value[0] == '1') {
        dividendCopy.makePositive();
        divisorCopy.makePositive();
    }
    else
    {
        bool isNegativeResult = true;
        dividendCopy.makePositive();
        divisorCopy.makePositive();
    }

    dividendCopy.removeLeadingZeros();
    divisorCopy.removeLeadingZeros();
    std::string quotient = "0";
    std::string remainder = dividendCopy.value;
    std::string dividend = "";


    for (int i = 0; i < dividendCopy.value.size(); ++i) {
        if (!nextDigitAdded)
        {
            dividend += dividendCopy.value[i];
            deleteLeadingZeros(dividend);
        }
        dividend = addZeroBeforeNumber(dividend);
        divisorCopy.value = addZeroBeforeNumber(divisorCopy.value);
        if (binaryToDecimal(dividend) >= binaryToDecimal(divisorCopy.value)) {
            remainder = BinaryCalculator().Subtract(dividend, divisorCopy.value);
            deleteLeadingZeros(remainder);
            quotient += "1";
            if (!nextDigitAdded && i + 1 < dividendCopy.value.size()) {
                dividend = remainder + dividendCopy.value[i + 1];
                nextDigitAdded = true;
            }
            else {
                dividend = remainder + "0";
            }
        }
        else {
            quotient += "0";
            nextDigitAdded = false;
            if (remainder == "" && i + 1 >= dividendCopy.value.size()) {
                remainder = dividend;
            }
        }
    }
    if (remainder != "") {
        quotient += ".";
        quotient += remainder;
    }

    BinaryNumber result(quotient);

    int integerPartLength = result.value.find('.');
    if (integerPartLength == std::string::npos) {
        integerPartLength = result.value.length();
    }
    int missingDigits = 8 - integerPartLength;
    if (missingDigits > 0) {
        result.value.insert(0, missingDigits, '0');
    }

    if (isNegativeResult) {
        if (result.value[0] == '0') {
            result.value[0] = '1';
        }
    }

    return BinaryNumber(result);
}

void BinaryNumber::makeNegative()
{
    if (!value.empty() && value[0] == '0') {
        value[0] = '1';
    }
}

BinaryNumber BinaryNumber::operator-(const BinaryNumber& b) const
{
    BinaryCalculator calculator;

    BinaryNumber new_substractor = b;
    if (b.value[0] == '1')
    {
        new_substractor.makePositive();
    }
    else
    {
        new_substractor.makeNegative();
    }
    std::string a_complement = toTwosComplement(value);
    std::string b_complement = toTwosComplement(new_substractor.value);

    

    BinaryNumber result = calculator.Add(a_complement, b_complement);
    std::string result_str = result.value;
    if (result_str[0] == '0')
    {
        return result_str;
    }
    result_str = fromTwosComplement(result.value);
    return result_str;
}

int binaryToDecimal(std::string binary) {
    int decimal = 0;
    bool isNegative = (binary[0] == '1');

    size_t dotPosition = binary.find('.');
    std::string integerPart = binary.substr(1, dotPosition - 1);
    std::string fractionalPart = binary.substr(dotPosition + 1);

    for (int i = integerPart.size() - 1, exp = 0; i >= 0; --i, ++exp) {
        decimal += (integerPart[i] - '0') * pow(2, exp);
    }

    for (size_t i = 0; i < fractionalPart.size(); ++i) {
        decimal += (fractionalPart[i] - '0') * pow(2, -static_cast<int>(i + 1));
    }

    if (isNegative) {
        decimal = -decimal;
    }
    return decimal;
}

std::string intToBinary(int n) {
    std::string r;
    bool isNegative = n < 0;
    if (isNegative) {
        n = -n;
    }
    while (n) {
        r = (n % 2 == 0 ? "0" : "1") + r;
        n /= 2;
    }
    while (r.length() < 7) {
        r = "0" + r;
    }
    if (isNegative) {
        r = "1" + r;
    }
    else {
        r = "0" + r;
    }
    return r;
}