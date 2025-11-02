#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main () {

    /*vector <string>fruits = {"Apple", "Banana", "Cherry"};

    for (string fruit : fruits) {
        cout << fruit << endl;
    }*/

    /*string word;
    word = "I can do Magic";

    string reverseWord = "";

    for (char c: string(word.rbegin(), word.rend())) {
        reverseWord += c;
    }

    cout << "original " << word << endl;

    cout << endl;

    cout << "changed " << reverseWord << endl;*/

    string friut, Fname;

    vector<string> Myarray = {"apple", "banana", "guava"};

    for (string fruits : Myarray) {
        cout << fruits << endl;
    }

    cout << "add a friut: ";
    cin.ignore();
    getline (cin, Fname);

    Myarray.push_back(Fname);

    for (string frutes : Myarray) {
        cout << frutes << endl;
    }

    return 0;
}