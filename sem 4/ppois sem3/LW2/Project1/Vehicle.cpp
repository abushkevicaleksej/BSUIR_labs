#include "Vehicle.h"
#include <string>

Vehicle::Vehicle()
{
	model = "";
	place = 0;
}
std::string Vehicle::GetModel()
{
	return model;
}
void Vehicle::SetModel(const std::string& newmodel)
{
	this->model = newmodel;
}

int Vehicle::GetNumOfPlaces()
{
	return place;
}
void Vehicle::SetNumOfPlaces(int newplace)
{
	this->place = newplace;
}

TypeOfVehicle Vehicle::GetTypeOfVehicle()
{
	return type;
}

void Vehicle::SetTypeOfVehicle(TypeOfVehicle type)
{
	this->type = type;
}

void Vehicle::FillThePlace()
{
	this->place--;
}

void Vehicle::FreeThePlace()
{
	this->place++;
}