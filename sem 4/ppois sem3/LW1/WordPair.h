#pragma once
#include "Direction.h"
#include<iostream>
#include<string>
#include<fstream>

using namespace std;

class WordPair
{
public:
	
	string GetEng();

	string GetRus();

	WordPair* GetLeft();

	WordPair* GetRight();

	void SetLeft(WordPair* left);

	void SetRight(WordPair* right);

	Direction InSubTree(const string& eng);

	WordPair(const string& eng, const string& rus);

	void ReadFromFile(const string& path);

	void SwitchTransl(const string& eng, const string& rus);

	string operator[](const string& eng);

	void Del(const string& eng, const string& rus);

private:
	
	WordPair* FindMinNode();

	WordPair* Finder(const string& eng);

	string eng, rus;

	WordPair* left = NULL, * right = NULL;
};

