#pragma once
#include <string>
class Contact
{
private:
	std::string phone_number;

	std::string email;
public:
	
	Contact() {}

	~Contact() {}

	std::string GetPhoneNumber();

	void SetPhoneNumber(const std::string& new_phone_number);

	std::string GetEmail();

	void SetEmail(std::string newemail);
};