//
// Лабораторная работа №1 по дисциплине "Логические основы интеллектуальных систем"
// Выполнили студенты группы 221701 БГУИР:
// - Робилко Тимур Маркович
// - Абушкевич Алексей Александрович
// 
// Класс для хранения unit-тестов, относящихся к классу LogicalExpression
// 11.04.2024
//
// Источники:
// - Проектирование программного обеспечения интеллектуальных систем (3 семестр)
// - Библиотека xUnit
//

using LogicalExpressionClassLibrary;
using LogicalExpressionClassLibrary.LogicalParser;
using System.Diagnostics.CodeAnalysis;

namespace LogicalExpressionUnitTest
{
    //"(A1&(A2|(¬(A3|(A4|A5)))))"
    //"((A|B)&(¬C))"
    //"((¬A)|(¬(B&C)))"
    //"(A&(B&C))",
    //"(A&(B|C))",
    //"(A→(B→C))",
    //"(B|C)",
    //"((A1|(A2&A3))|B1)",
    //"((A1|F)|T)",
    //"((P|(Q&R))|S)",
    //"((A1|(&A3))|B1)",

    // pz 2
    // "(((!P)>P)>(R|Q))"
    // "((((P>R)&(Q>S))&((!P)|(!S)))>((!P)|(!Q)))"

    [ExcludeFromCodeCoverage]
    public class LogicalExpressionUnitTest
    {
        [Theory]
        [InlineData("A")]
        [InlineData("B")]
        [InlineData("C")]
        [InlineData("((A\\/(B/\\C))\\/1)")]
        [InlineData("((A\\/0)\\/1)")]
        [InlineData("(!(!A))")]
        [InlineData("(!(!(!(!A))))")]
        [InlineData("((A\\/(B/\\C))\\/D)")]
        [InlineData("(((!A)/\\B)\\/C)")]
        public void RecursiveParsing_shouldEqual(string input)
        {
            LogicalExpression expr = new(input, new RecursiveLogicalParser());

            Assert.Equal(input, expr.ToString());
        }

        [Theory]
        [InlineData("A")]
        [InlineData("B")]
        [InlineData("C")]
        [InlineData("((A\\/(B/\\C))\\/D)")]
        [InlineData("((A\\/0)\\/1)")]
        [InlineData("(!(!A))")]
        [InlineData("(!(!(!(!A))))")]
        public void GetTruthTable_shouldNotThrow(string input)
        {
            LogicalExpression expr = new(input);

            var exception = Record.Exception(() => _ = expr.TruthTable);
            Assert.Null(exception);
        }

        [Theory]
        [InlineData("A", "A")]
        [InlineData("B", "B")]
        [InlineData("C", "C")]
        public void GetVariable_shouldReturnFalseByDefault(string input, string variable)
        {
            LogicalExpression expr = new(input);

            bool result = expr.GetVariable(variable);

            Assert.False(result);
        }

        [Theory]
        [InlineData("A", "X")]
        [InlineData("B", "X")]
        [InlineData("C", "X")]
        public void GetVariable_UninitializedVariable_ShouldThrow(string input, string variable)
        {
            LogicalExpression expr = new(input);

            Assert.Throws<ArgumentException>(() => expr.GetVariable(variable));
        }

        [Theory]
        [InlineData("((A\\/B)\\/C)", true, true, true, true)]
        [InlineData("((A\\/B)\\/C)", false, false, false, false)]
        [InlineData("((A/\\B)\\/C)", false, false, true, true)]
        [InlineData("((A/\\B)\\/C)", true, true, false, true)]
        [InlineData("((A/\\B)/\\C)", true, false, false, false)]
        [InlineData("((A/\\B)/\\C)", true, true, true, true)]
        [InlineData("((A->B)/\\C)", true, false, true, false)]
        [InlineData("((A->B)/\\C)", false, false, true, true)]
        [InlineData("((A/\\B)~C)", true, true, true, true)]
        [InlineData("((A/\\B)~C)", false, false, false, true)]
        [InlineData("(((!B)/\\A)\\/C)", false, true, false, false)]
        [InlineData("(((!A)/\\B)\\/C)", true, true, false, false)]
        public void Evaluation_shouldEqualExprected(string input, bool A, bool B, bool C, bool result)
        {
            LogicalExpression expr = new(input);
            expr.SetVariable("A", A);
            expr.SetVariable("B", B);
            expr.SetVariable("C", C);

            var actualResult = expr.Evaluation;

            Assert.Equal(result, actualResult);
        }

