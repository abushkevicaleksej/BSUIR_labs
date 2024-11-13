#pragma once
#include "Human.h"
Name Human::GetName()
{
	return name;
}
string Human::GetSurname()
{
	return name.GetSurname();
}
void Human::SetName(const string& newSurname, const string& newName, const string& newLastName)
{
	name.SetSurname(newSurname);
	name.SetName(newName);
	name.SetLastname(newLastName);
}
int Human::GetAge()
{
	return age;
}
void Human::SetAge(int newAge)
{
	this->age = newAge;
}
Gender Human::GetGender()
{
	return gender;
}
void Human::SetGender(Gender newGender)
{
	this->gender = newGender;
}