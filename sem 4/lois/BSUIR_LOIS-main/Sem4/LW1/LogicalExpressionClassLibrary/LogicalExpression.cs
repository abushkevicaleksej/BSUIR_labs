//
// Лабораторная работа №1 по дисциплине "Логические основы интеллектуальных систем"
// Вариант 5: Проверить, следует ли формула из заданной формулы сокращенного языка логики высказываний
// Выполнили студенты группы 221701 БГУИР:
// - Робилко Тимур Маркович
// - Абушкевич Алексей Александрович
// 
// Класс, отвечающий за представление логического выражения в памяти компьютера
// 27.03.2024
//
// Источники:
// - Основы Алгоритмизации и Программирования (2 семестр). Практикум
//

using LogicalExpressionClassLibrary.LogicalExpressionTree;
using LogicalExpressionClassLibrary.LogicalExpressionTree.OperationNodes;
using LogicalExpressionClassLibrary.LogicalExpressionTree.ValueNodes;
using LogicalExpressionClassLibrary.LogicalParser;
using System.Collections;
using System.Diagnostics.CodeAnalysis;
using System.Text;
using static LogicalExpressionClassLibrary.AppConstants;

namespace LogicalExpressionClassLibrary
{
    public sealed class LogicalExpression
    {
        private readonly Dictionary<string, List<AtomicFormulaNode>> _variables = [];
        private TreeNode? _root;

        private List<Dictionary<string, bool>>? _truthTable;
        public List<Dictionary<string, bool>> TruthTable
        {
            get
            {
                _truthTable ??= BuildTruthTable();
                return new(_truthTable);
            }
        }
        public bool Evaluation => _root!.Evaluation;
        public LogicalExpression(string input, AbstractLogicalParser logicalParser = null!)
        {
            if (input.Length == 0)
            {
                throw new ArgumentException("Expression notation is empty");
            }

            // Inject new parser if provided
            logicalParser = logicalParser is null ? new RecursiveLogicalParser() : logicalParser;

            (_root, _variables) = logicalParser.Parse(input);
        }
        private LogicalExpression() { }
        private static void NextCombination(BitArray bits)
        {
            for (int i = bits.Length - 1; i >= 0; i--)
            {
                bits[i] = !bits[i];

                if (bits[i])
                {
                    break;
                }
            }
        }
        private static void StoreEvaluation(Dictionary<string, bool> truthRow, TreeNode? root)
        {
            if (root is null)
            {
                return;
            }

            truthRow[root.ToString()!] = root.Evaluation;

            StoreEvaluation(truthRow, root.Left);
            StoreEvaluation(truthRow, root.Right);
        }
        private List<Dictionary<string, bool>> BuildTruthTable()
        {
            List<Dictionary<string, bool>> truthTable = [];

            // Preserve initial state before checking all combinations of variables
            Dictionary<string, bool> initialVariablesState = [];

            foreach (var kvp in _variables!)
            {
                initialVariablesState[kvp.Key] = kvp.Value[0].Value;
            }

            // Mask indicates which variables will be true
            BitArray variablesTruthMask = new(_variables.Count, false);

            do
            {
                ConsoleLogger.Log("Next combination of values", ConsoleLogger.DebugLevels.Debug);

                int variableIndex = 0;

                foreach (var v in _variables.Values)
                {
                    foreach (var node in v)
                    {
                        node.Value = variablesTruthMask[variableIndex];
                    }

                    variableIndex++;
                }

                Dictionary<string, bool> truthRow = [];

                StoreEvaluation(truthRow, _root);

                truthTable.Add(truthRow);

                NextCombination(variablesTruthMask);
            }
            while (variablesTruthMask.HasAnySet());

            ConsoleLogger.Log("Reverting to default values", ConsoleLogger.DebugLevels.Debug);

            foreach (var kv in initialVariablesState)
            {
                var listOfNodesToReset = _variables[kv.Key];

                foreach (var node in listOfNodesToReset)
                {
                    node.Value = kv.Value;
                }
            }

            return truthTable;
        }
        public bool GetVariable(string varName)
        {
            if (_variables!.TryGetValue(varName, out var variable) == true && variable.Count > 0)
            {
                return variable[0].Value;
            }
            else throw new ArgumentException($"Uninitialized variable '{varName}' addressed");
        }
        public void SetVariable(string varName, bool variableValue)
        {
            if (_variables!.TryGetValue(varName, out var variableList))
            {
                foreach (var variable in variableList)
                {
                    variable.Value = variableValue;
                }
            }
            else throw new ArgumentException($"Uninitialized variable '{varName}' addressed");
        }
        public override string ToString() => _root?.ToString()!;

