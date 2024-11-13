#include "pch.h"
#include "CppUnitTest.h"
#include "../UnitTest1/SystemOfLibraries.h"
using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1
{
	TEST_CLASS(UnitTest1)
	{
	public:
		
		TEST_METHOD(AddLibToSystem)
		{
			SystemOfLibraries firstlib;
			Library library;
			firstlib.AddLibToSystem(library);
			Assert::AreEqual(firstlib.GetNumOfLibs(), 1);
		}

		TEST_METHOD(AddBookToBase)
		{
			Library mylib;
			Book book;
			Name authors_name;
			Date first_date;
			Date second_date;
			book.SetBookName("Harry Potter and the Chamber of Secrets");
			book.SetAgeLimit(6);
			book.SetAuthorsName(authors_name,"Rowling","Joanne", "Kathleen");
			book.SetDateOfPublishing(first_date, 2, 7, 1998);
			book.SetDateOfAdding(second_date, 20, 10, 2005);
			book.SetFactory("London Books ltd.");
			book.SetNumOfPages(251);
			book.SetWear(0);
			mylib.AddBookToBase(book);
			Assert::AreEqual(mylib.GetNumOfBooks(),1);
		}

		TEST_METHOD(AddWorkerToSystem)
		{
			SystemOfLibraries mainlib;
			Library high_lib;
			Library child_lib;
			mainlib.AddLibToSystem(high_lib);
			mainlib.AddLibToSystem(child_lib);

			Staff first_worker;
			Staff second_worker;

			first_worker.SetName("Ivanov", "Ivan", "Ivanovich");
			first_worker.SetAge(34);
			first_worker.SetJobTitle(JobTitle::LOADER);
			first_worker.SetSalaryToStaff(500);

			second_worker.SetName("Borisov", "Aleksey", "Petrovich");
			second_worker.SetAge(55);
			second_worker.SetJobTitle(JobTitle::ADMINISTRATOR);
			second_worker.SetSalaryToStaff(800);

			high_lib.AddWorker(first_worker);
			child_lib.AddWorker(second_worker);

			Assert::IsTrue(first_worker.GetSalary()<second_worker.GetSalary());
		}

		TEST_METHOD(AddReaderToSystem)
		{
			Library mylib;
			Book book;
			Name authors_name;
			Date first_date;
			Date second_date;
			Reader reader;
			reader.SetName("Abushkevich", "Aleksey", "Aleksandrovich");
			reader.SetAge(19);
			reader.SetGender(Gender::MALE);
			

			book.SetBookName("Harry Potter and the Chamber of Secrets");
			book.SetAgeLimit(6);
			book.SetAuthorsName(authors_name, "Rowling", "Joanne", "Kathleen");
			book.SetDateOfPublishing(first_date, 2, 7, 1998);
			book.SetDateOfAdding(second_date, 20, 10, 2005);
			book.SetFactory("London Books ltd.");
			book.SetNumOfPages(251);
			book.SetWear(0);

			
			mylib.AddBookToBase(book);
			reader.AddBook(book);
			mylib.AddReader(reader);

			Assert::AreEqual(mylib.GetNumOfReaders(), 1);
		
		}

		TEST_METHOD(AddLibToSystemAndDeleteIt)
		{
			SystemOfLibraries firstlib;
			Library library;
			library.SetLibName("VitebskLib1");
			firstlib.AddLibToSystem(library);
			firstlib.DeleteLibFromSystem("VitebskLib1");
			Assert::AreEqual(firstlib.GetNumOfLibs(), 0);
		}

		TEST_METHOD(AddFullEmployeeToSystem)
		{
			SystemOfLibraries mainSystem;
			Library highLib;
			highLib.SetLibName("Minsk Library");
			highLib.SetAddress("Nezavisimosty pr-t");
			highLib.SetSpace(10);
			
			mainSystem.AddLibToSystem(highLib);

			Staff firstWorker;
			Staff secondWorker;
			Staff thirdWorker;
			Staff forthWorker;

			firstWorker.SetName("Ivanov", "Ivan", "Ivanovich");
			firstWorker.SetAge(34);
			firstWorker.SetJobTitle(JobTitle::LOADER);
			firstWorker.SetSalaryToStaff(500);

			secondWorker.SetName("Borisov", "Aleksey", "Petrovich");
			secondWorker.SetAge(55);
			secondWorker.SetJobTitle(JobTitle::ADMINISTRATOR);
			secondWorker.SetSalaryToStaff(800);

			thirdWorker.SetName("Borisenko", "Aleksandr", "Pavlovich");
			thirdWorker.SetAge(41);
			thirdWorker.SetJobTitle(JobTitle::SECURITY);
			thirdWorker.SetSalaryToStaff(400);

			forthWorker.SetName("Viktorova", "Lidiya", "Semenovna");
			forthWorker.SetAge(54);
			forthWorker.SetJobTitle(JobTitle::CLEANER);
			forthWorker.SetSalaryToStaff(550);

			highLib.AddWorker(firstWorker);
			highLib.AddWorker(secondWorker);
			highLib.AddWorker(thirdWorker);
			highLib.AddWorker(forthWorker);

			Assert::AreEqual(highLib.GetNumOfWorkers(), 4);
		}

		TEST_METHOD(AddBookToBookShelf)
		{
			BookShelf firstShelf;
			firstShelf.SetName("A1");
			firstShelf.SetNumOfBooks(40);

			Name authorsName;
			Date firstDate;
			Date secondDate;
			Date thirdDate;


			Book book;
			book.SetBookName("Harry Potter and the Chamber of Secrets");
			book.SetAgeLimit(6);
			book.SetAuthorsName(authorsName, "Rowling", "Joanne", "Kathleen");
			book.SetDateOfPublishing(firstDate, 2, 7, 1998);
			book.SetDateOfAdding(secondDate, 20, 10, 2005);
			book.SetTerm(thirdDate, 23, 10, 2023);
			book.SetFactory("London Books ltd.");
			book.SetNumOfPages(251);
			book.SetWear(0);

			firstShelf.AddBooksToShelf(book);
			Assert::AreEqual(firstShelf.GetNumOfBooks(), 1);
		}

		TEST_METHOD(AddLobby)
		{
			SystemOfLibraries firstlib;
			Library library;
			library.SetLibName("VitebskLib");
			
			LibraryLobby firstLobby;
			LibraryLobby secondLobby;
			firstLobby.SetNumOfPlaces(4);
			secondLobby.SetNumOfPlaces(5);

			BookShelf shelf;
			shelf.SetName("A1");

			library.AddLobby(firstLobby);
			library.AddLobby(secondLobby);

			Assert::AreEqual(library.GetNumOfLobbies(), 2);
		}

		TEST_METHOD(DeleteWorker)
		{
			SystemOfLibraries mainSystem;
			Library highLib;
			highLib.SetLibName("Minsk Library");
			highLib.SetAddress("Nezavisimosty pr-t");
			highLib.SetSpace(10);

			mainSystem.AddLibToSystem(highLib);

			Staff firstWorker;
			Staff secondWorker;
			Staff thirdWorker;
			Staff forthWorker;

			firstWorker.SetName("Ivanov", "Ivan", "Ivanovich");
			firstWorker.SetAge(34);
			firstWorker.SetJobTitle(JobTitle::LOADER);
			firstWorker.SetSalaryToStaff(500);

			secondWorker.SetName("Borisov", "Aleksey", "Petrovich");
			secondWorker.SetAge(55);
			secondWorker.SetJobTitle(JobTitle::ADMINISTRATOR);
			secondWorker.SetSalaryToStaff(800);

			thirdWorker.SetName("Borisenko", "Aleksandr", "Pavlovich");
			thirdWorker.SetAge(41);
			thirdWorker.SetJobTitle(JobTitle::SECURITY);
			thirdWorker.SetSalaryToStaff(400);

			forthWorker.SetName("Viktorova", "Lidiya", "Semenovna");
			forthWorker.SetAge(54);
			forthWorker.SetJobTitle(JobTitle::CLEANER);
			forthWorker.SetSalaryToStaff(550);

			Library mylib;
			Book firstBook;
			Book secondBook;
			Name authors_name;
			Date first_date;
			Date second_date;
			firstBook.SetBookName("Harry Potter and the Chamber of Secrets");
			firstBook.SetAgeLimit(6);
			firstBook.SetAuthorsName(authors_name, "Rowling", "Joanne", "Kathleen");
			firstBook.SetDateOfPublishing(first_date, 2, 7, 1998);
			firstBook.SetDateOfAdding(second_date, 20, 10, 2005);
			firstBook.SetFactory("London Books ltd.");
			firstBook.SetNumOfPages(251);
			firstBook.SetWear(0);

			secondBook.SetBookName("Harry Potter and the Prisoner of Azkaban");
			secondBook.SetAgeLimit(6);
			secondBook.SetAuthorsName(authors_name, "Rowling", "Joanne", "Kathleen");
			secondBook.SetDateOfPublishing(first_date, 2, 7, 1998);
			secondBook.SetDateOfAdding(second_date, 20, 10, 2006);
			secondBook.SetFactory("London Books ltd.");
			secondBook.SetNumOfPages(349);
			secondBook.SetWear(0);

			highLib.AddWorker(firstWorker);
			highLib.AddWorker(secondWorker);
			highLib.AddWorker(thirdWorker);
			highLib.AddWorker(forthWorker);

			highLib.DeleteWorker("Ivanov");

			highLib.AddBookToBase(firstBook);
			highLib.AddBookToBase(secondBook);
			highLib.DeleteBookFromBase("Harry Potter and the Prisoner of Azkaban");

			Reader reader;
			reader.SetName("Abushkevich", "Alexey", "Aleksandrovich");
			reader.SetAge(19);
			reader.SetGender(Gender::MALE);

			highLib.AddReader(reader);
			highLib.DeleteReader("Abushkevich");

			Assert::AreEqual(highLib.GetNumOfWorkers(), 3);
		}

		TEST_METHOD(DeleteLobby)
		{
			LibraryLobby firstLobby;
			LibraryLobby secondLobby;
			Library library;
			firstLobby.SetName("A");
			secondLobby.SetName("B");
			library.AddLobby(firstLobby);
			library.AddLobby(secondLobby);
			library.DeleteLobby("A");

			Assert::AreEqual(library.GetNumOfLobbies(), 1);
		}

		TEST_METHOD(BooksTests1)
		{
			Name authorsName;
			Date firstDate;
			Date secondDate;
			Date thirdDate;


			Book book;
			book.SetBookName("Harry Potter and the Chamber of Secrets");
			book.SetAgeLimit(6);
			book.SetAuthorsName(authorsName, "Rowling", "Joanne", "Kathleen");
			book.SetDateOfPublishing(firstDate, 2, 7, 1998);
			book.SetDateOfAdding(secondDate, 20, 10, 2005);
			book.SetTerm(thirdDate, 23, 10, 2023);
			book.SetFactory("London Books ltd.");
			book.SetNumOfPages(251);
			book.SetWear(0);

			Assert::AreEqual(book.GetAgeLimit(), 6);
		}

		TEST_METHOD(BooksTests2)
		{
			Book firstBook;
			Book secondBook;
			Name authors_name;
			Date first_date;
			Date second_date;
			firstBook.SetBookName("Harry Potter and the Chamber of Secrets");
			firstBook.SetAgeLimit(6);
			firstBook.SetAuthorsName(authors_name, "Rowling", "Joanne", "Kathleen");
			firstBook.SetDateOfPublishing(first_date, 2, 7, 1998);
			firstBook.SetDateOfAdding(second_date, 20, 10, 2005);
			firstBook.SetFactory("London Books ltd.");
			firstBook.SetNumOfPages(251);
			firstBook.SetWear(0);

			secondBook.SetBookName("Harry Potter and the Prisoner of Azkaban");
			secondBook.SetAgeLimit(6);
			secondBook.SetAuthorsName(authors_name, "Rowling", "Joanne", "Kathleen");
			secondBook.SetDateOfPublishing(first_date, 2, 7, 1998);
			secondBook.SetDateOfAdding(second_date, 20, 10, 2006);
			secondBook.SetFactory("London Books ltd.");
			secondBook.SetNumOfPages(349);
			secondBook.SetWear(0);

			Reader reader;
			reader.SetName("Abushkevich", "Alexey", "Aleksandrovich");
			reader.SetAge(19);
			reader.SetGender(Gender::MALE);

			reader.AddBook(firstBook);
			reader.AddBook(secondBook);
			reader.RemoveBook("Harry Potter and the Prisoner of Azkaban");

			Assert::AreEqual(reader.GetNumOfBooks(), 1);
		
		}
	};
}
