#include "Person.h"

Name Person::GetName()
{
	return name;
}

void Person::SetName(const std::string& newsurname, const std::string& newname, const std::string& newlast_name)
{
	name.SetSurname(newsurname);
	name.SetName(newname);
	name.SetLastName(newlast_name);
}
int Person::GetAge()
{
	return age;
}

void Person::SetBenefit(Discount discount)
{
	this->discount = discount;
}

Discount Person::GetDiscount()
{
	return discount;
}

void Person::SetDiscount(Discount discount)
{
	this->discount = discount;
}

void Person::SetAge(int newage)
{
	if (newage < 1 || newage > 100) {
		throw std::invalid_argument("Invalid num of age!");
	}
	if (newage <= 7)
	{
		this->discount = Discount::CHILD_UNDER_7;
	}
	this->age = newage;
}

void Person::SetInfoAbout(const std::string& surname, const std::string& name, const std::string& last_name)
{
	SetName(surname, name, last_name);
}