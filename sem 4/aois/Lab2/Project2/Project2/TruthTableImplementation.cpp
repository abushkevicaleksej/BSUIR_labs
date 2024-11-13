#include "TruthTable.h"
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <numeric>
#include <iomanip>


#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_set>
#include <cmath>
#include <algorithm>
int IsOperator(char c)
{
    switch (c)
    {
    case '!':
    case '&':
    case '|':
    case '>':
    case '~':
        return 1;
    }
    return 0;
}
int IsBinaryOperator(char c)
{
    return c != '!' && IsOperator(c);
}
int IsInvalidChar(char c)
{
    if (c == '(' || c == ')')
        return 0;
    else if (isupper(c) || IsOperator(c))
        return 0;
    return 1;
}
int IsUpperAlpha(char c)
{
    return isupper(c);
}
int Priority(char operation)
{
    switch (operation)
    {
    case '!':
        return 5;
    case '&':
        return 4;
    case '|':
        return 3;
    case '>':
        return 2;
    case '~':
        return 1;
    default:
        return 0;
    }
}

int IsValidExpression(const string& expression)
{
    if (expression.empty())
    {
        throw std::invalid_argument("You didn't enter anything!");
    }

    string::const_iterator pos;
    pos = find_if(expression.begin(), expression.end(), IsInvalidChar);
    if (pos != expression.end())
    {
        throw std::invalid_argument("Invalid characters: '" + string(1, *pos) + "'");
    }
    vector<int> bracketpos[2];
    for (pos = expression.begin(); pos != expression.end(); ++pos)
    {
        if (*pos == '(')
            bracketpos[0].push_back(distance(expression.begin(), pos));
        else if (*pos == ')')
            bracketpos[1].push_back(distance(expression.begin(), pos));
    }
    vector<int>::size_type vector;
    for (vector = 0; vector != bracketpos[0].size(); ++vector)
    {
        if (bracketpos[0][vector] > bracketpos[1][vector])
        {
            throw std::invalid_argument("Bracket positions don't match!");
        }
    }
    return 1;
}


set<char> GetExpressionInfo(const string& expression)
{
    set<char> expression_elem;

    for (string::size_type i = 0; i != expression.size(); ++i)
    {
        if (isupper(expression[i]))
        {
            expression_elem.insert(expression[i]);
        }
    }
    return expression_elem;
}

string InfixToSuffix(const string& expression)
{
    char top;
    stack<char> stack;
    string suffix;

    for (string::size_type i = 0; i != expression.size(); ++i)
    {
        if (isupper(expression[i]))
            suffix += expression[i];
        else if (expression[i] == '(')
            stack.push(expression[i]);
        else if (IsOperator(expression[i]))
        {
            while (1)
            {
                if (stack.empty() || stack.top() == '(')
                {
                    stack.push(expression[i]);
                    break;
                }
                else
                {
                    top = stack.top();
                    if (Priority(expression[i]) > Priority(top) || (expression[i] == '!' && top == '!'))
                    {
                        stack.push(expression[i]);
                        break;
                    }
                    else
                    {
                        suffix += stack.top();
                        stack.pop();
                    }
                }
            }
        }
        else if (expression[i] == ')')
        {
            while (!stack.empty() && (top = stack.top()) != '(')
            {
                suffix += top;
                stack.pop();
            }
            stack.pop();
        }

    }
    while (!stack.empty())
    {
        suffix += stack.top();
        stack.pop();
    }
    return suffix;
}

int Eval(const string& row, const string& suffix, const set<char>& expression_elem)
{
    char intermediate = 0;
    int first, second, result;
    stack<char> stack;
    map<char, int> map;
    string::size_type i;

    set<char>::const_iterator pos;
    for (pos = expression_elem.begin(), i = 0; pos != expression_elem.end(); ++pos, ++i)
    {
        map.insert(pair<char, int>(*pos, row[i] - '0'));
    }

    first = second = 0;
    for (i = 0; i != suffix.size(); ++i)
    {
        if (isupper(suffix[i]))
            stack.push(map[suffix[i]]);
        else if (IsOperator(suffix[i]))
        {
            second = stack.top();
            stack.pop();

            if (suffix[i] != '!' && !stack.empty())
            {
                first = stack.top();
                stack.pop();
            }

            switch (suffix[i])
            {
            case '!':
                intermediate = !second;
                break;
            case '&':
                intermediate = first && second;
                break;
            case '|':
                intermediate = first || second;
                break;
            case '>':
                intermediate = !first || second;
                break;
            case '~':
                intermediate = first == second;
            }
            stack.push(intermediate);
        }
    }
    result = stack.top();
    stack.pop();
    return result;
}

