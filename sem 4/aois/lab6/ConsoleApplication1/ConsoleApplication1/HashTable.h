#pragma once
#include "Node.h"

class HashTable {
private:
    std::vector<Node*> table;

    bool isCollision = false;

    bool hasUpdated = false;

    int hashFunction(string key);

public:
    HashTable();

    void insert(string key, string value);

    void remove(string key);

    string display();

    void update(string key, string value);

    int get_size();

    string getValueByKey(string value);

    bool getCollision();

    void setCollision(bool collisionStatus);

    int getNumberOfEntries();

    bool getUpdateStatus();

    void setUpdateStatus(bool updateStatus);
};
