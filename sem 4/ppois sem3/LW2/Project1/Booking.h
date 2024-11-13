#pragma once
#include "Consumer.h"
#include "Route.h"
#include "Date.h"
#include "Status.h"
class Booking
{
	std::string info;
	Status status = Status::EXPECTATION;
public:
	Booking() {}
	
	~Booking() {}

	Status GetStatus();

	void SetStatus(Status status);

};