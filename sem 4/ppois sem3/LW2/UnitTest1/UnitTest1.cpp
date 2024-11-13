#include "pch.h"
#include "CppUnitTest.h"
#include "../Project1/HeaderPicker.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1
{
	TEST_CLASS(UnitTest1)
	{
	public:
		
		TEST_METHOD(AddDriverTest)
		{
			Driver driver;
			driver.SetAge(56);
			driver.SetEmail("abuskevicaleksej@gmail.com");
			driver.SetPhoneNumber("80295966635");
			driver.SetName("Ivanov","Boris","Petrovich");
			driver.SetTypeOfDriversVehicle(TypeOfVehicle::BUS);
			Assert::AreEqual(driver.GetAge(), 56);
		}

		TEST_METHOD(AddEmployeeAndCompanyTest)
		{
			Company company1("VitebskTrans");
			Company company2("MinskTrans");
			Driver driver1;
			Employee employee;
			driver1.SetInfoAbout("Ivanov", "Ivan", "Ivanovich");
			driver1.SetTypeOfDriversVehicle(TypeOfVehicle::TAXI);
			employee.SetInfoAbout("Bobkov", "Igor", "Vitalievich");
			employee.SetJobTitle("Dispetcher");
			driver1.SetAge(30);
			company1.AddEmployee(employee);
			company1.AddDriver(driver1);
			company2.AddDriver(driver1);
			Assert::IsTrue(company1.GetCompanyName()!= company2.GetCompanyName());
		}

		TEST_METHOD(AddConsumerTest)
		{
			Company company1("VitebskTrans");
			Consumer klient;
			Route marshroute;
			Booking booking;
			Date date;
			date.SetDate(10, 12, 2023);

			marshroute.SetRouteName("Minsk - Vitebsk");
			marshroute.SetNumOfTime(120);
			marshroute.SetPlace("Minsk Avtovokzal - Vitebsk Avtovokzal");
			marshroute.SetDate(date);
			company1.AddRoute(marshroute);

			klient.SetName("Petrov", "Petr", "Petrovich");
			klient.SetAge(20);
			klient.AddOrder(booking);
			klient.Pay(booking);


			Assert::IsTrue(booking.GetStatus() != Status::EXPECTATION);
		}

		TEST_METHOD(ApplyDiscountTest)
		{
			Company company1("MogilevTrans");
			Consumer klient;
			Route marshroute;
			Booking booking;
			Date date;
			date.SetDate(10, 12, 2023);

			marshroute.SetRouteName("Minsk - Mogilev");
			marshroute.SetNumOfTime(120);
			marshroute.SetPlace("Minsk Avtovokzal - Mogilev Avtovokzal");
			marshroute.SetDate(date);
			company1.AddRoute(marshroute);

			klient.SetName("Doe", "John", "Martinez");
			klient.SetAge(7);
			klient.AddOrder(booking);
			klient.Pay(booking);

			Assert::IsTrue(klient.GetDiscount() == Discount::CHILD_UNDER_7);
		}

		TEST_METHOD(AddDiversVehicleTest)
		{
			Vehicle car;
			Driver driver;
			driver.SetInfoAbout("Sohov", "Ivan", "Alekseevich");
			driver.SetAge(45);
			driver.SetPhoneNumber("88005553535");
			driver.SetEmail("sohovivan@yandex.ru");
			
			car.SetModel("Mercedes Sprinter");
			car.SetNumOfPlaces(25);
			car.SetTypeOfVehicle(TypeOfVehicle::BUS_TAXI);
			car.FillThePlace();
			
			driver.SetDriversVehicle(car);

			Assert::AreEqual(car.GetNumOfPlaces(),24);
		}
	};
}
