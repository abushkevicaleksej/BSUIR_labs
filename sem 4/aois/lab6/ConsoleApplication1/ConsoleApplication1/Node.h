#pragma once
#include <string>
#include <iostream>
#include <vector>
using namespace std;

class Node {
public:
    string key;
    string value;
    Node* next;

    Node(string key, string value) {
        this->key = key;
        this->value = value;
        this->next = nullptr;
    }



    string getValue() {
        return this->value;
    }

};

