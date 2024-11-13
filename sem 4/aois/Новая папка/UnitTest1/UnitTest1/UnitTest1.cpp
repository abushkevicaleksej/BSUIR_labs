#include "pch.h"
#include "CppUnitTest.h"
#include "Minimization.h"
using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1
{
	TEST_CLASS(MinimizationTests)
	{
	public:
		
		TEST_METHOD(IsValidCNF)
		{
			string expression = "(!(A&(!B))>C)";
			set<char> expression_elem;
			vector<char> result;
			expression_elem = GetExpressionInfo(expression);
			vector<int>index;
			result = PrintTable(expression, index);

			string CNF = PrintCnf(result, expression_elem);

			string finalCNF = "(A | B | C) & (A | !B | C) & (!A | !B | C)";
			Assert::AreEqual(CNF, finalCNF);
		}

		TEST_METHOD(IsValidDNF)
		{
			string expression = "(!(A&(!B))>C)";
			set<char> expression_elem;
			vector<char> result;
			expression_elem = GetExpressionInfo(expression);
			vector<int>index;
			result = PrintTable(expression, index);

			string DNF = PrintDnf(result, expression_elem);

			string finalDNF = "(!A & !B & C) | (!A & B & C) | (A & !B & !C) | (A & !B & C) | (A & B & C)";
			Assert::AreEqual(DNF, finalDNF);
		}

		TEST_METHOD(MinimizeCNF)
		{
			string expression = "(!(A&(!B))>C)";
			set<char> expression_elem;
			vector<char> result;
			expression_elem = GetExpressionInfo(expression);
			vector<int>index;
			result = PrintTable(expression, index);

			string CNF = PrintCnf(result, expression_elem);
			CNF = minimizeCnf(CNF);
			string finalCNF = "(A|C) & (!B|C)";
			Assert::AreEqual(CNF, finalCNF);
		}

		TEST_METHOD(MinimizeDNF)
		{
			string expression = "(!(A&(!B))>C)";
			set<char> expression_elem;
			vector<char> result;
			expression_elem = GetExpressionInfo(expression);
			vector<int>index;
			result = PrintTable(expression, index);

			string DNF = PrintDnf(result, expression_elem);
			DNF = minimizeDnf(DNF);
			string finalDNF = "(C) | (A&!B)";
			Assert::AreEqual(DNF, finalDNF);
		}

		TEST_METHOD(MinimizeKarnaughCNF)
		{
			string expression = "(!(A&(!B))>C)";
			set<char> expression_elem;
			vector<char> result;
			expression_elem = GetExpressionInfo(expression);
			vector<int>index;
			result = PrintTable(expression, index);

			string CNF = PrintCnf(result, expression_elem);
			CNF = minimizeSKNFbyKarnaugh(CNF, index);
			string finalCNF = "(A|C) & (!B|C)";
			Assert::AreEqual(CNF, finalCNF);
		}

		TEST_METHOD(MinimizeKarnaughDNF)
		{
			string expression = "(!(A&(!B))>C)";
			set<char> expression_elem;
			vector<char> result;
			expression_elem = GetExpressionInfo(expression);
			vector<int>index;
			result = PrintTable(expression, index);

			string DNF = PrintDnf(result, expression_elem);
			DNF = minimizeSDNFbyKarnaugh(DNF, index);
			string finalDNF = "(C) | (A&!B)";
			Assert::AreEqual(DNF, finalDNF);
		}

		TEST_METHOD(TableCNF)
		{
			string expression = "(!(A&(!B))>C)";
			set<char> expression_elem;
			vector<char> result;
			expression_elem = GetExpressionInfo(expression);
			vector<int>index;
			result = PrintTable(expression, index);

			string origCNF = PrintCnf(result, expression_elem);
			string CNF = PrintCnf(result, expression_elem);
			CNF = minimizeCnf(CNF);
			minimizeCnfTable(CNF, origCNF);

			string finalCNF = "(A|C) & (!B|C)";
			Assert::AreEqual(CNF, finalCNF);
		}

		TEST_METHOD(TableDNF)
		{
			string expression = "(!(A&(!B))>C)";
			set<char> expression_elem;
			vector<char> result;
			expression_elem = GetExpressionInfo(expression);
			vector<int>index;
			result = PrintTable(expression, index);

			string origDNF = PrintDnf(result, expression_elem);
			string DNF = PrintDnf(result, expression_elem);
			DNF = minimizeDnf(DNF);
			minimizeDnfTable(DNF, origDNF);

			string finalDNF = "(C) | (A&!B)";
			Assert::AreEqual(DNF, finalDNF);
		}

		TEST_METHOD(IsValid)
		{
			string expression = "(!(A&(!B))>C)";
			Assert::AreEqual(IsValidExpression(expression), 1);
		}

		TEST_METHOD(IsNotValid)
		{
			string expression = "";
			Assert::AreEqual(IsValidExpression(expression), 0);
		}
	};
}
