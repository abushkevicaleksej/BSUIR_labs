//
// Лабораторная работа №1 по дисциплине "Логические основы интеллектуальных систем"
// Вариант 5: Проверить, следует ли формула из заданной формулы сокращенного языка логики высказываний
// Выполнили студенты группы 221701 БГУИР:
// - Робилко Тимур Маркович
// - Абушкевич Алексей Александрович
// 
// Объявление символов алфавита сокращенного языка логики высказываний
// 10.04.2024
//
// Источники:
// - Логические основы интеллектуальных систем. Практикум
//

namespace LogicalExpressionClassLibrary
{
    public static class AppConstants
    {
        public enum LogicalSymbols
        {
            Disjunction,
            Conjunction,
            LeftBracket,
            RightBracket,
            Equality,
            Implication,
            Negation,
            False,
            True,
        };
        public static Dictionary<LogicalSymbols, string> LogicalSymbolsDict = new()
        {
            { LogicalSymbols.Disjunction, "\\/" },
            { LogicalSymbols.Conjunction, "/\\" },
            { LogicalSymbols.LeftBracket, "(" },
            { LogicalSymbols.RightBracket, ")" },
            { LogicalSymbols.Equality, "~" },
            { LogicalSymbols.Implication, "->" },
            { LogicalSymbols.Negation, "!" },
            { LogicalSymbols.False, "0" },
            { LogicalSymbols.True, "1" },
    };
    }
}
