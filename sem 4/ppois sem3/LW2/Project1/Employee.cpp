#include "Employee.h"


Employee::Employee()
{
	this->job_title = "";
}

std::string Employee::GetJobTitle()
{
	return job_title;
}

void Employee::SetJobTitle(const std::string& newjob_title)
{
	this->job_title = newjob_title;
}