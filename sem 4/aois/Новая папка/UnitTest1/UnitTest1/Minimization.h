
#pragma once
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <stack>
#include <iomanip>
#include <algorithm>
#include <iterator>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <unordered_set>
#include <numeric>

using namespace std;

int IsOperator(char c);

int IsBinaryOperator(char c);

int IsInvalidChar(char c);

int IsUpperAlpha(char c);

int Priority(char opr);

int IsValidExpression(const string& exp);

string InfixToSuffix(const string& exp);

int Eval(const string& row, const string& suffix, const set<char>& exp_elem);

vector<char> PrintTable(const string& exp, vector<int>& index);

double CountIndexNumber(double& decimal, vector<int>& index);

int IsTautology(const vector<char>& result);

int IsContradiction(const vector<char>& result);

set<char> GetExpressionInfo(const string& expression);

string PrintCnf(const vector<char>& result, const set<char>& exp_elem);

string PrintDnf(const vector<char>& result, const set<char>& exp_elem);

std::vector<std::string> splitCnf(const std::string& s);

std::vector<std::string> splitDnf(const std::string& s);

std::vector<std::string> splitImplicants(const std::string& input);

std::unordered_set<std::string> setIntersection(const std::vector<std::string>& v1, const std::vector<std::string>& v2);

bool AreLettersEqual(const vector<string>& lit1, const vector<string>& lit2);

bool isSubstringInOriginal(const std::string& subConstituent, const std::string& originalConstituent);

std::string minimizeCnf(const std::string& cnf);

string minimizeDnf(const std::string& dnf);

void minimizeCnfTable(const std::string& cnf, const std::string& origcnf);

void minimizeDnfTable(const std::string& dnf, const std::string& origdnf);

string processDnf(const std::string& dnf);

string processCnf(const std::string& cnf);

string decimalToBinary(int n, int bits);

int toGray(int number);

vector<string> extractVariablesSKNF(const string& sknf);

vector<string> extractVariablesSDNF(const string& sknf);

string minimizeSKNFbyKarnaugh(const std::string& sknf, const std::vector<int>& index);

string minimizeSDNFbyKarnaugh(const std::string& sdnf, const std::vector<int>& index);

