#pragma once
#include "Consumer.h"
#include "Route.h"
class Review
{
private:
	std::string text;
	int rating;
	int index;
public:
	Review();

	~Review() {};

	int GetRating();

	void SetRating(int rating);

	int GetIndex();

	void SetIndex(int index);

	std::string GetText();

	void SetText(const std::string& text);
};