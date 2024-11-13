#pragma once
#include "Booking.h"
#include "Status.h"
#include <vector>
#include <string>
class Consumer : public Person
{
	std::vector<Booking>bookings;

public:
	std::string GetStringSurname();

	void AddOrder(Booking& booking);

	void Pay(Booking& booking);
};