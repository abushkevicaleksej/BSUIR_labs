#include <iostream>
#include <string>
#include <cmath>

using namespace std;

class FloatNumber {
private:
    string sign;
    string exponent;
    string mantissa;

public:
    FloatNumber();
    FloatNumber(double num);
    void Convert(double num);
    string GetBinaryRepresentation() const;
    void ConsoleOutput();
    string FloatToBinary(double num) const;
    FloatNumber operator+(const FloatNumber& other) const;

private:
    string IntToBinary(int num) const;
    string PadWithZeros(const string& input, int targetLength) const;
    double BinaryToFloat() const;
};


FloatNumber::FloatNumber() : sign("0"), exponent(""), mantissa("") {}

FloatNumber::FloatNumber(double num) : sign("0"), exponent(""), mantissa("") {
    Convert(num);
}

string PadWithZeros(const string& input, int targetLength);

string FloatToBinary(double num);

void Convert(double num);

string GetBinaryRepresentation();

void ConsoleOutput();

string IntToBinary(int num);

FloatNumber operator+(const FloatNumber& other);

double BinaryToFloat();
