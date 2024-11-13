#pragma once
#include "Person.h"
#include "Contact.h"
class Employee : public Person, Contact
{
private:
	Name name;
	Contact cont;
	std::string job_title;
public:
	Employee();

	~Employee() {}

	std::string GetJobTitle();

	void SetJobTitle(const std::string& newjob_title);
};