//
// Лабораторная работа №1 по дисциплине "Логические основы интеллектуальных систем"
// Выполнили студенты группы 221701 БГУИР:
// - Робилко Тимур Маркович
// - Абушкевич Алексей Александрович
// 
// Класс для хранения unit-тестов, относящихся к классу TreeNode
// 30.02.2024
//
// Источники:
// - Проектирование программного обеспечения интеллектуальных систем (3 семестр)
// - Библиотека xUnit
//

using LogicalExpressionClassLibrary;
using LogicalExpressionClassLibrary.LogicalExpressionTree;
using LogicalExpressionClassLibrary.LogicalExpressionTree.ValueNodes;
using System.Diagnostics.CodeAnalysis;

namespace LogicalExpressionUnitTest
{
    [ExcludeFromCodeCoverage]
    public class TreeNodeTest
    {
        [Theory]
        [InlineData("A0")]
        [InlineData("1B")]
        [InlineData("")]
        [InlineData("(")]
        public void AtomicFormulaNode_IncorrectName_shouldThrow(string input)
        {
            Assert.Throws<ArgumentException>(() => new AtomicFormulaNode(input));
        }
    }
}