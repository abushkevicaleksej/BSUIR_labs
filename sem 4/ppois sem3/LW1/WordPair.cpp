#include "WordPair.h"
#include "realization.h"
#include "../vocabularylib/UnitTest1/vocabulary.h"

string WordPair::GetEng()
{
    return this->eng;
}

string WordPair::GetRus()
{
    return this->rus;
}

WordPair* WordPair::GetLeft()
{
    return this->left;
}

WordPair* WordPair::GetRight()
{
    return this->right;
}

void WordPair::SetLeft(WordPair* left)
{
    this->left = left;
}

void WordPair::SetRight(WordPair* right)
{
    this->right = right;
}

Direction WordPair::InSubTree(const string& eng)
{
    if (!this)
    {
        return Direction::ROOT;
    }
    if (eng < this->GetEng())
    {
        return Direction::LEFT;
    }
    else
    {
        return Direction::RIGHT;
    }
}

WordPair::WordPair(const string& eng, const string& rus)
{
    this->eng = eng;
    this->rus = rus;
}

void WordPair::Del(const string& eng, const string& rus) {
    WordPair* node = this;
    if (node == nullptr) {
        return;
    }
    if (eng < node->eng) {
        node->left->Del(eng, rus);
    }
    else if (eng > node->eng) {
        node->right->Del(eng, rus);
    }
    else {
        if (node->left == nullptr) {
            WordPair* middle_node = node->right;
            delete node;
            node = middle_node;
        }
        else if (node->right == nullptr) {
            WordPair* middle_node = node->left;
            delete node;
            node = middle_node;
        }
        else {
            WordPair* middle_node = node->right->FindMinNode();
            node->eng = middle_node->eng;
            node->rus = middle_node->rus;
            node->right->Del(middle_node->eng, middle_node->rus);
        }
    }
}

WordPair* WordPair::FindMinNode() {
    if (this->left == nullptr) {
        return this;
    }
    return this->left->FindMinNode();
}


WordPair* WordPair::Finder(const string& eng) {
    if (this->eng == eng)
    {
        return this;
    }
    if (eng < this->eng)
    {
        return this->left->Finder(eng);
    }
    else
    {
        return this->right->Finder(eng);
    }
}

string WordPair::operator[](const string& eng)
{
    return Finder(eng)->rus;
}


void WordPair::ReadFromFile(const string& path)
{
    this->ReadFromFile(path);
}

void WordPair::SwitchTransl(const string& eng, const string& rus)
{
    Finder(eng)->rus = rus;
}

