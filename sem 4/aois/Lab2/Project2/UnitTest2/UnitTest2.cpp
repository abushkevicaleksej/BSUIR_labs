#include "pch.h"
#include "CppUnitTest.h"
#include "../Project2/TruthTable.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest2
{
	TEST_CLASS(UnitTest2)
	{
	public:
		
		TEST_METHOD(TestMethod1)
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
	};
}
