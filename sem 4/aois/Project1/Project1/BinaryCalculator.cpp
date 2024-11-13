#include "BinaryCalculator.h"


std::string BinaryCalculator::Add(std::string a, std::string b) {
    std::string result = "";
    int carry = 0;
    int maxLength = std::max(a.length(), b.length());
    while (a.length() < maxLength) a = "0" + a;
    while (b.length() < maxLength) b = "0" + b;

    for (int i = maxLength - 1; i >= 0; i--) {
        int sum = (a[i] - '0') + (b[i] - '0') + carry;
        result = char(sum % 2 + '0') + result;
        carry = sum / 2;
    }
    if (result.length() > 8) {
        result = result.substr(result.length() - 8);
    }
    return result;
}

std::string BinaryCalculator::Multiply(std::string a, std::string b) {
    bool isNegativeResult = (a[0] == '1' && b[0] == '0') || (a[0] == '0' && b[0] == '1');
    if (a[0] == '1') a = a.substr(1);
    if (b[0] == '1') b = b.substr(1);

    std::string result = "0";
    for (int i = b.size() - 1; i >= 0; --i) {
        if (b[i] == '1') {
            result = Add(result, a);
        }
        a = a + "0";
    }
    if (isNegativeResult) {
        result = '1' + result;
    }
    else {
        result = '0' + result;
    }

    return result;
}

std::string BinaryCalculator::Subtract(std::string a, std::string b) {
    std::string result = "";
    int borrow = 0;

    int maxLength = std::max(a.length(), b.length());
    while (a.length() < maxLength) a = "0" + a;
    while (b.length() < maxLength) b = "0" + b;

    for (int i = maxLength - 1; i >= 0; i--) {
        int bitA = a[i] - '0';
        int bitB = b[i] - '0';
        int subtract = bitA - bitB - borrow;
        if (subtract < 0) {
            subtract += 2;
            borrow = 1;
        }
        else {
            borrow = 0;
        }

        result = std::to_string(subtract) + result;
    }

    return result;
}


std::string toComplement(std::string binary) {
    if (binary[0] == '0')
    {
        return binary;
    }
    std::string complement = "";
    complement += binary[0];
    for (int i = 1; i < binary.length(); i++) {

        complement += (binary[i] == '0' ? "1" : "0");
    }
    return complement;
}

std::string toTwosComplement(std::string binary) {
    if (binary[0] == '0') {
        return binary;
    }
    BinaryCalculator calculator;
    binary = toComplement(binary);
    binary = calculator.Add(binary, "00000001");
    return binary;
}

std::string fromTwosComplement(const std::string& twosComplement) {
    std::string result = twosComplement;
    if (twosComplement[0] == '1') {
        bool borrow = true;
        for (int i = twosComplement.size() - 1; i >= 0; --i) {
            if (borrow) {
                if (twosComplement[i] == '1') {
                    result[i] = '0';
                    borrow = false;
                }
                else {
                    result[i] = '1';
                }
            }
        }
    }
    for (int i = 1; i < result.size(); ++i) {
        result[i] = (result[i] == '0' ? '1' : '0');
    }

    return result;
}

void deleteLeadingZeros(std::string& str) {
    size_t firstOneIndex = str.find('1'); 
    if (firstOneIndex != std::string::npos) {
        str = str.substr(firstOneIndex); 
    }
    else {
        str = "0"; 
    }
}
