//
// Лабораторная работа №1 по дисциплине "Логические основы интеллектуальных систем"
// Вариант 5: Проверить, следует ли формула из заданной формулы сокращенного языка логики высказываний
// Выполнили студенты группы 221701 БГУИР:
// - Робилко Тимур Маркович
// - Абушкевич Алексей Александрович
// 
// Класс, отвечающий за логгирование информации в консоль
// 27.03.2024
//
// Источники:
// - Библиотека логгирования Serilog для C#
//

using System.Diagnostics;
using System.Diagnostics.CodeAnalysis;

namespace LogicalExpressionClassLibrary
{
    [ExcludeFromCodeCoverage]
    public static class ConsoleLogger
    {
        public static DebugLevels DebugLevel = 0;
        [Flags]
        public enum DebugLevels
        {
            Error = 1,
            Warning = 2,
            Info = 4,
            Debug = 8
        }
        static ConsoleLogger()
        {
            Console.ForegroundColor = ConsoleColor.White;
        }
        public static void Log(string message, DebugLevels level = DebugLevels.Info)
        {
            if (DebugLevel.HasFlag(level))
            {
                var className = new StackTrace().GetFrame(1)?.GetMethod()?.ReflectedType!.Name;

                Console.ForegroundColor = level switch
                {
                    DebugLevels.Info => ConsoleColor.DarkCyan,
                    DebugLevels.Warning => ConsoleColor.DarkYellow,
                    DebugLevels.Error => ConsoleColor.DarkRed,
                    DebugLevels.Debug => ConsoleColor.DarkGreen,
                    _ => ConsoleColor.White,
                };
                Console.Write($"[{level}] ");
                Console.ForegroundColor = ConsoleColor.DarkGray;
                Console.Write($"[{className}] ");
                Console.ForegroundColor = ConsoleColor.White;
                Console.WriteLine($"{message}");
            }
        }
    }
}
