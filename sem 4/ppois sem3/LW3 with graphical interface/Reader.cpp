#pragma once
#include "Reader.h"
int Reader::GetNumOfBooks()
{
	return book.size();
}
void Reader::AddBook(Book& newBook)
{
	newBook.SetBookStatus(BookStatus::UNAVAILABLE);
	book.push_back(newBook);
}
void Reader::RemoveBook(const string& name)
{
	for (auto it = book.begin(); it != book.end(); ++it)
	{
		if (it->GetBookName() == name)
		{
			book.erase(it);
			break;
		}
	}
}