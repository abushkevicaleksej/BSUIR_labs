#include "Review.h"

Review::Review()
{
	this->text = "";
	this->rating = 0;
	this->index = 0;
}

int Review:: GetRating()
{
	return rating;
}

void Review::SetRating(int rating)
{
	this->rating = rating;
}

int Review::GetIndex()
{
	return index;
}

void Review::SetIndex(int index)
{
	this->index = index;
}

std::string Review::GetText()
{
	return text;
}

void Review::SetText(const std::string & text)
{
	this->text = text;
}