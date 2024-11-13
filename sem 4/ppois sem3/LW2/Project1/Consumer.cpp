#include "Consumer.h"


std::string Consumer:: GetStringSurname()
{
	return GetStringSurname();
}

void Consumer::AddOrder(Booking& booking)
{
	bookings.push_back(booking);
}

void Consumer::Pay(Booking& booking)
{
	booking.SetStatus(Status::CONFIRMED);
}