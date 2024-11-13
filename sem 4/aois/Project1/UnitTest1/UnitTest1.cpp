#include "pch.h"
#include "CppUnitTest.h"
#include "../Project1/BinaryNumber.h"
#include "../Project1/FloatNumber.h"
using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1
{
	TEST_CLASS(UnitTest1)
	{
	public:
		
		TEST_METHOD(TestMethod1)
		{
			BinaryCalculator calc;
			int x=4, y=5;
			BinaryNumber a(intToBinary(x)), b(intToBinary(y));
			Assert::AreEqual(binaryToDecimal(a.GetValue()), x);
		}
	};
}
