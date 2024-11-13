#include "WordPair.h"
#include "realization.h"
#include "../vocabularylib/UnitTest1/vocabulary.h"

Vocabulary::Vocabulary()
{
    root = NULL;
}

Vocabulary::~Vocabulary()
{
     Empty();
}

int Vocabulary::GetSize()
{
    return size;
}

string Vocabulary::operator[](const string& eng)
{
    return (*root)[eng];
}

void Vocabulary::Del(const string& eng, const string& rus)
{
    if (!root)
    {
        return;
    }
    root->Del(eng, rus);
    size--;
}

WordPair* Vocabulary::GetRoot()
{
    return this->root;
}

void Vocabulary::SwitchTransl(const string& eng, const string& rus)
{
    root->SwitchTransl(eng, rus);
}

Direction Vocabulary::InSubTree(const string& eng)
{
    return root->InSubTree(eng);
}

void Vocabulary::ReadFromFile(const string& path)
{
    ifstream fin;
    string eng = "", rus = "";
    fin.open(path);
    if (fin.is_open())
    {
        do
        {
            fin >> eng;
            fin >> rus;
            Push(eng, rus, InSubTree(eng));
        } while (!(fin.eof()) && eng != "");
    }
    fin.close();
}

void Vocabulary::Empty()
{
    this->root = NULL;
}

void Vocabulary::Push(const string& eng, const string& rus, Direction direction)
{
    if (direction == Direction::ROOT || this->root == NULL) {
        this->root = new WordPair(eng, rus);
        size++;
        return;
    }
    try {
        root = Push(root, eng, rus, InSubTree(eng));
        size++;
    }
    catch (const std::runtime_error& e)
    {
        cout << "Error: " << e.what() << endl;
    }
}

WordPair* Vocabulary::Push(WordPair* node, const string& eng, const string& rus, Direction direction)
{
    if (node == nullptr)
    {
        node = new WordPair(eng, rus);
        return node;
    }

    if ((node->GetEng() == eng) && (node->GetRus() == rus))
    {
        throw std::runtime_error("Element is already in the tree");
    }

    if (direction == Direction::LEFT)
    {
        node->SetLeft(Push(node->GetLeft(), eng, rus, direction));
    }
    else if (direction == Direction::RIGHT)
    {
        node->SetRight(Push(node->GetRight(), eng, rus, direction));
    }

    return node;
}
