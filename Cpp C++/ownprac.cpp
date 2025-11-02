#include <iostream>

using namespace std;

int main() {

    int table[10];

    for (int i = 0; i < 10; i++) {
        table[1] = -1;
    }

    int numbers[] = {1, 2, 3, 4, 5};
    int size;

    for (int i = 0; i < size; i++) {
        int number = numbers[i];
        int position = number % 10;
        table[position] = number;

    }

    cout << "table";

    for (int i = 0; i< 10; i++) {
        cout << i << " : " << table[i] << endl;
    }

}