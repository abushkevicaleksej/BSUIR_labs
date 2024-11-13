#pragma once
#include "Staff.h"
int Staff::GetSalary()
{
	return salary;
}
JobTitle Staff::GetJobTitle()
{
	return jobTitle;
}
void Staff::SetJobTitle(JobTitle job)
{
	this->jobTitle = job;
}

void Staff::SetSalaryToStaff(int salary)
{
	if (this->GetJobTitle() == JobTitle::CLEANER)
	{
		this->salary = 1.5 * salary;
	}
	if (this->GetJobTitle() == JobTitle::SECURITY)
	{
		this->salary = 1.75 * salary;
	}
	if (this->GetJobTitle() == JobTitle::LOADER)
	{
		this->salary = 2 * salary;
	}
	if (this->GetJobTitle() == JobTitle::ADMINISTRATOR)
	{
		this->salary = 2.5 * salary;
	}
}