        [Theory]
        [InlineData("")]
        [InlineData("a")]
        [InlineData("(A)")]
        [InlineData("(A1B)")]
        [InlineData("(A=B1)")]
        [InlineData("(AB&)")]
        [InlineData("(!)")]
        [InlineData("(A!B)")]
        [InlineData("(A/\\(\\/C))")]
        [InlineData("(1_0_\\(\\/?))")]
        [InlineData("(A/\\B/\\C))))))))))))))))")]
        [InlineData("A()C")]
        [InlineData("A->B->C->D")]
        [InlineData("A->B")]
        [InlineData("(A->B->C->(G->H)->I)")]
        [InlineData("A/\\B/\\C/\\D/\\E/\\F/\\G/\\H/\\I")]
        [InlineData("(0)")]
        [InlineData("(AG)")]
        [InlineData("(A->B123)")]
        [InlineData("(AB/\\&&C)")]
        [InlineData("(A->(A))")]
        [InlineData("((A)->A)")]
        [InlineData("((A)->(A))")]
        [InlineData("(A")]
        [InlineData("A))")]
        [InlineData("A->B))")]
        [InlineData("(A->B))")]
        [InlineData("((A->B")]
        [InlineData("A->(B(C))")]
        [InlineData("(A->B)->C")]
        [InlineData("A->B)->C")]
        [InlineData("A->B)->C)")]
        [InlineData("((A->B->C))")]
        [InlineData("((A->B->C)))))->)")]
        [InlineData("(((A->B)->C->D)))")]
        [InlineData("(A->B)(!C)")]
        [InlineData("((A->(B->C)->D))")]
        public void Parsing_IncorrectNotation_shouldThrow(string input)
        {
            Assert.Throws<ArgumentException>(() => new LogicalExpression(input));
        }

        [Fact]
        public void SettingVariable_VariableChangesValue_ShouldResetEvaluation()
        {
            LogicalExpression expr = new("((A/\\B)~C)");
            expr.SetVariable("A", true);
            expr.SetVariable("B", false);
            expr.SetVariable("C", false);
            var oldResult = expr.Evaluation;

            expr.SetVariable("B", true);

            Assert.NotEqual(oldResult, expr.Evaluation);
        }


        [Theory]
        [InlineData("A", "B", false)]
        [InlineData("(A->B)", "((!A)\\/B)", true)]
        [InlineData("A", "A", true)]
        [InlineData("(A->B)", "((!B)->(!A))", true)]
        [InlineData("(A->B)", "((!B)->A)", false)]
        [InlineData("(A/\\B)", "A", true)]
        [InlineData("((A/\\B)->C)", "(A->(B->C))", true)]
        [InlineData("((A->B)/\\(B->C))", "(A->C)", true)]
        [InlineData("(A/\\(B\\/C))", "((A/\\B)\\/(A/\\C))", true)]
        [InlineData("(A->(B/\\C))", "((A/\\B)\\/(A/\\C))", false)]
        [InlineData("(A->(B/\\C))", "((A->B)/\\(A->C))", true)]
        public void ImpliesFrom_GivenCorrectData_ResultShouldEqual(string first_formula, string second_formula, bool result)
        {
            LogicalExpression expr1 = new(first_formula);
            LogicalExpression expr2 = new(second_formula);
            bool actualResult = expr2.ImpliesFrom(expr1);
            Assert.Equal(result, actualResult);
        }

    }
}