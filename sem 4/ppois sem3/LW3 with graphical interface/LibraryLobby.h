#pragma once
#include "../UnitTest1/BookShelf.h"
class LibraryLobby
{
private:
	string name;
	int numOfPlaces;
	vector<BookShelf> bookShelf;
public:
	LibraryLobby() {}
	
	~LibraryLobby() {}
	
	string GetName();
	
	void SetName(string newName);
	
	int GetNumOfPlaces();
	
	void SetNumOfPlaces(int newNumOfPlaces);
};