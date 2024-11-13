#include "HashTable.h"
//добавить rehash
int HashTable::hashFunction(string key) {
    int hash = 0;
    for (int i = 0; i < key.length(); ++i) {
        hash += (int)key[i];
    }
    return hash % table.size();
}

HashTable::HashTable() : table(1, nullptr) {

    for (int i = 0; i < table.size(); ++i) {
        table[i] = nullptr;
    }
}

void HashTable::insert(string key, string value) {
    int index = hashFunction(key);
    if (table[index] == nullptr) {
        table[index] = new Node(key, value);
    }
    else {
        cout << "Collision in " << key << endl;
        setCollision(true);
        Node* temporarVar = table[index];
        while (temporarVar->next != nullptr) {
            temporarVar = temporarVar->next;
        }
        temporarVar->next = new Node(key, value);
    }
}

void HashTable::remove(string key) {
    int index = hashFunction(key);
    if (table[index] == nullptr) {
        cout << "Element with key " << key << " not found." << endl;
        return;
    }
    Node* temporarVar = table[index];
    Node* prev = nullptr;
    while (temporarVar != nullptr && temporarVar->key != key) {
        prev = temporarVar;
        temporarVar = temporarVar->next;
    }
    if (temporarVar == nullptr) {
        cout << "Element with key " << key << " not found." << endl;
        return;
    }
    if (prev == nullptr) {
        table[index] = temporarVar->next;
    }
    else {
        prev->next = temporarVar->next;
    }
    delete temporarVar;
    cout << "Element with key " << key << " was deleted." << endl;
}

string HashTable::display() {
    string result;
    for (int i = 0; i < table.size(); ++i) {
        if (table[i] != nullptr) {
            Node* temporarVar = table[i];
            while (temporarVar != nullptr) {
                result += "Index: " + to_string(i) + ", Key: " + temporarVar->key + ", Definition: " + temporarVar->value + "\n";
                temporarVar = temporarVar->next;
            }
        }
    }
    return result;
}


void HashTable::update(string key, string newValue) {
    int index = hashFunction(key);
    if (table[index] == nullptr) {
        cout << "Element with key " << key << " not found." << endl;
        return;
    }
    Node* temporarVar = table[index];
    while (temporarVar != nullptr && temporarVar->key != key) {
        temporarVar = temporarVar->next;
    }
    if (temporarVar == nullptr) {
        cout << "Element with key " << key << " not found." << endl;
        return;
    }
    temporarVar->value = newValue;
    cout << "Element with key " << key << " was updated." << endl;
    setUpdateStatus(true);
}

bool HashTable::getUpdateStatus()
{
    return this->hasUpdated;
}

void HashTable::setUpdateStatus(bool updateStatus)
{
    this->hasUpdated = updateStatus;
}


int HashTable::get_size()
{
    return table.size();
}

int HashTable::getNumberOfEntries() {
    int count = 0;
    for (int i = 0; i < table.size(); ++i) {
        Node* temporarVar = table[i];
        while (temporarVar != nullptr) {
            count++;
            temporarVar = temporarVar->next;
        }
    }
    return count;
}


string HashTable::getValueByKey(string key) {
    int index = hashFunction(key);
    if (table[index] == nullptr) {
        cout << "Element with key " << key << " not found." << endl;
        return "";
    }
    Node* temporarVar = table[index];
    while (temporarVar != nullptr && temporarVar->key != key) {
        temporarVar = temporarVar->next;
    }
    if (temporarVar == nullptr) {
        cout << "Element with key " << key << " not found." << endl;
        return "";
    }
    return temporarVar->getValue();
}


bool HashTable::getCollision()
{
    return this->isCollision;
}

void HashTable::setCollision(bool collisionStatus)
{
    this->isCollision = collisionStatus;
}
