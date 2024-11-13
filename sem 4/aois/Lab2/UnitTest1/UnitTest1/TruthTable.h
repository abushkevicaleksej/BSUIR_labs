#pragma once
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <stack>
#include <algorithm>
#include <iterator>
#include <cstdlib>
#include <cctype>
#include <cmath>

using namespace std;

int IsOperator(char c);

int IsBinaryOperator(char c);

int IsInvalidChar(char c);

int IsUpperAlpha(char c);

int Priority(char opr);

int IsValidExpression(const string& exp);

set<char> GetExpInfo(const string& exp);

string InfixToSuffix(const string& exp);

int Eval(const string& row, const string& suffix, const set<char>& exp_elem);

vector<char> PrintTable(const string& exp, vector<int>& index);

double CountIndexNumber(double& decimal, vector<int>& index);

int IsTautology(const vector<char>& result);

int IsContradiction(const vector<char>& result);

void PrintCnf(const vector<char>& result, const set<char>& exp_elem);

void PrintDnf(const vector<char>& result, const set<char>& exp_elem);