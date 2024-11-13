#pragma once
class Date
{
private:
	int day;
	int month;
	int year;
public:
	Date() {};
	
	~Date() {};
	
	int GetDay();
	
	void SetDay(int newDay);
	
	int GetMonth();
	
	void SetMonth(int newMonth);
	
	int GetYear();
	
	void SetYear(int newYear);
};