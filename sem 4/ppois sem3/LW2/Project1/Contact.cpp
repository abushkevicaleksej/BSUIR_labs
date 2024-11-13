#include "Contact.h"

std::string Contact:: GetPhoneNumber()
{
	return phone_number;
}

void Contact::SetPhoneNumber(const std::string& new_phone_number)
{
	this->phone_number = new_phone_number;
}

std::string Contact::GetEmail()
{
	return email;
}

void Contact::SetEmail(std::string newemail)
{
	this->email = newemail;
}