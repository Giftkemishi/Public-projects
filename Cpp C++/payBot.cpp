#include <iostream>
#include <cctype>
#include <string>
#include <vector>

using namespace std;

int Welcome() {

    cout << "Hello, My name is payBot. i officially welcome you to our store" << endl;

    return 0;

}

int pay() { 

    int pay, pin;

    cout << "\t 1. Card \n\t 2. Cash \n\t 3. Cancel" << endl;

    cout << "Enter number." << endl;
    cout << "How would you like to pay? ";
    cin >> pay;

    switch (pay) {
        case 1:

            cout << "Card." << endl;

            cout << "Enter card on the card slot" << endl;

            cout << "Enter pin: ";
            cin >> pin;

        break;

        case 2:

            cout << "Cash" << endl;

            cout << "Enter cash on the slot cash." << endl;
        
        break;

        case 3:

            cout << "Thank you for visiting our store." << endl;

        break;

        default:

            cout << "No number entered.";
    }

    while (true) {
        if (pay == 3) {

            cout << "Cancelled." << endl;
            break;
        }else {
            continue;
        }
    }

    return 0;

}

double rate() {

    int num, rateNum;

    vector<string> rates = {"bad", "upgrade", "good", "better", "perfect"};
    int number[5] = {1, 2, 3, 4, 5};

    for (int i = 0; i <5; i++) {
        cout << number [i] << ": " << rates[i] << endl;
    }

    return 0;

}


int main() {

    int rateNum;
    string donate, cat;

    Welcome();

    pay();

    cout << "Wanna donate a change for a cat? (y/n) ";
    cin >> donate;

if (donate == "y") {

    cout << rate() << endl;

    cout << "Rate me: ";
    cin >> rateNum;
    //toLowercase(rateNum);

    switch (rateNum) {
        case 1:

            cout << "We will do better next time." << endl;

        break;

        case 2:

            cout << "We will change what need to be changed." << endl;

        break;

        case 3:

            cout << "A good start to be doing better." << endl;

        break;

        case 4:

            cout << "Thank you for you feedback." << endl;

        break;

        case 5:

            cout << "You will totally get discount next time." << endl;

        break;

        default:
            cout << "No rate found." << endl;
    }

    } else if (donate == "n") {

        cout << "Are you sure you don't want to donate for the cat? (y/n) ";
        cin >> cat;
            
        if (cat == "y") {
            cout << "ohh... \n the cat just dies! \n it doesnt have 9 lives." << endl;

            cout << "Do you feel bad? (y/n) ";
            cin >> cat;

            if (cat == "y") {
                cout << "so you are heartless? (y/n) ";
                if (cat == "n") {
                    cout << "But you didn't want to save it. \n no one loves you right? (y/y) " << endl;
                    if (cat == "y") {

                        vector<string> rates = {"perfect", "perfect", "perfect", "perfect", "perfect"};
                        int number[5] = {1, 2, 3, 4, 5};

                        for (int i = 0; i <5; i++) {
                            cout << number [i] << ": " << rates[i] << endl;
                        }

                        cout << "rate us: ";
                        cin >> rateNum;

                    }else {}
                    
                } else {
                    cout << "no one loves you. for real." << endl;
                }

            } else {
                cout << "You are just evil." << endl;
            }

        } else {
            cout << "Then why haven't you donated yet!? \n don't even answer it just died." << endl;
        }

    } else {
        cout << "so, you are evil? dont answer, we got our answer." << endl;
}

return 0;
}