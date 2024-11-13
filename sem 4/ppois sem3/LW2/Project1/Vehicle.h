#pragma once
#include "TypeOfVehicle.h"
class Vehicle 
{
	std::string model;

	int place;

	TypeOfVehicle type;

public:
	Vehicle();

	std::string GetModel();

	void SetModel(const std::string& newmodel);

	int GetNumOfPlaces();

	void SetNumOfPlaces(int newplace);

	TypeOfVehicle GetTypeOfVehicle();

	void SetTypeOfVehicle(TypeOfVehicle type);

	void FillThePlace();

	void FreeThePlace();
};