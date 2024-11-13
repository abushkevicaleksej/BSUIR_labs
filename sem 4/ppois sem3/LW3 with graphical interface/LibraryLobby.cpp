#pragma once
#include "LibraryLobby.h"

string LibraryLobby::GetName()
{
	return name;
}
void LibraryLobby::SetName(string newName)
{
	this->name = newName;
}
int LibraryLobby::GetNumOfPlaces()
{
	return numOfPlaces;
}
void LibraryLobby::SetNumOfPlaces(int newNumOfPlaces)
{
	this->numOfPlaces = newNumOfPlaces;
}