vector<char> PrintTable(const string& expression, vector<int>& index)
{
    int cols, rows, intermediate;
    string row, suffix;
    set<char> expression_elem;

    expression_elem = GetExpressionInfo(expression);
    for (set<char>::iterator pos = expression_elem.begin(); pos != expression_elem.end(); ++pos)
    {
        cout << '\t' << *pos;
    }
    cout << '\t' << expression << endl;

    suffix = InfixToSuffix(expression);
    cols = expression_elem.size();
    rows = static_cast<int>(pow(2.0, cols));

    bitset<26> bsize;
    vector<char> result;
    for (int i = 0; i < rows; ++i)
    {
        bsize = i;
        row = bsize.to_string();
        row = bsize.to_string<char, char_traits<char>, allocator<char> >();
        row.erase(0, 26 - cols);
        for (int j = 0; j < cols; ++j)
        {
            cout << '\t' << row[j];
        }
        intermediate = Eval(row, suffix, expression_elem);
        result.push_back(intermediate);
        cout << '\t' << intermediate << endl;

        index.push_back(intermediate);
    }
    return result;
}

double CountIndexNumber(double &decimal, vector<int>&index)
{
    for (int i = 0; i < index.size(); i++)
    {
        decimal = decimal * 2 + index[i];
        cout << index[i] << " ";
    }
    cout << " = index = " << decimal << endl;
    return decimal;
}


int IsTautology(const vector<char>& result)
{
    return result.end() == find(result.begin(), result.end(), 0);
}

int IsContradiction(const vector<char>& result)
{
    return result.end() == find(result.begin(), result.end(), 1);
}


string PrintCnf(const vector<char>& result, const set<char>& expression_elem)
{
    if (IsTautology(result))
        return "";

    vector<char> element;
    copy(expression_elem.begin(), expression_elem.end(), back_inserter(element));

    size_t i, j;
    vector<int> vector;
    for (i = 0; i != result.size(); ++i)
    {
        if (result[i] == 0)
            vector.push_back(i);
    }

    ostringstream oss;
    cout << "CNF\n" << "CNF Index Form (";
    for (i = 0; i != vector.size(); ++i)
    {
        if (i < vector.size() - 1)
            cout << vector[i] << ", ";
        else
            cout << vector[i];
    }
    cout << ')' << endl;

    bitset<26> bsize;
    string row;
    for (i = 0; i != vector.size(); ++i)
    {
        oss << '(';
        bsize = vector[i];
        row = bsize.to_string();
        row = bsize.to_string<char, char_traits<char>, allocator<char> >();
        row.erase(0, 26 - element.size());
        for (j = 0; j != element.size(); ++j)
        {
            if (row[j] == '1')
                oss << "!" << element[j];
            else
                oss << element[j];

            if (j < element.size() - 1)
                oss << " | ";
        }
        if (i < vector.size() - 1)
            oss << ") & ";
        else
            oss << ')';
    }
    return oss.str();
}

string PrintDnf(const vector<char>& result, const set<char>& expression_elem)
{
    if (IsContradiction(result))
        return "";

    vector<char> element;
    copy(expression_elem.begin(), expression_elem.end(), back_inserter(element));

    size_t i, j;
    vector<int> vector;
    for (i = 0; i != result.size(); ++i)
    {
        if (result[i] == 1)
            vector.push_back(i);
    }

    ostringstream oss;
    cout << "DNF\n" << "DNF Index Form (";
    for (i = 0; i != vector.size(); ++i)
    {
        if (i < vector.size() - 1)
            cout << vector[i] << ", ";
        else
            cout << vector[i];
    }
    cout << ')' << endl;

    bitset<26> bsize;
    string row;
    for (i = 0; i != vector.size(); ++i)
    {
        oss << '(';
        bsize = vector[i];
        row = bsize.to_string<char, char_traits<char>, allocator<char> >();
        row.erase(0, 26 - element.size());
        for (j = 0; j != element.size(); ++j)
        {
            if (row[j] == '1')
                oss << element[j];
            else
                oss << "!" << element[j];

            if (j < element.size() - 1)
                oss << " & ";
        }
        if (i < vector.size() - 1)
            oss << ") | ";
        else
            oss << ')';
    }
    return oss.str();
}

