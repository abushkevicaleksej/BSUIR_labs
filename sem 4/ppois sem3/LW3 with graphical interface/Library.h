#pragma once
#include <string>
#include <iostream>
#include <vector>
#include "../UnitTest1/Staff.h"
#include "../UnitTest1/Reader.h"
#include "../UnitTest1/Book.h"
#include "../UnitTest1/LibraryLobby.h"
#include "../Project1/TypeOfLibrary.h"
using namespace std;

class Library
{
private:
	vector<Staff>worker;
	vector<Reader> reader;
	vector<Book>book;
	vector<LibraryLobby>lobby;
	string name;
	string address;
	int space;
	TypeOfLibrary type;
public:
	Library() {}
	~Library() {}

	int GetNumOfReaders();

	void SetSalaryToStaff(Staff& worker, int salary);

	void AddWorker(Staff& staff);

	void DeleteWorker(const string& surname);

	string GetLibName();

	void SetLibName(const string& newName);

	string GetAddress();

	void SetAddress(const string& newAddress);

	int GetSpace();

	void SetSpace(int newSpace);

	TypeOfLibrary GetTypeOfLib();

	void SetTypeOfLib(TypeOfLibrary newType);

	void AddReader(Reader& newReader);

	void DeleteReader(const string& surname);

	void AddBookToBase(Book& newBook);

	void DeleteBookFromBase(const string& name);

	int GetNumOfBooks();

	void AddLobby(LibraryLobby& newLobby);

	void DeleteLobby(const string& name);

	int GetNumOfWorkers();

	int GetNumOfLobbies();
};

