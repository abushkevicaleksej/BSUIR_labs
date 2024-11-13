#include "pch.h"
#include "CppUnitTest.h"
#include "../ConsoleApplication1/ConstMatrix.h"
using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1
{
	TEST_CLASS(UnitTest1)
	{
	public:
		
		TEST_METHOD(TestGetValue)
		{
			ConstMatrix matrix;
			Assert::AreEqual(1, matrix.getValue(0, 0));
			Assert::AreEqual(0, matrix.getValue(1, 0));
		}

		TEST_METHOD(TestSetValue)
		{
			ConstMatrix matrix;
			matrix.setValue(0, 0, 0);
			Assert::AreEqual(0, matrix.getValue(0, 0));
		}

		TEST_METHOD(TestFindWordPosition)
		{
			ConstMatrix matrix;
			string word = "00010000";
			int position = matrix.findWordPosition(word, true);
			Assert::AreNotEqual(-1, position);
		}

		TEST_METHOD(TestF1Function)
		{
			ConstMatrix matrix;
			string firstWord = "1010";
			string secondWord = "1100";
			string result = matrix.f1Function(firstWord, secondWord);
			Assert::AreEqual(string("1000"), result);
		}
	};
}