bool IsValidCNFExpression(const std::string& expression) {
    bool in_literal = false;  // Флаг, указывающий на нахождение внутри литерала
    bool in_term = false;     // Флаг, указывающий на нахождение внутри терма

    for (char c : expression) {
        if (c == '(') {
            if (in_term || in_literal) {
                // Если уже находимся внутри терма или литерала, это ошибка
                return false;
            }
            in_term = true;  // Входим в новый терм
        }
        else if (c == ')') {
            if (!in_literal || !in_term) {
                // Если не находимся внутри литерала или терма, это ошибка
                return false;
            }
            in_literal = false;  // Заканчиваем литерал
            in_term = false;     // Заканчиваем терм
        }
        else if (c == '|') {
            if (!in_literal) {
                // Если встречаем оператор и не внутри литерала, это ошибка
                return false;
            }
        }
        else if (c == '&')
        {
            if (in_term)
            {
                return false;
            }
        }
        else if (std::isalpha(c)) {
            if (!in_term) {
                // Если встречаем букву вне терма, это ошибка
                return false;
            }
            in_literal = true;  // Начинаем новый литерал
        }
        else if (std::isspace(c)) {
            // Пропускаем пробелы
            continue;
        }
        else {
            // Если встречаем недопустимый символ, это ошибка
            return false;
        }
    }
    // Убедимся, что мы закончили в корректном состоянии (не внутри терма или литерала)
    return !in_literal && !in_term;
}

bool IsValidDNFExpression(const string& expression) {
    bool in_literal = false;  // Флаг, указывающий на нахождение внутри литерала
    bool in_term = false;     // Флаг, указывающий на нахождение внутри терма

    for (char c : expression) {
        if (c == '(') {
            if (in_term || in_literal) {
                // Если уже находимся внутри терма или литерала, это ошибка
                return false;
            }
            in_term = true;  // Входим в новый терм
        }
        else if (c == ')') {
            if (!in_literal || !in_term) {
                // Если не находимся внутри литерала или терма, это ошибка
                return false;
            }
            in_literal = false;  // Заканчиваем литерал
            in_term = false;     // Заканчиваем терм
        }
        else if (c == '&') {
            if (!in_literal) {
                // Если встречаем оператор и не внутри литерала, это ошибка
                return false;
            }
        }
        else if (c == '|')
        {
            if (in_term)
            {
                return false;
            }
        }
        else if (std::isalpha(c)) {
            if (!in_term) {
                // Если встречаем букву вне терма, это ошибка
                return false;
            }
            in_literal = true;  // Начинаем новый литерал
        }
        else if (std::isspace(c)) {
            // Пропускаем пробелы
            continue;
        }
        else {
            // Если встречаем недопустимый символ, это ошибка
            return false;
        }
    }
    // Убедимся, что мы закончили в корректном состоянии (не внутри терма или литерала)
    return !in_literal && !in_term;
}


bool IsValidDNF(const string& expression) {
    if (IsValidDNFExpression(expression) == 0)
    {
        return false;
    }
    set <char> dnfelem = GetExpressionInfo(expression);
    return true;
}


bool IsValidCNF(const string& expression) {
    if (IsValidCNFExpression(expression) == 0)
    {
        return false;
    }
    set <char> cnfelem = GetExpressionInfo(expression);
    return true;
}

string InputCNF() {
    string expression;
    cout << "Enter a CNF expression:" << endl;
    cin >> expression;
    if (!IsValidCNF(expression)) {
        throw std::invalid_argument("Invalid CNF expression!");
    }
    return expression;
}

string InputDNF() {
    string expression;
    cout << "Enter a DNF expression:" << endl;
    cin >> expression;
    if (!IsValidDNF(expression)) {
        throw std::invalid_argument("Invalid DNF expression!");
    }
    return expression;
}


