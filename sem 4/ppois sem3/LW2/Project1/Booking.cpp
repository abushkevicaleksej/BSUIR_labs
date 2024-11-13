#include "Booking.h"
Status Booking::GetStatus()
{
	return status;
}

void Booking:: SetStatus(Status status)
{
	this->status = status;
}