#include <string>
#include <vector>
#include <iostream>
#include "Employee.h"
#include "Consumer.h"
#include "Driver.h"
#include "Route.h"
#pragma once

class Company
{
public:

	Company(const std::string& name)
	{
		this->name = name;
	}

	~Company() {}

	std::string GetCompanyName();

	void SetCompanyName(const std::string& name);

	std::string GetAdress();

	void SetAddress(const std::string& address);

	void AddRoute(Route tour);

	void DeleteRoute(const std::string& name);

	void ShowRouteList() const;

	void AddEmployee(Employee& emp);

	void DeleteEmployee(const std::string& surname);

	void ShowEmployeeList() const;

	void AddConsumer(Consumer& cons);

	void DeleteConsumer(const std::string& surname);

	void ShowConsumerList()const;

	void AddDriver(Driver& driv);

	void DeleteDriver(const std::string& surname);

	void ShowDriverList()const;

private:
	std::string name;
	Contact contact;
	std::string address;
	std::vector<Route> routs;
	std::vector<Employee> employee;
	std::vector<Consumer> consumer;
	std::vector<Driver> driver;
};