std::vector<std::string> splitCnf(const std::string& s) {
    char delimiter = '&';
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(s);
    while (std::getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

std::vector<std::string> splitDnf(const std::string& s) {
    char delimiter = '|';
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(s);
    while (std::getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

std::vector<std::string> splitImplicants(const std::string& input) {
    std::vector<std::string> result;
    std::string temp = "";
    for (int i = 0; i < input.size(); i++)
    {
        if (input[i] == '!')
        {
            temp += input[i];
            continue;
        }
        if (input[i] == '|' || input[i] == '(' || input[i] == ')' || input[i] == ' ' || input[i] == '&')
        {
            if (!temp.empty()) {
                result.push_back(temp);
                temp = "";
            }
            continue;
        }
        temp += input[i];
    }
    if (!temp.empty()) {
        result.push_back(temp);
    }
    return result;
}


std::unordered_set<std::string> setIntersection(const std::vector<std::string>& v1, const std::vector<std::string>& v2) {
    std::unordered_set<std::string> set1(v1.begin(), v1.end()), set2(v2.begin(), v2.end());
    std::unordered_set<std::string> intersection;
    for (const auto& item : set1) {
        if (set2.count(item)) {
            intersection.insert(item);
        }
    }
    return intersection;
}

bool AreLettersEqual(const vector<string>& lit1, const vector<string>& lit2) {
    vector<string> letters1, letters2;
    for (const string& literal : lit1) {
        letters1.push_back(literal.substr(literal.find_first_not_of('!')));
    }
    for (const string& literal : lit2) {
        letters2.push_back(literal.substr(literal.find_first_not_of('!')));
    }
    sort(letters1.begin(), letters1.end());
    sort(letters2.begin(), letters2.end());
    return letters1 == letters2;
}

bool isSubstringInOriginal(const std::string& subConstituent, const std::string& originalConstituent) {
    std::vector<std::string> subLiterals = splitImplicants(subConstituent);
    std::vector<std::string> originalLiterals = splitImplicants(originalConstituent);

    for (const std::string& literal : subLiterals) {
        if (std::find(originalLiterals.begin(), originalLiterals.end(), literal) == originalLiterals.end()) {
            return false;
        }
    }
    return true;
}



std::string minimizeCnf(const std::string& cnf) {
    vector<string> clauses = splitCnf(cnf);
    if (clauses.empty() || clauses.size() == 1) {
        return clauses.empty() ? "" : clauses[0];
    }
    string result;
    vector<vector<int>> matrix(clauses.size(), vector<int>(clauses[0].size(), 0));
    bool changed = true;
    int stage = 1;
    while (changed) {
        bool merged = false;
        vector<string> newClauses;
        changed = false;
        cout << "Iteration " << stage << ":\n";
        for (size_t i = 0; i < clauses.size(); ++i) {
            merged = false;
            for (size_t j = 0; j < clauses.size(); ++j) {
                if (i != j) {
                    vector<string> literals1 = splitImplicants(clauses[i]);
                    vector<string> literals2 = splitImplicants(clauses[j]);

                    vector<string> matchingLiterals;
                    if (AreLettersEqual(literals1, literals2)) {
                        for (const string& literal : literals1) {
                            if (find(literals2.begin(), literals2.end(), literal) != literals2.end()) {
                                matchingLiterals.push_back(literal);
                            }
                        }

                        if (matchingLiterals.size() >= literals1.size() - 1) {
                            string mergedClause = accumulate(matchingLiterals.begin() + 1, matchingLiterals.end(), matchingLiterals[0],
                                [](const string& a, const string& b) { return a + "|" + b; });
                            if (find(newClauses.begin(), newClauses.end(), mergedClause) == newClauses.end()) {
                                newClauses.push_back(mergedClause);
                                changed = true;
                                cout << "Merged: " << clauses[i] << " with " << clauses[j] << " in " << mergedClause << endl;
                            }
                            merged = true;
                        }
                    }
                }
            }
            if (!merged) {
                newClauses.push_back(clauses[i]);
            }
        }
        clauses = newClauses;
        ++stage;
    }

    for (size_t i = 0; i < clauses.size(); ++i) {
        result += "(" + clauses[i] + ")";
        if (i < clauses.size() - 1) {
            result += " & ";
        }
    }
    std::cout << result << std::endl;
    return result;
}

std::string minimizeDnf(const std::string& dnf) {
    vector<string> clauses = splitDnf(dnf);
    if (clauses.empty() || clauses.size() == 1) {
        return clauses.empty() ? "" : clauses[0];
    }
    string result;
    vector<vector<int>> matrix(clauses.size(), vector<int>(clauses[0].size(), 0));
    bool changed = true;
    int stage = 1;
    while (changed) {
        bool merged = false;
        vector<string> newClauses;
        changed = false;
        cout << "Iteration " << stage << ":\n";
        for (size_t i = 0; i < clauses.size(); ++i) {
            merged = false;
            for (size_t j = 0; j < clauses.size(); ++j) {
                if (i != j) {
                    vector<string> literals1 = splitImplicants(clauses[i]);
                    vector<string> literals2 = splitImplicants(clauses[j]);

                    vector<string> matchingLiterals;
                    if (AreLettersEqual(literals1, literals2)) {
                        for (const string& literal : literals1) {
                            if (find(literals2.begin(), literals2.end(), literal) != literals2.end()) {
                                matchingLiterals.push_back(literal);
                            }
                        }

                        if (matchingLiterals.size() >= literals1.size() - 1) {
                            string mergedClause = accumulate(matchingLiterals.begin() + 1, matchingLiterals.end(), matchingLiterals[0],
                                [](const string& a, const string& b) { return a + "&" + b; });
                            if (find(newClauses.begin(), newClauses.end(), mergedClause) == newClauses.end()) {
                                newClauses.push_back(mergedClause);
                                changed = true;
                                cout << "Merged: " << clauses[i] << " with " << clauses[j] << " in " << mergedClause << endl;
                            }
                            merged = true;
                        }
                    }
                }
            }
            if (!merged) {
                newClauses.push_back(clauses[i]);
            }
        }
        clauses = newClauses;
        ++stage;
    }

    for (size_t i = 0; i < clauses.size(); ++i) {
        result += "(" + clauses[i] + ")";
        if (i < clauses.size() - 1) {
            result += " | ";
        }
    }
    std::cout << result << std::endl;
    return result;
}

void minimizeCnfTable(const std::string& cnf, const std::string& origcnf)
{
    cout << "Table of Merged Clauses:\n";
    vector<string> originalClauses = splitCnf(origcnf);
    vector<string> clauses = splitCnf(cnf);
    cout << setw(15) << " ";
    for (const auto& clause : originalClauses) {
        cout << setw(15) << clause;
    }
    cout << endl;

    for (size_t i = 0; i < clauses.size(); ++i) {
        cout << setw(15) << clauses[i];
            for (size_t j = 0; j < originalClauses.size(); ++j) {
            if (originalClauses[j].find(clauses[i])) {
                bool containsSubstring = isSubstringInOriginal(clauses[i], originalClauses[j]);
                if (containsSubstring) {
                    cout << setw(13) << "X";
                }
                else {
                    cout << setw(13) << " ";
                }
            }
            else {
                cout << setw(13) << " ";
            }
        }
        cout << endl;
    }
}

void minimizeDnfTable(const std::string& dnf, const std::string& origdnf)
{
    cout << "Table of Merged Clauses:\n";
    vector<string> originalClauses = splitDnf(origdnf);
    vector<string> clauses = splitDnf(dnf);
    cout << setw(13) << "";
    for (const auto& clause : originalClauses) {
        cout << setw(13) << clause;
    }
    cout << endl;

    for (size_t i = 0; i < clauses.size(); ++i) {
        cout << setw(13) << clauses[i];
        for (size_t j = 0; j < originalClauses.size(); ++j) {
            if (originalClauses[j].find(clauses[i])) {
                bool containsSubstring = isSubstringInOriginal(clauses[i], originalClauses[j]);
                if (containsSubstring) {
                    cout << setw(13) << "X";
                }
                else {
                    cout << setw(13) << " ";
                }
            }
            else {
                cout << setw(13) << " ";
            }
        }
        cout << endl;
    }
}

std::string processDnf(const std::string& dnf) {
    vector<string> clauses = splitDnf(dnf);
    if (clauses.empty() || clauses.size() == 1) {
        return clauses.empty() ? "" : clauses[0];
    }
    string result;
    vector<vector<int>> matrix(clauses.size(), vector<int>(clauses[0].size(), 0));
    bool changed = true;
    int stage = 1;
    while (changed) {
        bool merged = false;
        vector<string> newClauses;
        changed = false;
        for (size_t i = 0; i < clauses.size(); ++i) {
            merged = false;
            for (size_t j = 0; j < clauses.size(); ++j) {
                if (i != j) {
                    vector<string> literals1 = splitImplicants(clauses[i]);
                    vector<string> literals2 = splitImplicants(clauses[j]);

                    vector<string> matchingLiterals;
                    if (AreLettersEqual(literals1, literals2)) {
                        for (const string& literal : literals1) {
                            if (find(literals2.begin(), literals2.end(), literal) != literals2.end()) {
                                matchingLiterals.push_back(literal);
                            }
                        }

                        if (matchingLiterals.size() >= literals1.size() - 1) {
                            string mergedClause = accumulate(matchingLiterals.begin() + 1, matchingLiterals.end(), matchingLiterals[0],
                                [](const string& a, const string& b) { return a + "&" + b; });
                            if (find(newClauses.begin(), newClauses.end(), mergedClause) == newClauses.end()) {
                                newClauses.push_back(mergedClause);
                                changed = true;
                            }
                            merged = true;
                        }
                    }
                }
            }
            if (!merged) {
                newClauses.push_back(clauses[i]);
            }
        }
        clauses = newClauses;
        ++stage;
    }

    for (size_t i = 0; i < clauses.size(); ++i) {
        result += "(" + clauses[i] + ")";
        if (i < clauses.size() - 1) {
            result += " | ";
        }
    }
    return result;
}

std::string processCnf(const std::string& cnf) {
    vector<string> clauses = splitCnf(cnf);
    if (clauses.empty() || clauses.size() == 1) {
        return clauses.empty() ? "" : clauses[0];
    }
    string result;
    vector<vector<int>> matrix(clauses.size(), vector<int>(clauses[0].size(), 0));
    bool changed = true;
    int stage = 1;
    while (changed) {
        bool merged = false;
        vector<string> newClauses;
        changed = false;
        for (size_t i = 0; i < clauses.size(); ++i) {
            merged = false;
            for (size_t j = 0; j < clauses.size(); ++j) {
                if (i != j) {
                    vector<string> literals1 = splitImplicants(clauses[i]);
                    vector<string> literals2 = splitImplicants(clauses[j]);

                    vector<string> matchingLiterals;
                    if (AreLettersEqual(literals1, literals2)) {
                        for (const string& literal : literals1) {
                            if (find(literals2.begin(), literals2.end(), literal) != literals2.end()) {
                                matchingLiterals.push_back(literal);
                            }
                        }

                        if (matchingLiterals.size() >= literals1.size() - 1) {
                            string mergedClause = accumulate(matchingLiterals.begin() + 1, matchingLiterals.end(), matchingLiterals[0],
                                [](const string& a, const string& b) { return a + "|" + b; });
                            if (find(newClauses.begin(), newClauses.end(), mergedClause) == newClauses.end()) {
                                newClauses.push_back(mergedClause);
                                changed = true;
                            }
                            merged = true;
                        }
                    }
                }
            }
            if (!merged) {
                newClauses.push_back(clauses[i]);
            }
        }
        clauses = newClauses;
        ++stage;
    }

    for (size_t i = 0; i < clauses.size(); ++i) {
        result += "(" + clauses[i] + ")";
        if (i < clauses.size() - 1) {
            result += " & ";
        }
    }
    return result;
}
string decimalToBinary(int n, int bits) {
    string binary;
    for (int i = bits - 1; i >= 0; i--) {
        int k = n >> i;
        if (k & 1)
            binary += '1';
        else
            binary += '0';
    }
    return binary;
}

int toGray(int number)
{
    return number ^ (number >> 1);
}

vector<string> extractVariablesSKNF(const string& sknf) {
    unordered_set<string> variables;
    string term;
    bool insideTerm = false;

    for (char ch : sknf) {
        if (ch == '(') {
            insideTerm = true;
            term.clear();
        }
        else if (ch == ')') {
            insideTerm = false;
            if (!term.empty()) {
                stringstream ss(term);
                string var;
                while (getline(ss, var, '|')) {
                    var.erase(remove(var.begin(), var.end(), ' '), var.end());
                    var.erase(remove(var.begin(), var.end(), '!'), var.end());
                    if (!var.empty()) {
                        variables.insert(var);
                    }
                }
            }
        }
        else if (insideTerm) {
            term += ch;
        }
    }

    return vector<string>(variables.begin(), variables.end());
}

vector<string> extractVariablesSDNF(const string& sknf) {
    unordered_set<string> variables;
    string term;
    bool insideTerm = false;

    for (char ch : sknf) {
        if (ch == '(') {
            insideTerm = true;
            term.clear();
        }
        else if (ch == ')') {
            insideTerm = false;
            if (!term.empty()) {
                stringstream ss(term);
                string var;
                while (getline(ss, var, '&')) {
                    var.erase(remove(var.begin(), var.end(), ' '), var.end());
                    var.erase(remove(var.begin(), var.end(), '!'), var.end());
                    if (!var.empty()) {
                        variables.insert(var);
                    }
                }
            }
        }
        else if (insideTerm) {
            term += ch;
        }
    }

    return vector<string>(variables.begin(), variables.end());
}

std::string minimizeSKNFbyKarnaugh(const std::string& sknf, const std::vector<int>& index) {
    std::vector<std::string> variables = extractVariablesSKNF(sknf);
    int n = variables.size();
    int rows, cols;

    if (n % 2 == 0) {
        rows = cols = 1 << (n / 2);
    }
    else {
        rows = 1 << (n / 2);
        cols = 1 << ((n + 1) / 2);
    }

    std::vector<std::vector<int>> karnaughMap(rows, std::vector<int>(cols, 0));
    for (int i = 0; i < index.size(); i++) {
        int row = toGray(i / cols);
        int col = toGray(i % cols);
        karnaughMap[row][col] = index[i];
    }

    cout << "Karnaugh Map (" << rows << "x" << cols << "):" << endl;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << karnaughMap[i][j] << "   ";
        }
        cout << endl;
        cout << endl;
    }
    std::vector<std::string> minimizedTerms;
    std::vector<std::vector<bool>> visited(rows, std::vector<bool>(cols, false));
    std::string minimizedSKNF = processCnf(sknf);
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (karnaughMap[r][c] == 0 && !visited[r][c]) {
                visited[r][c] = true;
                std::vector<std::pair<int, int>> stack = { {r, c} };
                std::vector<std::pair<int, int>> group = { {r, c} };
                int curR = stack.back().first;
                int curC = stack.back().second;
                while (!stack.empty()) {
                
                   // auto [curR, curC] = stack.back();

                    stack.pop_back();


                    // Check 4 neighbors (left, right, up, down)
                    /*for (auto [dr, dc] : std::vector<std::pair<int, int>>{ {0, 1}, {1, 0}, {0, -1}, {-1, 0} }) {

                        int newR = (curR + dr + rows) % rows;
                        int newC = (curC + dc + cols) % cols;
                        if (karnaughMap[newR][newC] == 0 && !visited[newR][newC]) {
                            visited[newR][newC] = true;
                            stack.emplace_back(newR, newC);
                            group.emplace_back(newR, newC);
                        }
                    }*/
                }

                std::string term;
                for (int i = 0; i < n; ++i) {
                    int mask = 1 << (n - i - 1);
                    bool same = true;
                    bool val = group[0].first & mask;
                    if (same) {
                        if (!term.empty()) {
                            term += " | ";
                        }
                        if (!(group[0].first & mask)) {
                            term += "!";
                        }
                        term += variables[i];
                    }
                }
                minimizedTerms.push_back("(" + term + ")");
            }
        }
    }

    std::string minimizeSKNF = minimizedTerms.empty() ? "1" : "";
    for (const auto& term : minimizedTerms) {
        if (!minimizeSKNF.empty()) {
            minimizeSKNF += " & ";
        }
        minimizeSKNF += term;
    }

    return minimizedSKNF;
}

