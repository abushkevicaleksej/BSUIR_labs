#include "ConstMatrix.h"

int main()
{
	ConstMatrix matr;
	matr.printMatrix();
	int index = 4;
	cout << "Word index:" << index << "  :  " << matr.getWordFromMatrix(index) << endl;
	cout << "Address row word:" << index << "   :   " << matr.getAddressRowWord(index) << endl;
	string firstWord = matr.getWordFromMatrix(4);
	cout << firstWord << endl;
	string secondWord = matr.getWordFromMatrix(5);
	cout << secondWord << endl;
	string resultWord = matr.f1Function(firstWord, secondWord);
	cout << "Result F1: " << resultWord << endl;
	string resultF3 = matr.f3Function(firstWord, secondWord);
	cout << "Result F3: " << resultF3 << endl;
	string resultF12 = matr.f12Function(firstWord, secondWord);
	cout << "Result F12: " << resultF12 << endl;
	string resultF14 = matr.f14Function(firstWord, secondWord);
	cout << "Result F14: " << resultF14 << endl;
	




	string keyV = "111";
	string SumResult = matr.summAB(keyV);
	matr.printMatrix();


	cout << matr.findWordPosition(firstWord, true);
	matr.printMatrix();


	return 0;
}