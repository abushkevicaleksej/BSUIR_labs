//
// Лабораторная работа №1 по дисциплине "Логические основы интеллектуальных систем"
// Вариант 5: Проверить, следует ли формула из заданной формулы сокращенного языка логики высказываний
// Выполнили студенты группы 221701 БГУИР:
// - Робилко Тимур Маркович
// - Абушкевич Алексей Александрович
// 
// Главный файл программы, отвечающий за пользовательский интерфейс
// 10.04.2024
//
// Источники:
// - Логические основы интеллектуальных систем. Практикум
// - Интеграционная платформа
//

using LogicalExpressionClassLibrary;
using System.Diagnostics;
using System.Diagnostics.CodeAnalysis;
using static LogicalExpressionClassLibrary.AppConstants;

ConsoleLogger.DebugLevel =
    ConsoleLogger.DebugLevels.Error |
    ConsoleLogger.DebugLevels.Warning |
    ConsoleLogger.DebugLevels.Info;

List<string> TestCases = [
    $"A",
    $"(A{LogicalSymbolsDict[LogicalSymbols.Conjunction]}B)",
    $"(B{LogicalSymbolsDict[LogicalSymbols.Conjunction]}C)",
    $"(A{LogicalSymbolsDict[LogicalSymbols.Conjunction]}(B{LogicalSymbolsDict[LogicalSymbols.Disjunction]}C))",
    $"(A{LogicalSymbolsDict[LogicalSymbols.Implication]}(B{LogicalSymbolsDict[LogicalSymbols.Equality]}C))",
    $"(({LogicalSymbolsDict[LogicalSymbols.Negation]}B){LogicalSymbolsDict[LogicalSymbols.Conjunction]}C)",
    $"(({LogicalSymbolsDict[LogicalSymbols.Negation]}A){LogicalSymbolsDict[LogicalSymbols.Disjunction]}C)",
    $"((B{LogicalSymbolsDict[LogicalSymbols.Implication]}A){LogicalSymbolsDict[LogicalSymbols.Equality]}C)",
];

void InputExpression(out LogicalExpression expr)
{
    while (true)
    {
        try
        {
            expr = new(Console.ReadLine()!);
            break;
        }
        catch (Exception e)
        {
            ConsoleLogger.Log(e.Message, ConsoleLogger.DebugLevels.Error);
            Console.WriteLine("Please, re-input expression");
        }
    }
}

void CheckImplication()
{
    Console.WriteLine("Input first formula:");
    InputExpression(out LogicalExpression expr1);

    Console.WriteLine("Input second formula:");
    InputExpression(out LogicalExpression expr2);

    //Console.WriteLine(expr1.ToTruthTableString());
    //Console.WriteLine(expr2.ToTruthTableString());
    Console.WriteLine($"{expr2} " + (expr2.ImpliesFrom(expr1) ? "implies" : "doesn't imply") + $" from {expr1}\n");
}

void CheckKnowledge()
{
    var random = new Random();

    int index = random.Next(TestCases.Count);
    LogicalExpression expr1 = new(TestCases[index]);

    index = random.Next(TestCases.Count);
    LogicalExpression expr2 = new(TestCases[index]);

    bool correctAnswer = expr1.ImpliesFrom(expr2);

    Console.WriteLine($"First formula:\t {expr1}");
    Console.WriteLine($"Second formula:\t {expr2}");
    Console.WriteLine("Does second expression imply from first one? Y/N");
    char userKeyInput = Console.ReadKey().KeyChar;
    bool userAnswer = userKeyInput == 'Y' || userKeyInput == 'y';

    if (correctAnswer == userAnswer) Console.WriteLine("\nCorrect!");
    else
    {
        Console.WriteLine("\nIncorrect! Compare truth tables to find out why:");
        Console.WriteLine(expr1.ToTruthTableString());
        Console.WriteLine(expr2.ToTruthTableString());
    };
}

//Benchmarks.Execute();

while (true)
{
    Console.WriteLine("To check consecution, press 1.\nTo check your knowledge, press 2.");

    switch (Console.ReadLine())
    {
        case "1":
            {
                CheckImplication();
                break;
            }
        case "2":
            {
                CheckKnowledge();
                break;
            }
    }
}


[ExcludeFromCodeCoverage]
public partial class Program() { }