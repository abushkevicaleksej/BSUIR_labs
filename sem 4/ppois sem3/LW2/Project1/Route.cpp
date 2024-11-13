#include "Route.h"

Route::Route()
{
	this->routename = "";
	this->place = "";
	this->time = 0;
	this->price = 0;
	this->about = "";
}

std::string Route::GetRouteName()
{
	return routename;
}

void Route::SetRouteName(const std::string& Routename)
{
	this->routename = Routename;
}

std::string Route::GetPlace()
{
	return place;
}

void Route::SetPlace(const std::string& place)
{
	this->place = place;
}

int Route::GetNumOfTime()
{
	return time;
}

void Route::SetNumOfTime(int days)
{
	this->time = time;
}

int Route::GetPrice()
{
	return price;
}

void Route::SetPrice(int price)
{
	this->price = price;
}

std::string Route::GetInfoAbout()
{
	return about;
}

void Route::SetInfoAbout(const std::string& about)
{
	this->about = about;
}

Date Route::GetDate()
{
	return date;
}

void Route::SetDate(Date newdate)
{
	GetDate() = newdate;
}

void Route::AddReview(const Review& rev)
{
	revs.push_back(rev);
}

void Route::ApplyDiscount()
{
	SetPrice((this->GetPrice()) * 0.5);
}

void Route::DeleteReview(int index)
{
	if (index >= 0 && index < revs.size())
	{
		revs.erase(revs.begin() + index);
	}
}

void Route::EditReview(int index, const Review& newReview)
{
	if (index >= 0 && index < revs.size())
	{
		revs[index] = newReview;
	}
}