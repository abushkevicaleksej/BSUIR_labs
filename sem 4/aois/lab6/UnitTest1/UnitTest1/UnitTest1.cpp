#include "pch.h"
#include "CppUnitTest.h"
#include "HashTable.h"
using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1
{
	TEST_CLASS(UnitTest1)
	{
	public:
		
		TEST_METHOD(AddNodeMethod)
		{
			HashTable hash;
			string key = "Cathet", value = "side of stretch-angled triagle";
			hash.insert(key, value);
			hash.insert(key, value);
			Assert::AreEqual(hash.getNumberOfEntries(), 2);
		}

		TEST_METHOD(IsCollisionMethod)
		{
			HashTable hash;
			string key = "Circle", value = "infinite set of points";
			hash.insert(key, value);
			hash.insert(key, value);
			Assert::AreEqual(hash.getCollision(), true);
		}

		TEST_METHOD(DeleteNodeMethod)
		{
			HashTable hash;
			string key = "Oval", value = "Figure constructed from two pairs of arcs, with two different radii";
			hash.insert(key, value);
			hash.insert(key, value);
			hash.remove(key);
			Assert::AreEqual(hash.getNumberOfEntries(), 1);
		}

		TEST_METHOD(GetValueMethod)
		{
			HashTable hash;
			string key = "Cube", value = "Solid three-dimensional figure, which has 6 square faces, 8 vertices and 12 edges";
			hash.insert(key, value);
			Assert::AreEqual(hash.getValueByKey(key), value);
		}

		TEST_METHOD(UpdateDataInHashTable)
		{
			HashTable hash;
			string key = "Square", value = "geometrical figure with 4 stretched angles";
			string newValue = "geometrical figure with 4 similiar sides";
			hash.insert(key, value);
			hash.update(key, newValue);
			Assert::AreEqual(hash.getValueByKey(key), newValue);
		}

		TEST_METHOD(GetInvalidValueMethod)
		{
			HashTable hash;
			string key = "Cube", value = "Solid three-dimensional figure, which has 6 square faces, 8 vertices and 12 edges";
			string newkey = "Triangle", emptyvalue = "";
			hash.insert(key, value);
			Assert::AreEqual(hash.getValueByKey(newkey), emptyvalue);
		}

		TEST_METHOD(UpdateWrongData)
		{
			HashTable hash;
			string key = "Cube", value = "Solid three-dimensional figure, which has 6 square faces, 8 vertices and 12 edges";
			string newkey = "Triangle";
			hash.insert(key, value);
			Assert::AreEqual(hash.getUpdateStatus(), false);
		}

		TEST_METHOD(DeleteWrongData)
		{
			HashTable hash;
			string key = "Cube", value = "Solid three-dimensional figure, which has 6 square faces, 8 vertices and 12 edges";
			string newkey = "Triangle";
			hash.insert(key, value);
			hash.remove(newkey);
			Assert::AreEqual(hash.getNumberOfEntries(), 1);
		}

		TEST_METHOD(DisplayTest)
		{
			HashTable hash;
			string key = "Cube", value = "Solid three-dimensional figure, which has 6 square faces, 8 vertices and 12 edges";
			hash.insert(key, value);
			string expected = "Index: 0, Key: Cube, Definition: Solid three-dimensional figure, which has 6 square faces, 8 vertices and 12 edges\n";
			Assert::AreEqual(hash.display(), expected);
		}
	};
}
