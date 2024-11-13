//
// Лабораторная работа №1 по дисциплине "Логические основы интеллектуальных систем"
// Вариант 5: Проверить, следует ли формула из заданной формулы сокращенного языка логики высказываний
// Выполнили студенты группы 221701 БГУИР:
// - Робилко Тимур Маркович
// - Абушкевич Алексей Александрович
// 
// Абстрактный класс парсера строковой записи логического выражения, предоставляющий
// базовый функционал для установления соответствия символов алфавита классам программы
// 27.03.2024
//
// Источники:
// - Основы Алгоритмизации и Программирования (2 семестр). Практикум
//

using LogicalExpressionClassLibrary.LogicalExpressionTree;
using LogicalExpressionClassLibrary.LogicalExpressionTree.OperationNodes;
using LogicalExpressionClassLibrary.LogicalExpressionTree.ValueNodes;
using static LogicalExpressionClassLibrary.AppConstants;

namespace LogicalExpressionClassLibrary.LogicalParser
{
    public abstract class AbstractLogicalParser
    {
        public static readonly Dictionary<LogicalSymbols, Func<TreeNode, TreeNode, TreeNode>> _binaryOperatorsNodes = new()
            {
                { LogicalSymbols.Conjunction, (left, right) => new ConjunctionNode(left, right) },
                { LogicalSymbols.Disjunction, (left, right) => new DisjunctionNode(left, right) },
                { LogicalSymbols.Implication, (left, right) => new ImplicationNode(left, right) },
                { LogicalSymbols.Equality,    (left, right) => new EqualityNode(left, right) },
            };

        public static readonly Dictionary<LogicalSymbols, TreeNode> _constNodes = new()
            {
                { LogicalSymbols.True, TrueNode.GetInstance() },
                { LogicalSymbols.False, FalseNode.GetInstance() },
            };
        public abstract (TreeNode root, Dictionary<string, List<AtomicFormulaNode>> variables) Parse(string input);
    }
}