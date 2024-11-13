#include "Name.h"


std::string Name::GetSurname()
{
	return surname;
}
void Name::SetSurname(const std::string& newsurname)
{
	this->surname = newsurname;
}

std::string Name::GetStringSurname()
{
	return surname;
}

std::string Name::GetName()
{
	return name;
}
void Name::SetName(const std::string& newname)
{
	this->name = newname;
}

std::string Name::GetLastName()
{
	return last_name;
}
void Name::SetLastName(const std::string& newlast_name)
{
	this->last_name = newlast_name;
}