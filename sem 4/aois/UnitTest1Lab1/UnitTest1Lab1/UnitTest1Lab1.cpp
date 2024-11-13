
#include "pch.h"
#include "CppUnitTest.h"
#include "BinaryNumber.h"
#include "FloatNumber.h"
using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1Lab1
{
	TEST_CLASS(UnitTest1Lab1)
	{
	public:
		
		TEST_METHOD(IsTheSameChecker)
		{
			BinaryCalculator calc;
			int x = 4;
			BinaryNumber a(intToBinary(x));
			Assert::AreEqual(binaryToDecimal(a.GetValue()), x);
		}
		TEST_METHOD(IsTheSameCheckerForNegative)
		{
			BinaryCalculator calc;
			int x = -3;
			BinaryNumber a(intToBinary(x));
			Assert::IsTrue(a.GetValue() == "10000011");
		}
		TEST_METHOD(IsStraightAndReverseTheSame)
		{
			BinaryCalculator calc;
			int x = 4;
			BinaryNumber a(intToBinary(x));
			Assert::AreEqual(toComplement(a.GetValue()), a.GetValue());
		}
		TEST_METHOD(IsAddedAndReverseTheSame)
		{
			BinaryCalculator calc;
			int x = 17;
			BinaryNumber a(intToBinary(x));
			Assert::AreEqual(toTwosComplement(a.GetValue()), a.GetValue());
		}
		TEST_METHOD(ReverseForNegative)
		{
			BinaryCalculator calc;
			int x = -17;
			BinaryNumber a(intToBinary(x));
			Assert::IsTrue(toComplement(a.GetValue()) == "11101110");
		}
		TEST_METHOD(SumFirst)
		{
			BinaryCalculator calc;
			int x = -17,y=3;
			BinaryNumber a(intToBinary(x)), b(intToBinary(y));
			BinaryNumber sum = a + b;
			Assert::AreEqual(binaryToDecimal(sum.GetValue()), -14);
		}
		TEST_METHOD(SumSecond)
		{
			BinaryCalculator calc;
			int x = 17, y = 3;
			BinaryNumber a(intToBinary(x)), b(intToBinary(y));
			BinaryNumber sum = a + b;
			Assert::AreEqual(binaryToDecimal(sum.GetValue()), 20);
		}
		TEST_METHOD(SumThird)
		{
			BinaryCalculator calc;
			int x = -17, y = -3;
			BinaryNumber a(intToBinary(x)), b(intToBinary(y));
			BinaryNumber sum = a + b;
			Assert::AreEqual(binaryToDecimal(sum.GetValue()), -20);
		}
		TEST_METHOD(DiffFirst)
		{
			BinaryCalculator calc;
			int x = -17, y = -3;
			BinaryNumber a(intToBinary(x)), b(intToBinary(y));
			BinaryNumber diff = a - b;
			Assert::AreEqual(binaryToDecimal(diff.GetValue()), -14);
		}
		TEST_METHOD(DiffSecond)
		{
			BinaryCalculator calc;
			int x = -17, y = 3;
			BinaryNumber a(intToBinary(x)), b(intToBinary(y));
			BinaryNumber diff = a - b;
			Assert::AreEqual(binaryToDecimal(diff.GetValue()), -20);
		}
		TEST_METHOD(DiffThird)
		{
			BinaryCalculator calc;
			int x = 17, y = 3;
			BinaryNumber a(intToBinary(x)), b(intToBinary(y));
			BinaryNumber diff = a - b;
			Assert::AreEqual(binaryToDecimal(diff.GetValue()), 14);
		}
		TEST_METHOD(MultFirst)
		{
			BinaryCalculator calc;
			int x = 17, y = 3;
			BinaryNumber a(intToBinary(x)), b(intToBinary(y));
			BinaryNumber mult = a * b;
			Assert::AreEqual(binaryToDecimal(mult.GetValue()), 51);
		}
		TEST_METHOD(MultSecond)
		{
			BinaryCalculator calc;
			int x = -17, y = 0;
			BinaryNumber a(intToBinary(x)), b(intToBinary(y));
			BinaryNumber mult = a * b;
			Assert::AreEqual(binaryToDecimal(mult.GetValue()), 0);
		}
		TEST_METHOD(MultThird)
		{
			BinaryCalculator calc;
			int x = -17, y = -1;
			BinaryNumber a(intToBinary(x)), b(intToBinary(y));
			BinaryNumber mult = a * b;
			Assert::AreEqual(binaryToDecimal(mult.GetValue()), 17);
		}
		TEST_METHOD(DivFirst)
		{
			BinaryCalculator calc;
			int x = -17, y = -1;
			BinaryNumber a(intToBinary(x)), b(intToBinary(y));
			BinaryNumber div = a / b;
			Assert::AreEqual(binaryToDecimal(div.GetValue()), 17);
		}
		TEST_METHOD(DivSecond)
		{
			BinaryCalculator calc;
			int x = 17, y = 17;
			BinaryNumber a(intToBinary(x)), b(intToBinary(y));
			BinaryNumber div = a / b;
			Assert::AreEqual(binaryToDecimal(div.GetValue()), 1);
		}
		TEST_METHOD(DivThird)
		{
			BinaryCalculator calc;
			int x = 18, y = 2;
			BinaryNumber a(intToBinary(x)), b(intToBinary(y));
			BinaryNumber div = a / b;
			Assert::AreEqual(binaryToDecimal(div.GetValue()), 9);
		}
		TEST_METHOD(DivForth)
		{
			BinaryCalculator calc;
			int x = 10, y = 4;
			BinaryNumber a(intToBinary(x)), b(intToBinary(y));
			BinaryNumber div = a / b;
			Assert::AreEqual(binaryToDecimal(div.GetValue()), 2);
		}
		TEST_METHOD(DivFifth)
		{
			BinaryCalculator calc;
			int x = 0, y = 4;
			BinaryNumber a(intToBinary(x)), b(intToBinary(y));
			BinaryNumber div = a / b;
			Assert::AreEqual(binaryToDecimal(div.GetValue()), 0);
		}
		TEST_METHOD(FloatSumFirst)
		{
			std::string outputS = "0 10000000 1010011001100110011001";
			float floatNum1 = 1.1, floatNum2 = 2.2;
			FloatNumber num1F(floatNum1), num2F(floatNum2);
			FloatNumber outputF = num1F + num2F;
			Assert::AreEqual(outputF.printFloatNumber(), outputS);
		}
		TEST_METHOD(FloatSumSecond)
		{
			float floatNum1 = 1.0, floatNum2 = 2.0;
			FloatNumber num1F(floatNum1), num2F(floatNum2);
			FloatNumber outputF = num1F + num2F;
			Assert::AreEqual(outputF.calcInDec(), 3.0f);
		}
	};
}
