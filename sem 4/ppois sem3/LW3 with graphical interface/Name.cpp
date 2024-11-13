#pragma once
#include "Name.h"
string Name::GetSurname()
{
	return surname;
}
void Name::SetSurname(const string& newSurname)
{
	this->surname = newSurname;
}
string Name::GetName()
{
	return name;
}
void Name::SetName(const string& newName)
{
	this->name = newName;
}
string Name::GetLastname()
{
	return lastName;
}
void Name::SetLastname(const string& newLastName)
{
	this->lastName = newLastName;
}