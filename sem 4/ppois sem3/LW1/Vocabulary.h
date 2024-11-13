#pragma once
#include "../vocabularylib/Direcrion.h"
#include "../vocabularylib/WordPair.h"
class Vocabulary
{
public:

	Vocabulary();

	~Vocabulary();

	void Empty();

	Direction InSubTree(const string& eng);

	string  operator[](const string& eng);

	int GetSize();

	WordPair* GetRoot();

	void Del(const string& eng, const string& rus);

	void SwitchTransl(const string& eng, const string& rus);

	void ReadFromFile(const string& path);

	void Push(const string& eng, const string& rus, Direction direction);


private:

	WordPair* Push(WordPair* node, const string& eng, const string& rus, Direction direction);

	WordPair* root = NULL;

	int size = 0;

};
