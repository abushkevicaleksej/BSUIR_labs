using System.Diagnostics;
using System.Diagnostics.CodeAnalysis;
using static LogicalExpressionClassLibrary.AppConstants;

namespace LogicalExpressionClassLibrary
{
    [ExcludeFromCodeCoverage]
    public class Benchmarks
    {
        static string BuildTest(int varCount, LogicalSymbols op)
        {
            List<char> symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

            if (varCount < 1 && varCount > symbols.Count)
            {
                throw new NotImplementedException();
            }

            string result = string.Empty;

            result += symbols[0];

            for (int i = 1; i < varCount; i++)
            {
                result = result.Insert(0, LogicalSymbolsDict[LogicalSymbols.LeftBracket]);
                result = result += LogicalSymbolsDict[op] + symbols[i] + LogicalSymbolsDict[LogicalSymbols.RightBracket];
            }

            return result;
        }

        public static void Execute()
        {
            Stopwatch sw = new();

            List<int> cases = [1, 4, 7, 10, 15, 20, 23, 26];
            
            foreach (int testCase in cases)
            {
                LogicalExpression expr0 = new(BuildTest(testCase, LogicalSymbols.Implication));
                LogicalExpression expr1 = new(BuildTest(testCase, LogicalSymbols.Equality));

                string str0 = expr0.ToString();
                string str1 = expr1.ToString();

                // Naive approach
                //sw.Restart();
                //bool resultNaive = new LogicalExpression($"({str1}->{str0})").IsTautology();
                ////Console.WriteLine($"{str0} " + (resultNaive ? "implies" : "doesn't imply") + $" from {str1}");
                //sw.Stop();
                //Console.WriteLine($"{testCase} VARIABLES. NAIVE - ELAPSED {sw.Elapsed}");

                // Optimized approach
                sw.Restart();
                bool resultGood = expr0.ImpliesFrom(expr1);
                Console.WriteLine($"{str0} " + (resultGood ? "implies" : "doesn't imply") + $" from {str1}");
                sw.Stop();
                Console.WriteLine($"{testCase} variables. Elapsed {sw.Elapsed}");
            }
        }
    }
}
