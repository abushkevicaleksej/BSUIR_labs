#include "pch.h"
#include "CppUnitTest.h"
#include "ConstMatrix.h"
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

		TEST_METHOD(TestGetAddressRowWord)
		{
			ConstMatrix matrix;
			string word = matrix.getAddressRowWord(0);
			Assert::AreEqual(string("1001111000001000"), word);
		}

		TEST_METHOD(TestSetWord)
		{
			ConstMatrix matrix;
			string newWord = "1010101010101010";
			matrix.setWord(0, newWord);
			string word = matrix.getWordFromMatrix(0);
			Assert::AreEqual(newWord, word);
		}

		TEST_METHOD(TestSummAB)
		{
			ConstMatrix matrix;
			string key = "100";
			string result = matrix.summAB(key);
			Assert::AreEqual(string("1000110001101001"), result);
		}

		TEST_METHOD(TestF14Function)
		{
			ConstMatrix matrix;
			string firstWord = "1010";
			string secondWord = "1100";
			string result = matrix.f14Function(firstWord, secondWord);
			Assert::AreEqual(string("0111"), result);
		}

		TEST_METHOD(TestF12Function)
		{
			ConstMatrix matrix;
			string firstWord = "1010";
			string secondWord = "1100";
			string result = matrix.f12Function(firstWord, secondWord);
			Assert::AreEqual(string("0101"), result);
		}
	};
}
