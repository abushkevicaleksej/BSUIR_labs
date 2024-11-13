#include "pch.h"
#include "CppUnitTest.h"
#include "../vocabularylib/WordPair.h"
#include "../UnitTest1/Vocabulary.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace Vocabulary_Tests
{
	TEST_CLASS(Vocabulary_Tests)
	{
	public:
		
		TEST_METHOD(Test_Other_Way)
		{
			Vocabulary voc;
			Assert::IsTrue(voc.GetRoot() == nullptr);
		}

		TEST_METHOD(Root_Emptying)
		{
			Vocabulary voc;
			string eng = "hen", rus = "kuritsa";
			voc.Push(eng,rus, voc.InSubTree(eng));
			voc.Empty();
			Assert::IsTrue(voc.GetRoot() == NULL);
		}

		TEST_METHOD(Pushing_Using_Vocabulary)
		{
			Vocabulary voc;
			voc.Push("cat", "kot", voc.InSubTree("cat"));
			voc.Push("dog", "sobaka", voc.InSubTree("dog"));
			voc.Push("cow", "korova", voc.InSubTree("cow"));
			voc.Push("bird", "ptica", voc.InSubTree("bird"));
			voc.Del("bird", "ptica");
			Assert::IsTrue(voc.GetSize() == 3);
		}

		TEST_METHOD(Switcing_Using_Vocabulary)
		{
			Vocabulary voc;
			voc.Push("cat", "kot", voc.InSubTree("cat"));
			voc.Push("dog", "sobaka", voc.InSubTree("dog"));
			voc.Push("cow", "korova", voc.InSubTree("cow"));
			voc.Push("bird", "ptica", voc.InSubTree("bird"));
			voc.SwitchTransl("bird", "vorobei");
			Assert::IsTrue(voc["bird"]=="vorobei");
		}

		TEST_METHOD(Test_Get_Size)
		{
			Vocabulary voc;
			voc.Push("cat", "kot", voc.InSubTree("cat"));
			voc.Push("dog", "sobaka", voc.InSubTree("dog"));
			voc.Push("cow", "korova", voc.InSubTree("cow"));
			voc.Push("bird", "ptica", voc.InSubTree("bird"));
			Assert::IsTrue(voc["cat"] == "kot");
		}

		TEST_METHOD(IsEmpty)
		{
			Vocabulary voc;
			voc.Push("cow", "korova", voc.InSubTree("cow"));
			voc.Push("debugger", "otladchik",voc.InSubTree("debugger"));
			voc.Push("eng", "angl", voc.InSubTree("eng"));
			voc.Push("university", "universitet", voc.InSubTree("university"));
			voc.Push("book", "kNiGA", voc.InSubTree("book"));
			Assert::IsTrue(voc.GetSize() == 5);
		}

		TEST_METHOD(Test_Del)
		{
			Vocabulary voc;
			voc.Push("cow", "korova", voc.InSubTree("cow"));
			voc.Push("chair", "stul", voc.InSubTree("chair"));
			voc.Del("chair", "stul");
			Assert::IsTrue(voc.GetSize() == 1);
		}

		TEST_METHOD(Negative_Test_Change_Translation)
		{
			Vocabulary voc;
			voc.Push("bird", "ptica", voc.InSubTree("bird"));
			voc.Push("fox", "lisa", voc.InSubTree("fox"));
			voc.SwitchTransl("bird", "vorobei");
			voc.SwitchTransl("fox", "rijaya");
			Assert::IsTrue(voc.GetSize() == 2);
		}

		TEST_METHOD(Negative_Test_Pull_File)
		{
			Vocabulary voc;
			voc.ReadFromFile("vocabulary.txt");
			Assert::IsTrue(voc.GetSize() == 3);
		}

		TEST_METHOD(Translation)
		{
			Vocabulary voc;
			voc.Push("oop","ооп", voc.InSubTree("oop"));
			voc.Push("programming", "programmirovanie", voc.InSubTree("programming"));
			voc.SwitchTransl("programming","c++");
			voc.Del("programming", (voc)["programming"]);
			Assert::IsTrue(voc.GetSize() == 1);
		}
	};
}

