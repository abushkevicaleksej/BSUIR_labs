#pragma once
#include "TypeOfVehicle.h"
#include "Vehicle.h"
class Driver : public Person, public Contact
{
private:
	Vehicle vehicle;
	TypeOfVehicle vehicletype;
public:
	Driver() {}

	~Driver() {}

	Vehicle GetDriversVehicle();

	void SetDriversVehicle(Vehicle vehicle);

	void SetTypeOfDriversVehicle(TypeOfVehicle vehicletype);

	TypeOfVehicle GetTypeOfDriversVehicle();
};