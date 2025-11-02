#include <iostream>

using namespace std;

struct Node {
    int value;
    Node* next;
};

void printing(Node* sec) {
    Node* temp = sec;
    while (temp != nullptr) {
        cout << temp->value << " ";
        temp = temp->next;
    }
}

int main() {

Node* sec = new Node();
Node* third = new Node();
Node* four = new Node();

    sec->value = 20;
    sec->next = third;

    third->value = 30;
    third->next = four;

    four->value = 40;
    four->next = nullptr;

    cout << "Printing first node" << endl;
    printing(sec);
    cout << endl;

    Node* six = new Node();
    six->value = 60;
    six->next = nullptr;
    four->next  = six;

    cout << "After linking new node" << endl;
    printing(sec);
    cout << endl;

    Node* head = new Node();
    head->value = 10;
    head->next = nullptr;
    head->next = sec;

    cout << "Adding new node at the biginning." << endl;
    printing(head);
    cout << endl;

    Node* fifth = new Node();
    fifth->value = 50;
    fifth->next = nullptr;

    Node* temp = sec;
    while (temp != nullptr && temp->value != 40) {
        temp = temp->next;
    }
    if (temp != nullptr) {
        fifth->next = temp->next;
        temp->next = fifth;
    }

    cout << "adding node in the middle." << endl;
    printing(head);
    cout << endl;

    Node* sev = new Node();
    sev->value = 70;
    sev->next = nullptr;

    while (temp->next != nullptr) {
        temp = temp->next;
    }
    temp->next = sev;

    cout << "adding at the end." << endl;
    printing(head);
    cout << endl;






}