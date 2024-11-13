//
// Лабораторная работа №1 по дисциплине "Логические основы интеллектуальных систем"
// Вариант 5: Проверить, следует ли формула из заданной формулы сокращенного языка логики высказываний
// Выполнили студенты группы 221701 БГУИР:
// - Робилко Тимур Маркович
// - Абушкевич Алексей Александрович
// 
// Класс узла синтаксического дерева для представления атомарной формулы логики высказываний
// 27.02.2024
//
// Источники:
// - Основы Алгоритмизации и Программирования (2 семестр). Практикум
//

namespace LogicalExpressionClassLibrary.LogicalExpressionTree.ValueNodes
{
    public sealed class AtomicFormulaNode : TreeNode
    {
        private string _name = string.Empty;
        public string Name
        {
            get => _name;
            set
            {
                if (!ValidateName(value))
                {
                    throw new ArgumentException("Invalid atomic formula");
                }

                _name = value;
            }
        }

        private bool _value = false;
        public bool Value

        {
            get => _value;
            set
            {
                ConsoleLogger.Log($"Set {Name} to {value}", ConsoleLogger.DebugLevels.Debug);
                
                if (_value != value)
                {
                    ClearEvaluation();
                    _value = value;
                }
            }
        }

        public AtomicFormulaNode(string name) : base(null, null)
        {
            Name = name;
        }
        protected override bool Evaluate() => Value;

        private static bool ValidateName(string name)
        {
            if (name.Length != 1 || !char.IsLetter(name[0]) || !char.IsUpper(name[0]))
            {
                return false;
            }
            return true;
        }
        public override string ToString() => Name;
    }
}