#pragma once
#include "Consumer.h"
#include "Date.h"
#include "Booking.h"
class Payment
{
private:
	Consumer cons_info;
	int price;
	Date date;
public:
	int GetPrice();

	void SetPrice(int newprice);
};