#include "pch.h"
#include "CppUnitTest.h"
#include "TruthTable.h"
using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1
{
	TEST_CLASS(UnitTest2)
	{
	public:

		TEST_METHOD(TestValidIndex)
		{
			string exp = "(A&B)";
			set<char> exp_elem;
			vector<char> result;
			vector<int>index;
			double decimal = 0;
			exp_elem = GetExpInfo(exp);
			result = PrintTable(exp, index);
			decimal = CountIndexNumber(decimal, index);
			Assert::IsTrue(decimal == 1);
		}

		TEST_METHOD(TestValidExpr1)
		{
			string exp = "(A&B";
			Assert::AreEqual(IsValidExpression(exp), 0);
		}

		TEST_METHOD(TestValidExpr2)
		{
			string exp = "";
			Assert::AreEqual(IsValidExpression(exp), 0);
		}

		TEST_METHOD(TestValidExpr3)
		{
			string exp = "a&B";
			Assert::AreEqual(IsValidExpression(exp), 0);
		}

		TEST_METHOD(TestCountIndexNumber)
		{
			vector<int> index = { 1, 0, 1 }; 
			double decimal = 0;
			double result = CountIndexNumber(decimal, index);
			Assert::AreEqual(result, 5.0); 
		}

		TEST_METHOD(TestIsValidExpression_InvalidEnd)
		{
			string exp = "(A&B)&";
			int result = IsValidExpression(exp);
			Assert::AreEqual(result, 0); 
		}

		TEST_METHOD(TestIsValidExpression_InvalidCharacters)
		{
			string exp = "(A&B)+";
			int result = IsValidExpression(exp);
			Assert::AreEqual(result, 0); 
		}

		TEST_METHOD(TestInfixToSuffix_Conversion)
		{
			string infix = "(A&B)";
			string expectedSuffix = "AB&";
			string actualSuffix = InfixToSuffix(infix);
			Assert::AreEqual(expectedSuffix, actualSuffix); 
		}

		TEST_METHOD(EmptyExpression)
		{
			string exp = "";
			int result = IsValidExpression(exp);
			Assert::AreEqual(result, 0);
		}

		TEST_METHOD(InvalidCharacters)
		{
			string exp = "(A&B)+";
			int result = IsValidExpression(exp);
			Assert::AreEqual(result, 0); 
		}

		TEST_METHOD(ValidBeginning)
		{
			string exp = "(A&B)";
			int result = IsValidExpression(exp);
			Assert::AreEqual(result, 1); 
		}

		TEST_METHOD(InvalidBeginning)
		{
			string exp = "&(A&B)";
			int result = IsValidExpression(exp);
			Assert::AreEqual(result, 0); 
		}

		TEST_METHOD(ValidEnd)
		{
			string exp = "(A&B)";
			int result = IsValidExpression(exp);
			Assert::AreEqual(result, 1); 
		}

		TEST_METHOD(InvalidEnd)
		{
			string exp = "(A&B)&";
			int result = IsValidExpression(exp);
			Assert::AreEqual(result, 0); 
		}

		TEST_METHOD(UnmatchedParentheses)
		{
			string exp = "(A&B))";
			int result = IsValidExpression(exp);
			Assert::AreEqual(result, 0); 
		}

		TEST_METHOD(InvalidCharactersInMeta)
		{
			string exp = "(a&B)";
			int result = IsValidExpression(exp);
			Assert::AreEqual(result, 0); 
		}

		TEST_METHOD(ContradictionResult)
		{
			vector<char> result = { 0, 0, 0 };
			set<char> exp_elem = { 'A', 'B', 'C' };
			stringstream ss;
			streambuf* oldCout = cout.rdbuf();
			cout.rdbuf(ss.rdbuf());
			PrintDnf(result, exp_elem);
			cout.rdbuf(oldCout);
			Assert::AreEqual(ss.str().c_str(), ""); 
		}

		TEST_METHOD(ValidResult)
		{
			vector<char> result = { 1, 0, 1 };
			set<char> exp_elem = { 'A', 'B', 'C' };
			stringstream ss;
			streambuf* oldCout = cout.rdbuf();
			cout.rdbuf(ss.rdbuf());
			PrintDnf(result, exp_elem);
			cout.rdbuf(oldCout);
			Assert::AreEqual(ss.str().c_str(), "DNF\nM (0, 2)\n( !A &  !B &  !C) | ( !A & B &  !C)\n");
		}

		TEST_METHOD(EmptyExpElem)
		{
			vector<char> result = { 1, 0, 1 };
			set<char> exp_elem;
			stringstream ss;
			streambuf* oldCout = cout.rdbuf();
			cout.rdbuf(ss.rdbuf());
			PrintDnf(result, exp_elem);
			cout.rdbuf(oldCout);
			Assert::AreEqual(ss.str().c_str(), "DNF\nM (0, 2)\n() | ()\n");
		}

		TEST_METHOD(InvalidRightSideCharacter)
		{
			string exp = "(A&B!";
			int result = IsValidExpression(exp);
			Assert::AreEqual(result, 0); 
		}

		TEST_METHOD(OperatorStackNotEmpty)
		{
			string exp = "(A&B)";
			string equal = "AB&";
			string suffix = InfixToSuffix(exp);
			Assert::AreEqual(suffix, equal);
		}

		TEST_METHOD(CnfWithTautologyResult)
		{
			vector<char> result = { 1, 1, 1 }; 
			set<char> exp_elem = { 'A', 'B', 'C' };
			stringstream ss;
			streambuf* old_buf = cout.rdbuf(); 
			cout.rdbuf(ss.rdbuf()); 
			PrintCnf(result, exp_elem); 
			cout.rdbuf(old_buf); 
			Assert::IsTrue(ss.str().empty());
		}

		TEST_METHOD(CnfWithNonTautologyResult)
		{
			vector<char> result = { 0, 1, 0 };
			set<char> exp_elem = { 'A', 'B', 'C' };
			stringstream ss;
			streambuf* old_buf = cout.rdbuf(); 
			cout.rdbuf(ss.rdbuf()); 
			PrintCnf(result, exp_elem); 
			cout.rdbuf(old_buf); 
			string expectedOutput = "CNF\nM (0, 2)\n(A | B | C) & (A | !B | C)\n";
			Assert::AreEqual(ss.str(), expectedOutput);
		}
	};
}
