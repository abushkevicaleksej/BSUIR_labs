#include "Payment.h"

int Payment:: GetPrice()
{
	return price;
}
void Payment::SetPrice(int newprice)
{
	this->price = newprice;
}