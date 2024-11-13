#pragma once
#include "Book.h"
int Book::GetNumOfPages()
{
	return numOfPages;
}
void Book::SetNumOfPages(int pages)
{
	this->numOfPages = pages;
}
int Book::GetAgeLimit()
{
	return ageLimit;
}
void Book::SetAgeLimit(int newAge)
{
	this->ageLimit = newAge;
}
int Book::GetWear()
{
	return wear;
}
void Book::SetWear(int newWear)
{
	this->wear = newWear;
}
string Book::GetFactory()
{
	return factory;
}
void Book::SetFactory(string newFactory)
{
	this->factory = newFactory;
}
string Book::GetBookName()
{
	return name;
}
void Book::SetBookName(const string& newName)
{
	this->name = newName;
}
Name Book::GetAuthorsName()
{
	return authorsName;
}
void Book::SetAuthorsName(Name& authorsName, const string& surname, const string& name, const string& lastName)
{
	authorsName.SetSurname(surname);
	authorsName.SetName(name);
	authorsName.SetLastname(lastName);
}
Date Book::GetDateOfPublishing()
{
	return dateOfPublishing;
}
void Book::SetDateOfPublishing(Date& dateOfPublishing, int day, int month, int year)
{
	dateOfPublishing.SetDay(day);
	dateOfPublishing.SetMonth(month);
	dateOfPublishing.SetYear(year);
}
Date Book::GetDateOfAdding()
{
	return dateOfAddingToLib;
}
void Book::SetDateOfAdding(Date& dateOfAddingToLib, int day, int month, int year)
{
	dateOfAddingToLib.SetDay(day);
	dateOfAddingToLib.SetMonth(month);
	dateOfAddingToLib.SetYear(year);
}
Date Book::GetTerm()
{
	return term;
}
void Book::SetTerm(Date& dateOfAddingToLib, int day, int month, int year)
{
	term.SetDay(day);
	term.SetMonth(month);
	term.SetYear(year);
}
BookStatus Book::GetBookStatus()
{
	return status;
}
void Book::SetBookStatus(BookStatus status)
{
	this->status = status;
}