#pragma once
#include "../Project1/Library.h"

int Library::GetNumOfReaders()
{
	return reader.size();
}
void Library::SetSalaryToStaff(Staff& worker, int salary)
{
	worker.SetSalaryToStaff(salary);
}
void Library::AddWorker(Staff& staff)
{
	worker.push_back(staff);
}
void Library::DeleteWorker(const string& surname)
{
	for (auto it = worker.begin(); it != worker.end(); ++it)
	{
		if (it->GetSurname() == surname)
		{
			worker.erase(it);
			break;
		}
	}
}
string Library::GetLibName()
{
	return name;
}
void Library::SetLibName(const string& newName)
{
	this->name = newName;
}
string Library::GetAddress()
{
	return address;
}
void Library::SetAddress(const string& newAddress)
{
	this->address = newAddress;
}
int Library::GetSpace()
{
	return space;
}
void Library::SetSpace(int newSpace)
{
	this->space = newSpace;
}
TypeOfLibrary Library::GetTypeOfLib()
{
	return type;
}
void Library::SetTypeOfLib(TypeOfLibrary newType)
{
	this->type = newType;
}
void Library::AddReader(Reader& newReader)
{
	reader.push_back(newReader);
}
void Library::DeleteReader(const string& surname)
{
	for (auto it = reader.begin(); it != reader.end(); ++it)
	{
		if (it->GetSurname() == surname)
		{
			reader.erase(it);
			break;
		}
	}
}
void Library::AddBookToBase(Book& newBook)
{
	book.push_back(newBook);
}
void Library::DeleteBookFromBase(const string& name)
{
	for (auto it = book.begin(); it != book.end(); ++it)
	{
		if (it->GetBookName() == name)
		{
			book.erase(it);
			break;
		}
	}
}

int Library::GetNumOfBooks()
{
	return book.size();
}

void Library::AddLobby(LibraryLobby& newLobby)
{
	lobby.push_back(newLobby);
}
void Library::DeleteLobby(const string& name)
{
	for (auto it = lobby.begin(); it != lobby.end(); ++it)
	{
		if (it->GetName() == name)
		{
			lobby.erase(it);
			break;
		}
	}
}

int Library::GetNumOfWorkers()
{
	return worker.size();
}

int Library::GetNumOfLobbies()
{
	return lobby.size();
}