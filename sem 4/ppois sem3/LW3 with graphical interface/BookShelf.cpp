#pragma once
#include "BookShelf.h"
string BookShelf::GetName()
{
	return name;
}
void BookShelf::SetName(string name)
{
	this->name = name;
}
int BookShelf::GetNumOfBooks()
{
	return books.size();
}
void BookShelf::SetNumOfBooks(int newBooks)
{
	this->numOfBooks = newBooks;
}
void BookShelf::AddBooksToShelf(Book& book)
{
	books.push_back(book);
}
void BookShelf::DeleteBookFromShelf(const string& name)
{
	for (auto it = books.begin(); it != books.end(); ++it)
	{
		if (it->GetBookName() == name)
		{
			books.erase(it);
			break;
		}
	}
}