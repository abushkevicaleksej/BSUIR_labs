#pragma once
#include "../UnitTest1/Gender.h"
#include "../UnitTest1/Name.h"
class Human
{
private:
	Name name;
	int age;
	Gender gender;
public:
	Human() {}
	
	virtual ~Human() {}
	
	Name GetName();
	
	string GetSurname();
	
	void SetName(const string& newSurname, const string& newName, const string& newLastName);
	
	int GetAge();
	
	void SetAge(int newAge);
	
	Gender GetGender();
	
	void SetGender(Gender newGender);
};