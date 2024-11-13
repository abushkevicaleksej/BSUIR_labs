#pragma once
#include "../UnitTest1/BookStatus.h"
#include "../UnitTest1/Date.h"
#include "../UnitTest1/Name.h"
class Book
{
	int numOfPages;
	int ageLimit;
	int wear;
	string factory;
	string genre;
	string name;
	Name authorsName;
	Date dateOfPublishing;
	Date dateOfAddingToLib;
	Date term;
	BookStatus status;

public:
	Book() {}
	~Book() {}

	int GetNumOfPages();

	void SetNumOfPages(int pages);

	int GetAgeLimit();
	
	void SetAgeLimit(int newAge);
	
	int GetWear();
	
	void SetWear(int newWear);
	
	string GetFactory();
	
	void SetFactory(string newFactory);
	
	string GetBookName();
	
	void SetBookName(const string& newName);
	
	Name GetAuthorsName();
	
	void SetAuthorsName(Name& authorsName, const string& surname, const string& name, const string& lastName);
	
	Date GetDateOfPublishing();
	
	void SetDateOfPublishing(Date& dateOfPublishing, int day, int month, int year);
	
	Date GetDateOfAdding();
	
	void SetDateOfAdding(Date& dateOfAddingToLib, int day, int month, int year);
	
	Date GetTerm();
	
	void SetTerm(Date& dateOfAddingToLib, int day, int month, int year);
	
	BookStatus GetBookStatus();
	
	void SetBookStatus(BookStatus status);
};