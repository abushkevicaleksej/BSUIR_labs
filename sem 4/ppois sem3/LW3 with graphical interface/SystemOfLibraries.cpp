#pragma once
#include "SystemOfLibraries.h"
int SystemOfLibraries::GetNumOfLibs()
{
	return lib.size();
}
void SystemOfLibraries::AddLibToSystem(Library& library)
{
	lib.push_back(library);
}
void SystemOfLibraries::DeleteLibFromSystem(const string& name)
{
	for (auto it = lib.begin(); it != lib.end(); ++it)
	{
		if (it->GetLibName() == name)
		{
			lib.erase(it);
			break;
		}
	}
}