#pragma once
#include "Review.h"
#include "Date.h"
#include "Discount.h"
#include "Consumer.h"
class Route
{
private:
	std::string routename;
	std::string place;
	int time;
	int price;
	std::string about;
	Date date;
	std::vector<Review> revs;
public:
	
	Route();

	~Route(){}

	std::string GetRouteName();

	void SetRouteName(const std::string& Routename);

	std::string GetPlace();

	void SetPlace(const std::string& place);

	int GetNumOfTime();

	void SetNumOfTime(int days);

	int GetPrice();

	void SetPrice(int price);

	std::string GetInfoAbout();

	void SetInfoAbout(const std::string& about);

	Date GetDate();

	void SetDate(Date newdate);

	void AddReview(const Review& rev);

	void ApplyDiscount();

	void DeleteReview(int index);

	void EditReview(int index, const Review& newReview);
};