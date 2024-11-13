#include "FloatNumber.h"
#include "BinaryNumber.h"


int main() {
    setlocale(LC_ALL, "Russian");
    int x, y;
    std::cout << "Введите первое число: ";
    std::cin >> x;
    std::cout << "Введите второе число: ";
    std::cin >> y;
    BinaryNumber a(intToBinary(x)), b(intToBinary(y));
    
        std::cout << "Прямой код числа " << x << ": " << a.GetValue() << std::endl;
        std::cout << "Обратный код числа " << x << ": " << toComplement(a.GetValue()) << std::endl;
        std::cout << "Дополнительный код числа " << x << ": " << toTwosComplement(a.GetValue()) << std::endl;
    
        std::cout << "Прямой код числа " << y << ": " << b.GetValue() << std::endl;
        std::cout << "Обратный код числа " << y << ": " << toComplement(b.GetValue()) << std::endl;
        std::cout << "Дополнительный код числа " << y << ": " << toTwosComplement(b.GetValue()) << std::endl;
   
        BinaryNumber sum = a + b;
        std::cout << "Сумма " << ": " << sum.GetValue() << "   " << binaryToDecimal(sum.GetValue()) << std::endl;

        BinaryNumber raz = a - b;
        std::cout << "Raznost' " << ": " << raz.GetValue() << "   " << binaryToDecimal(raz.GetValue()) << std::endl;

        BinaryNumber mult = a * b;
        std::cout << "Umnoj " << ": " << mult.GetValue() << "   " << binaryToDecimal(mult.GetValue()) << std::endl;

        BinaryNumber dd = a / b;
        std::cout << "Delenie " << ": " << dd.GetValue() << "   " << std::endl;

        std::cout << "Десятичное " << x << ": " << binaryToDecimal(a.GetValue()) << std::endl;

        std::cout << "Десятичное " << y << ": " << binaryToDecimal(b.GetValue()) << std::endl;

        std::cout << "Первое число с плавающей точкой:" << std::endl;

        float floatNum1 = 0, floatNum2 = 0;

        FloatToBinaryConverter outputF;

        std::cin >> floatNum1;

        FloatToBinaryConverter num1F(floatNum1);

        std::cout << "Двоичная форма:" << std::endl;

        num1F.ConsoleOutput();

        std::cout << std::endl;

        std::cout << "Второе число с плавающей точкой:" << std::endl;

        std::cin >> floatNum2;

        FloatToBinaryConverter num2F(floatNum2);

        std::cout << "Двоичная форма:" << std::endl;

        num2F.ConsoleOutput();

        std::cout << "Сумма:" << std::endl;

        outputF = num1F + num2F;

        outputF.ConsoleOutput();

        std::cout << floatNum1 << " + " << floatNum2 << " = " <<std::endl;
    return 0;
}