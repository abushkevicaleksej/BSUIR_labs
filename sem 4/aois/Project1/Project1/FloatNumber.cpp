#include "FloatNumber.h"

string FloatNumber::PadWithZeros(const string& input, int targetLength) const {
    string result = input;
    while (result.length() < targetLength) {
        result = "0" + result;
    }
    return result;
}
string FloatNumber::FloatToBinary(double num) const {
    string result;
    bool started = false;
    for (int i = 0; i < 23; ++i) {
        num *= 2;
        if (num >= 1) {
            result += '1';
            num -= 1;
            started = true;
        }
        else {
            if (started) {
                result += '0';
            }
        }
    }
    return result;
}

void FloatNumber::Convert(double num) {
    if (num < 0) {
        sign = "1";
        num = -num;
    }
    else {
        sign = "0";
    }
    int exp = 0;
    if (num >= 1) {
        exp = floor(log2(num));
        num /= pow(2, exp);
        exp += 127;
    }
    else {
        exp = 126;
    }
    exponent = PadWithZeros(IntToBinary(exp), 8);
    mantissa = PadWithZeros(FloatToBinary(num - 1), 23);
}

string FloatNumber::GetBinaryRepresentation() const {
    return sign + " " + exponent + " " + mantissa;
}

void FloatNumber::ConsoleOutput() {
    cout << this->sign << " " << this->exponent << " " << this->mantissa << endl;
}

string FloatNumber::IntToBinary(int num) const {
    string result;
    while (num > 0) {
        result = to_string(num % 2) + result;
        num /= 2;
    }
    return result.empty() ? "0" : result;
}

FloatNumber FloatNumber::operator+(const FloatNumber& other) const {
    double num1 = this->BinaryToFloat();
    double num2 = other.BinaryToFloat();
    return FloatNumber(num1 + num2);
}

double FloatNumber::BinaryToFloat() const {
    int exp = stoi(this->exponent, nullptr, 2) - 127;
    double mantissa = 1.0;
    for (int i = 0; i < 23; ++i) {
        if (this->mantissa[i] == '1') {
            mantissa += pow(2, -i - 1);
        }
    }
    double num = pow(2, exp) * mantissa;
    return this->sign == "1" ? -num : num;
}