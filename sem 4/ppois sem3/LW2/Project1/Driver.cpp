#include "Driver.h"

Vehicle Driver:: GetDriversVehicle()
{
	return vehicle;
}

void Driver::SetDriversVehicle(Vehicle vehicle)
{
	this->vehicle = vehicle;
}

void Driver::SetTypeOfDriversVehicle(TypeOfVehicle vehicletype)
{
	this->vehicletype = vehicletype;
}

TypeOfVehicle Driver::GetTypeOfDriversVehicle()
{
	return vehicletype;
}