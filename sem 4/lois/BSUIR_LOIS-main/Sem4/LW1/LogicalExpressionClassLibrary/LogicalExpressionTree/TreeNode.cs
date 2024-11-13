//
// Лабораторная работа №1 по дисциплине "Логические основы интеллектуальных систем"
// Вариант 5: Проверить, следует ли формула из заданной формулы сокращенного языка логики высказываний
// Выполнили студенты группы 221701 БГУИР:
// - Робилко Тимур Маркович
// - Абушкевич Алексей Александрович
// 
// Абстрактный класс узла синтаксического дерева для представления формулы сокращенного языка логики высказываний
// 27.02.2024
//
// Источники:
// - Основы Алгоритмизации и Программирования (2 семестр). Практикум
//

namespace LogicalExpressionClassLibrary.LogicalExpressionTree
{
    public abstract class TreeNode
    {
        private TreeNode? _right = null;
        public TreeNode? Right
        {
            get => _right;
            set
            {
                ClearEvaluation();
                _right = value;
            }
        }
        private TreeNode? _left = null;
        public TreeNode? Left
        {
            get => _left;
            set
            {
                ClearEvaluation();
                _left = value;
            }
        }
        public TreeNode? Parent { get; set; } = null;
        // Serves caching purpose and is used in truth tables
        private bool? _evaluation = null;
        public bool Evaluation
        {
            get
            {
                if (_evaluation == null)
                {
                    _evaluation = Evaluate();

                    ConsoleLogger.Log($"Evaluate {this}", ConsoleLogger.DebugLevels.Debug);
                }
                return _evaluation.Value;
            }
        }
        public TreeNode(TreeNode? left, TreeNode? right)
        {
            Right = right;
            Left = left;
        }
        protected abstract bool Evaluate();
        protected void ClearEvaluation()
        {
            if (_evaluation != null)
            {
                ConsoleLogger.Log($"Clear {GetType().Name} {this}", ConsoleLogger.DebugLevels.Debug);

                _evaluation = null;
                // If value is outdated then upper tree part is also outdated
                Parent?.ClearEvaluation();
            }
        }
    }
}
