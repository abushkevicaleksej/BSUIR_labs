#pragma once
#include "Name.h"
#include "Contact.h"
#include "Discount.h"
class Person : public Name
{
public:
	Person(){}

	~Person() {}

	Name GetName();

	void SetName(const std::string& newsurname, const std::string& newname, const std::string& newlast_name);

	int GetAge();

	void SetBenefit(Discount discount);

	Discount GetDiscount();

	void SetDiscount(Discount discount);

	void SetAge(int newage);

	void SetInfoAbout(const std::string& surname, const std::string& name, const std::string& last_name);

private:
	Name name;
	Discount discount;
	Contact contact;
	int age;
};