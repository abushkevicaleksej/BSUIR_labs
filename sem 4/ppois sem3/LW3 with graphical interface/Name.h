#pragma once
#include <string>
using namespace std;
class Name
{
	string surname;
	string name;
	string lastName;
public:
	Name() {}
	
	~Name() {}
	
	string GetSurname();
	
	void SetSurname(const string& newSurname);
	
	string GetName();
	
	void SetName(const string& newName);
	
	string GetLastname();
	
	void SetLastname(const string& newLastName);
};