std::string minimizeSDNFbyKarnaugh(const std::string& sdnf, const std::vector<int>& index) {
    std::vector<std::string> variables = extractVariablesSDNF(sdnf);
    int n = variables.size();
    int rows, cols;

    if (n % 2 == 0) {
        rows = cols = 1 << (n / 2);
    }
    else {
        rows = 1 << (n / 2);
        cols = 1 << ((n + 1) / 2);
    }

    std::vector<std::vector<int>> karnaughMap(rows, std::vector<int>(cols, 0));
    std::vector<std::string> minimizedTerms;
    std::vector<std::vector<bool>> visited(rows, std::vector<bool>(cols, false));
    std::string minimizedSDNF = processDnf(sdnf);
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (karnaughMap[r][c] == 0 && !visited[r][c]) {
                visited[r][c] = true;
                std::vector<std::pair<int, int>> stack = { {r, c} };
                std::vector<std::pair<int, int>> group = { {r, c} };
                int curR = stack.back().first;
                int curC = stack.back().second;
                while (!stack.empty()) {

                    // auto [curR, curC] = stack.back();

                    stack.pop_back();


                    // Check 4 neighbors (left, right, up, down)
                    /*for (auto [dr, dc] : std::vector<std::pair<int, int>>{ {0, 1}, {1, 0}, {0, -1}, {-1, 0} }) {

                        int newR = (curR + dr + rows) % rows;
                        int newC = (curC + dc + cols) % cols;
                        if (karnaughMap[newR][newC] == 0 && !visited[newR][newC]) {
                            visited[newR][newC] = true;
                            stack.emplace_back(newR, newC);
                            group.emplace_back(newR, newC);
                        }
                    }*/
                }

                std::string term;
                for (int i = 0; i < n; ++i) {
                    int mask = 1 << (n - i - 1);
                    bool same = true;
                    bool val = group[0].first & mask;
                    if (same) {
                        if (!term.empty()) {
                            term += " | ";
                        }
                        if (!(group[0].first & mask)) {
                            term += "!";
                        }
                        term += variables[i];
                    }
                }
                minimizedTerms.push_back("(" + term + ")");
            }
        }
    }

    std::string minimizeSDNF = minimizedTerms.empty() ? "1" : "";
    for (const auto& term : minimizedTerms) {
        if (!minimizeSDNF.empty()) {
            minimizeSDNF += " & ";
        }
        minimizeSDNF += term;
    }

    return minimizedSDNF;
}