        [ExcludeFromCodeCoverage]
        public string ToTruthTableString()
        {
            const int MaxColumnTitleWidth = 20;

            StringBuilder builder = new();

            foreach (var k in TruthTable[0].Keys)
            {
                builder.Append($"| {k[..Math.Min(k.Length, MaxColumnTitleWidth)]} ");
            }
            builder.AppendLine("| Total |");

            var separator = string.Empty.PadRight(builder.Length - 2, '-') + '\n';

            builder.Insert(0, separator).Append(separator);

            foreach (var truthRow in TruthTable)
            {
                foreach (var kvp in truthRow)
                {
                    string v = kvp.Value ? $"| {LogicalSymbolsDict[LogicalSymbols.True]} " : $"| {LogicalSymbolsDict[LogicalSymbols.False]} ";

                    builder.Append(v.PadRight(Math.Min(kvp.Key.Length, MaxColumnTitleWidth) + 3));
                }

                var expressionValue = truthRow[ToString()];
                builder.AppendLine(expressionValue ? $"|   {LogicalSymbolsDict[LogicalSymbols.True]}   |" : $"|   {LogicalSymbolsDict[LogicalSymbols.False]}   |");
            }

            builder.Append(separator);

            return builder.ToString();
        }
        public bool ImpliesFrom(LogicalExpression source)
        {
            LogicalExpression implication = new();
            #region Build implication expression

            var newRoot = new ImplicationNode(source._root, _root);

            _root.Parent = newRoot;
            source._root.Parent = newRoot;

            implication._root = newRoot;

            foreach (var variable in source._variables)
            {
                implication._variables.Add(variable.Key, variable.Value);
            }
            foreach (var variable in _variables)
            {
                if (implication._variables.TryGetValue(variable.Key, out var varlist))
                {
                    varlist.AddRange(_variables[variable.Key]);
                }
                else
                {
                    implication._variables.Add(variable.Key, variable.Value);
                }
            }
            #endregion

            bool resultBoolean = true;

            // Preserve initial state before checking all combinations of variables
            Dictionary<string, bool> initialVariablesState = [];

            foreach (var kvp in implication._variables)
            {
                initialVariablesState[kvp.Key] = kvp.Value[0].Value;
            }

            // Mask indicates which variables will be true
            BitArray variablesTruthMask = new(implication._variables.Count, false);

            do
            {
                int variableIndex = 0;

                foreach (var v in implication._variables.Values)
                {
                    foreach (var node in v)
                    {
                        node.Value = variablesTruthMask[variableIndex];
                    }

                    variableIndex++;
                }

                if (implication.Evaluation == false)
                {
                    resultBoolean = false;
                    break;
                }

                NextCombination(variablesTruthMask);
            }
            while (variablesTruthMask.HasAnySet());

            #region Restore initial values

            foreach (var kv in initialVariablesState)
            {
                var listOfNodesToReset = implication._variables[kv.Key];

                foreach (var node in listOfNodesToReset)
                {
                    node.Value = kv.Value;
                }
            }

            _root.Parent = null;
            source._root.Parent = null;

            #endregion

            return resultBoolean;
        }
    }
}
