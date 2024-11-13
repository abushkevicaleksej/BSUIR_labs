#pragma once
#include <vector>
#include "../UnitTest1/Book.h"
using namespace std;
class BookShelf
{
private:
	string name;
	int numOfBooks;
	vector<Book>books;
public:
	BookShelf() {}
	
	~BookShelf() {}
	
	string GetName();
	
	void SetName(string name);
	
	int GetNumOfBooks();
	
	void SetNumOfBooks(int newBooks);
	
	void AddBooksToShelf(Book& book);
	
	void DeleteBookFromShelf(const string& name);
};