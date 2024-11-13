#pragma once
#include "Date.h"
int Date::GetDay()
{
	return day;
}
void Date::SetDay(int newDay)
{
	this->day = newDay;
}
int Date::GetMonth()
{
	return month;
}
void Date::SetMonth(int newMonth)
{
	this->month = newMonth;
}
int Date::GetYear()
{
	return year;
}
void Date::SetYear(int newYear)
{
	this->year = newYear;
}