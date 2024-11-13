#include "Company.h"

std::string Company:: GetCompanyName()
{
	return name;
}

void Company:: SetCompanyName(const std::string& name)
{
	this->name = name;
}

std::string Company:: GetAdress()
{
	return address;
}

void Company::SetAddress(const std::string& address)
{
	this->address = address;
}

void Company::AddRoute(Route tour)
{
	routs.push_back(tour);
} 

void Company:: DeleteRoute(const std::string& name)
{
	for (auto it = routs.begin(); it != routs.end(); ) {
		if (it->GetRouteName() == name) {
			it = routs.erase(it);
		}
		else {
			++it;
		}
	}
}

void Company::ShowRouteList() const {
	for (auto rout : routs) {
		std::cout << rout.GetRouteName() << std::endl;
	}
}

void Company:: AddEmployee(Employee& emp)
{
	employee.push_back(emp);
}

void Company:: DeleteEmployee(const std::string& surname)
{
	for (auto it = employee.begin(); it != employee.end(); ) {
		if (it->GetStringSurname() == surname) {
			it = employee.erase(it);
		}
		else {
			++it;
		}
	}
}

void Company::ShowEmployeeList() const
{
	for (auto emp : employee)
	{
		std::cout << emp.GetStringSurname() << std::endl;
	}
}

void  Company::AddConsumer(Consumer& cons)
{
	consumer.push_back(cons);
}

void Company::DeleteConsumer(const std::string& surname)
{
	for (auto it = consumer.begin(); it != consumer.end(); ) {
		if (it->GetStringSurname() == surname) {
			it = consumer.erase(it);
		}
		else {
			++it;
		}
	}
}

void Company::ShowConsumerList()const
{
	for (auto cons : consumer)
	{
		std::cout << cons.GetStringSurname() << std::endl;
	}
}

void Company::AddDriver(Driver& driv)
{
	driver.push_back(driv);
}

void Company::DeleteDriver(const std::string& surname)
{
	for (auto it = driver.begin(); it != driver.end(); ) {
		if (it->GetStringSurname() == surname) {
			it = driver.erase(it);
		}
		else {
			++it;
		}
	}
}

void  Company::ShowDriverList()const
{
	for (auto driv : driver)
	{
		std::cout << driv.GetStringSurname() << std::endl;
	}
}