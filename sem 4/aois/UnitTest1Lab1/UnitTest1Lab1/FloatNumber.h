#pragma once
#include <iostream>
class FloatNumber
{
private:
    
    const std::string clearMantiss = "00000000000000000000000"; 
    const std::string exp127 = "01111111"; 
    const std::string clearExp = "00000000";
    const std::string binOne = "00000001";
    const std::string binMinusOne = "11111111";
    
    std::string minus;
    std::string exp;
    std::string mantiss;

    void SeparateParts(float decNum, std::string& intPart, std::string& behindPoinPart);

    void MakeIntBinary(int decNum, std::string& output);

    void MakeBehindPointBinary(float DecNum, std::string& output);

    std::string BinarySum(std::string binaryNum1, std::string binaryNum2);

    bool IsExpMore(std::string exp1, std::string exp2);

    void MoveNum(std::string& mantiss, int added);

    void MantiissEqualize(FloatNumber& num1, FloatNumber& num2);

    FloatNumber MantissSum(FloatNumber& num1, FloatNumber& num2);

    std::string MakeAdditional(std::string binaryNum);

    std::string BinNumInverse(std::string binaryNum);

    float IntPartInFloat(std::string intPart);

    float BehindPointPartInFloat(std::string behindPointPart);

    void FillByNumWithIntPart(std::string& intPart, std::string& behindPointPart, int& index);

    void FillByNumWhithNoIntPart(std::string& intPart, std::string& behindPointPart, int& index);

    void SumOfTwoOnes(std::string& num1, std::string& num2, bool& oneForNextDigit, int index);

    void SumOfOneAndZero(std::string& num1, std::string& num2, bool& oneForNextDigit, int index);

    void SumOfTwoZeros(std::string& num1, std::string& num2, bool& oneForNextDigit, int index);

    void ConvertToStandartFormat(std::string& num1MantissBuff, FloatNumber& num1, FloatNumber& output);

    void MultByExpWithNegativeDegree(FloatNumber& copyOfMainNum, std::string& intPart, std::string& behindPointPart);

    void MultByExpWithPositiveDegree(FloatNumber& copyOfMainNum, std::string& intPart, std::string& behindPointPart);

public:
    FloatNumber();

    FloatNumber(float input_num);

    FloatNumber operator+(const FloatNumber& num1);

    void operator=(const FloatNumber& num1);

    std::string printFloatNumber();

    float calcInDec();
}; 