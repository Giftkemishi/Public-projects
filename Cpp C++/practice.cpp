
//sequential search

#include <iostream>

using namespace std;

int search(int numbers[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (numbers[i] == target) {
            
            return i;
        }
    }
    return -1;
}

int main() {

    int numbers[5] = {10, 20, 30, 40, 50};
    int target;

    cout << "Number: ";
    cin >> target;

    int position = search(numbers, 5, target);

    if (position != -1) {
        cout << "Found at position: " << position << endl;
    } else {
        cout << "Not found!" << endl;
    }

}

// binary search

#include <iostream>

using namespace std;

int binarysearch(int numbers[], int size, int target) {

    int left = 0;
    int right = size -1;

    while (left <= right) {
        int mid = (left + right)/2;

        if (numbers[mid] == target) {
            return mid;
        } else if (numbers[mid] < target) {
            left = mid +1;
        } else {
            right = mid -1;
        }
    }
    return -1;

}

int main() {

    int numbers[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int size = 9;
    int target;

    cout << "Number";
    cin >> target;

    int position = binarysearch(numbers, size, target);

    if (position != -1) {
        cout << "found at: " << position << endl;
    } else {
        cout << "Not fount!" << endl;
    }

}


//hashing

#include <iostream>

using namespace std;

int main() {

    int table[10];

    for (int i = 0; i < 10; i++) {
        table[i] = -1;
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