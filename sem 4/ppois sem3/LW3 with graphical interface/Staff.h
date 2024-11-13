#pragma once
#include "../UnitTest1/JobTitle.h"
#include "../UnitTest1/Human.h"
class Staff : public Human
{
private:
	JobTitle jobTitle;
	int salary;
	Name staffName;
public:
	Staff() {}
	
	~Staff() {}
	
	int GetSalary();
	
	JobTitle GetJobTitle();
	
	void SetJobTitle(JobTitle job);

	void SetSalaryToStaff(int salary);
};