#pragma once
#include "../Project1/Library.h"
class SystemOfLibraries
{
private:
	vector<Library>lib;
public:
	SystemOfLibraries() {}
	
	~SystemOfLibraries() {}
	
	int GetNumOfLibs();
	
	void AddLibToSystem(Library& library);
	
	void DeleteLibFromSystem(const string& name);
};