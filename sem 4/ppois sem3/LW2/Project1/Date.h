#pragma once
class Date
{
private:
	int day;
	int month;
	int year;
public:
	Date() {}

	~Date() {}

	void SetDate(int day, int month, int year);

	int GetNumOfDay();

	void SetNumOfDay(int newday);

	int GetNumOfMonth();

	void SetNumOfMonth(int newmonth);

	int GetNumOfYear();

	void SetNumOfYear(int newyear);
};

