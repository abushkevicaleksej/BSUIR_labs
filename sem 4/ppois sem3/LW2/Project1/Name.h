#pragma once
#include <string>
class Name
{
private:
	std::string surname;
	std::string name;
	std::string last_name;
public:

	Name() {}

	~Name() {}

	std::string GetSurname();

	void SetSurname(const std::string& newsurname);

	std::string GetStringSurname();

	std::string GetName();

	void SetName(const std::string& newname);

	std::string GetLastName();

	void SetLastName(const std::string& newlast_name);
};