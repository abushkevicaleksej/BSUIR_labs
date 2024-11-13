#include "Date.h"

void Date:: SetDate(int day, int month, int year)
{
	SetNumOfDay(day);
	SetNumOfMonth(month);
	SetNumOfYear(year);
}

int Date::GetNumOfDay()
{
	return day;
}
void Date::SetNumOfDay(int newday)
{
	if (newday < 1 || newday > 31) {
		throw std::invalid_argument("Invalid num of day!");
	}
	this->day = newday;
}
int Date::GetNumOfMonth()
{
	return month;
}
void Date::SetNumOfMonth(int newmonth)
{
	if (newmonth < 1 || newmonth > 12) {
		throw std::invalid_argument("Invalid num of month!");
	}
	this->month = newmonth;
}
int Date::GetNumOfYear()
{
	return year;
}
void Date::SetNumOfYear(int newyear)
{
	if (newyear < 0) {
		throw std::invalid_argument("Invalid num of year!");
	}
	this->year = newyear;
}