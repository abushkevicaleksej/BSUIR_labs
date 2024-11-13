#pragma once
#include <iostream>
#include <string>
#include <bitset>
#include <cstdlib>
#include <ctime>

using namespace std;

class ConstMatrix
{
private:
	static const int row = 16;
	static const int column = 16;
	int matrix[row][column];

public:

	ConstMatrix();

	int getValue(int row, int col);

	void setValue(int row, int col, int newvalue);

	void printMatrix();

	string getWordFromMatrix(int index);

	string getAddressRowWord(int index);

	string f1Function(const string& firstWord, const string& secondWord);

	string f14Function(const string& firstWord, const string& secondWord);

	string f3Function(const string& firstWord, const string& secondWord);

	string f12Function(const string& firstWord, const string& secondWord);

	void setWord(int index, const string& newWord);

	string summAB(const string& key);

	int findWordPosition(const string& searchedWord, bool condition);
};