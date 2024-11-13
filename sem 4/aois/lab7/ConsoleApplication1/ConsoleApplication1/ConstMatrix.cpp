#include "ConstMatrix.h"

ConstMatrix::ConstMatrix()
{
	int predefinedMatrix[16][16] = {
		{1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0},
		{0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0},
		{1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0},
		{1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0},
		{0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1},
		{1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1},
		{0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0},
		{0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0},
		{0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1},
		{0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1},
		{0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1},
		{1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0},
		{0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0},
		{1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1},
		{1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1},
		{0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0}
	};

	for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < column; j++)
		{
			matrix[i][j] = predefinedMatrix[i][j];
		}
	}
}


int ConstMatrix::getValue(int row, int col)
{
	return matrix[row][col];
}

void ConstMatrix::setValue(int row, int col, int newvalue)
{
	matrix[row][col] = newvalue;
}

void ConstMatrix::printMatrix()
{
	for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < column; j++)
		{
			cout << matrix[i][j] << " ";
		}
		cout << endl;
	}
}

string ConstMatrix::getWordFromMatrix(int index)
{
	string word;
	for (int i = 0; i < column; i++) 
	{
		int x = (index + i) % column;
		word += to_string(matrix[x][index]);
	}
	return word;
}

string ConstMatrix::getAddressRowWord(int index) {
	string row;
	for (int i = 0; i < column; i++) 
	{
		int rowIndex = (index + i) % column;
		row += to_string(matrix[rowIndex][i]);
	}
	return row;
}

void ConstMatrix::setWord(int index, const string& newWord)
{
	for (int i = 0; i < 16; i++)
	{
		int value = newWord[i] - '0';
		matrix[i][index] = value;
	}
}


int ConstMatrix::findWordPosition(const string& searchedWord, bool condition)
{
	int searchedNum = stoi(searchedWord, nullptr, 2);

	int minNum = INT_MAX;
	int maxNum = INT_MIN;
	int minIndex = -1;
	int maxIndex = -1;

	bool g = false; 
	bool l = false;

	for (int i = 0; i < row; i++)
	{
		string word = getWordFromMatrix(i);
		int wordNum = stoi(word, nullptr, 2);

		if (condition && wordNum > searchedNum)
		{
			if (wordNum < minNum)
			{
				minNum = wordNum;
				minIndex = i;
				g = true; 
			}
		}
		else if (!condition && wordNum < searchedNum)
		{
			if (wordNum > maxNum)
			{
				maxNum = wordNum;
				maxIndex = i;
				l = true;
			}
		}
	}

	if (g && minIndex != -1)
	{
		return minIndex;
	}
	else if (l && maxIndex != -1)
	{
		return maxIndex;
	}

	return -1;
}


std::string ConstMatrix::f1Function(const string& firstWord, const string& secondWord)
{
	std::string result = "";
	for (int i = 0; i < firstWord.size(); i++)
	{
		if (firstWord[i] == '1' && secondWord[i] == '1')
		{
			result += '1';
		}
		else
		{
			result += '0';
		}
	}
	return result;
}

std::string ConstMatrix::f14Function(const string& firstWord, const string& secondWord)
{
	std::string result = "";
	for (int i = 0; i < firstWord.size(); i++)
	{
		if (firstWord[i] == '1' && secondWord[i] == '1')
		{
			result += '0';
		}
		else
		{
			result += '1';
		}
	}
	return result;
}

std::string ConstMatrix::f3Function(const string& firstWord, const string& secondWord)
{
	return firstWord;
}

std::string ConstMatrix::f12Function(const string& firstWord, const string& secondWord)
{
	std::string result = "";
	for (int i = 0; i < firstWord.size(); i++)
	{
		if (firstWord[i] == '1')
		{
			result += '0';
		}
		else
		{
			result += '1';
		}
	}
	return result;
}

string ConstMatrix::summAB(const string& key)
{
	string result = "";
	int index = 0;
	for (int i = 0; i < row; i++)
	{
		string word = getWordFromMatrix(i);
		if (word.substr(0, 3) == key)
		{
			result += word + " ";
			index = i;
		}
	}
	if (result.size() > 16) 
	{
		result = result.substr(0, 16); 
	}

	string V = result.substr(0, 3);
	string A = result.substr(3, 4);
	string B = result.substr(7, 4);
	string S = result.substr(11, 5);

	int numA = stoi(A, nullptr, 2);
	int numB = stoi(B, nullptr, 2);

	int sum = numA + numB;

	bitset<5> binarySum(sum); 
	S = binarySum.to_string();
	result = V + A + B + S;
	setWord(index, result);
	return result;
}
