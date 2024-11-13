#pragma once
#include "../UnitTest1/Human.h"
#include "../UnitTest1/Book.h"
#include <vector>
class Reader : public Human
{
private:
	vector<Book>book;
public:
	Reader() {}
	
	~Reader() {}
	
	int GetNumOfBooks();
	
	void AddBook(Book& newBook);
	
	void RemoveBook(const string& name);
};