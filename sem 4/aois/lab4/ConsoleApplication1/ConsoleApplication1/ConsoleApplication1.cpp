#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <stack>
#include <algorithm>
#include <sstream>
#include <numeric>
using namespace std;


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

string printSDNF(int h[16]) {
    std::ostringstream sdnf;
    for (int i = 0; i < 16; ++i) {
        if (h[i] == 1) {
            sdnf << "("
                << ((i < 8) ? "q3'" : "!q3'") << " & "
                << (((i / 4) % 2) ? "q2'" : "!q2'") << " & "
                << (((i / 2) % 2) ? "q1'" : "!q1'") << " & "
                << ((i % 2) ? "V" : "!V")
                << ") | ";
        }
    }
    string sdnf_str = sdnf.str();
    sdnf_str = sdnf_str.substr(0, sdnf_str.length() - 3);  // Удалить последний символ "|"
    return sdnf_str;
}

void printBinaryTable() {
    int h3[16], h2[16], h1[16];

    // Заполнение массивов h3, h2 и h1
    for (int i = 0; i < 16; ++i) {
        h3[i] = (i == 7 || i == 15) ? 1 : 0;
        h2[i] = (i == 3 || i == 7 || i == 11 || i == 15) ? 1 : 0;
        h1[i] = (i % 2 == 1) ? 1 : 0;
    }

    cout << endl;
    cout << "q3'\tq2'\tq1'\tV\th3\th2\th1\n";

    for (int i = 0; i < 16; ++i) {
        cout << (i < 8 ? 0 : 1) << "\t"
            << ((i / 4) % 2) << "\t"
            << ((i / 2) % 2) << "\t"
            << (i % 2) << "\t"
            << h3[i] << "\t"
            << h2[i] << "\t"
            << h1[i] << "\n";
    }

    string sdnf_h1 = printSDNF(h1);
    string sdnf_h2 = printSDNF(h2);
    string sdnf_h3 = printSDNF(h3);
    cout << endl;
    cout << "\nSDNF for h1:\n" << sdnf_h1 << endl;
    cout << "\nSDNF for h2:\n" << sdnf_h2<<endl;
    cout << "\nSDNF for h3:\n" << sdnf_h3<<endl;
    cout << endl;
    cout << "h1 SDNF PROCESSING" << endl;
    string minimized_h1 = minimizeDnf(sdnf_h1);
    cout << endl;
    cout << "h3 SDNF PROCESSING" << endl;
    string minimized_h2 = minimizeDnf(sdnf_h2);
    cout << endl;
    cout << "h3 SDNF PROCESSING" << endl;
    string minimized_h3 = minimizeDnf(sdnf_h3);

}

int main() {
    printBinaryTable();
    return 0;
}