int main()
{
    cout << "Input expression:" << endl;
    string expression = "(!(A&(!B))>C)";
    //cin >> expression;
 
    vector<int>index;
    set<char> expression_elem;
    vector<char> result;
    double decimal = 0;
    expression_elem = GetExpressionInfo(expression);
    result = PrintTable(expression, index);
    decimal = CountIndexNumber(decimal, index);
    string CNF = PrintCnf(result, expression_elem);
    string DNF = PrintDnf(result, expression_elem);
    cout << CNF << endl;
    cout << DNF << endl;
    string originalCNF = PrintCnf(result, expression_elem);
    string originalDNF = PrintDnf(result, expression_elem);
    cout << endl;
    cout << "CALCULATING METHOD:" << endl;
    
    cout << "CNF PROCESSING:" << endl;
    CNF = minimizeCnf(CNF);

    cout << endl;


    cout << "DNF PROCESSING:" << endl;
    DNF = minimizeDnf(DNF);

    cout << endl;
    cout << "TABLE-CALCULATING METHOD:" << endl;

    cout << "CNF PROCESSING:" << endl;
    minimizeCnfTable(CNF, originalCNF);

    cout << endl;


    cout << "DNF PROCESSING:" << endl;
    minimizeDnfTable(DNF, originalDNF);

    cout << endl;
    cout << "KARNAUGH METHOD PROCESSING:" << endl;
    CNF = minimizeSKNFbyKarnaugh(originalCNF, index);
    cout << "Minimized CNF by Karhaugh:" << CNF << endl;

    cout << endl;
    DNF = minimizeSDNFbyKarnaugh(originalDNF, index);
    cout << "Minimized DNF by Karhaugh:" << DNF << endl;
    return 0;
}