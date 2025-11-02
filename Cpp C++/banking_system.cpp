#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;


double balance = 0;

void mainMenu () {
    cout << "Main Menu" << endl;
}


void intro () {

    while (true) {

        cout << "\t choose option" << endl;

        string option [4] = {"1. check balance", "2. withdraw", "3. deposit", "4. Exit"};

        for (string i : option) {
            cout << "\t\t" << i << "\n";
        }

        int num;

        cout << "\t Enter option: ";
        cin >> num;
        
        double amount;

        switch (num) {
            case 1:

                cout << "\t\t Check balance" << endl;
                cout << "\t Balance R" << balance << endl;

            break;

            case 2:

                while (true) {
                    cout << "\t\t Withdraw" << endl;
                    cout << "\t Balance R" << balance << endl;
                    cout << "\t Enter amount: R";
                    cin >> amount;

                    if (amount > balance) {
                        cout << "\t insuffient balance." << endl;
                        cout << "\t enter valid amount or enter 0 to exit" << endl;
                        continue;
                    } else if (amount == 0) {
                        break;
                    } else if (amount < balance) {
                        cout << "\t\t Withdrawwing..." << endl;
                        balance -= amount;
                        cout << "\n\t\t Done! \n\t balance R" << balance << endl;
                        break;
                    }
                }

            break;

            case 3:

                cout << "\t\t Deposit \n\t Enter 0 to exit" << endl;
                

                while (true) {
                    cout << "\tEnter amount R";
                    cin >> amount;

                    if (amount == 0) {
                        break;
                    } else if (amount < 5) {
                        cout << "unable to deposit, only allows deposit from R5+" << endl;
                        continue;
                    } else if (amount > 3000) {
                        cout << "Unable to deposit huge amount on the ATM, please go inside the bank" << endl;
                        break;
                    }else if (amount >= 5 || amount <= 3000) {
                        cout << "\t\t Depositting..." << endl;
                        balance += amount;
                        cout << "\t Balance R" << balance << endl;
                        break;
                    } 

                }

            break;

            case 4:
                cout << "\t\t\t GoodBye" << endl;    
                mainMenu();            
            break;


            default:
                cout << "\t unable to find the option number." << endl;
            break;

        }
    } return;
}

void Log () {

    int Pin;
    int pin = 1234;

    cout << "\t Pin: ";
    cin >> Pin;

    while (true) {
        
        if (Pin == pin) {
            intro();
        } else if (Pin == 0) {
            mainMenu();
            break;
        }
    }
    return;
}

void create () {

        cout << "\t\t\t Open Account" << endl;

        string name;
        int pin;

        cout << "\t Name: ";
        cin.ignore();
        getline (cin, name);
        

        while ( name.length() < 3 || name.length() > 9 ) {
            cout << "\t name is too long." << endl; 
            cout << "\t Name: ";
            cin.ignore();
            getline (cin, name);
        }
        
        cout << "\t Pin: ";
        cin >> pin;
            while ( pin < 1000 || pin > 9999 ) {
                cout << "\t Pin code must be 4 digits." << endl;
                cout << "\t Pin: ";
                cin >> pin;
                continue;
            }

        return;

        if (pin == 0) {
            mainMenu();
            return;
        }
                
}

void Process () {
    while (true) {

        string opt[] = {"1. Create Account", "2. Log In", "3. Exit"};
        for (string i : opt) {
            cout << "\t\t" << i << "\n";
        }

        int option;


        cout << "\t Enter option: ";
        cin >> option;
        cin.ignore();

        if (option == 1) {
            create();
            break;
        } else if (option == 2) {
               Log ();
        } else if (option == 3) {
            cout << "\t GoodBye" << endl;
            break;
        }
    }
}

int main () {

    cout << "\t\t\t Welcome to ALL BANK" << endl;
    cout << "\t\t insert 0 to go back to every menu." << endl;

    mainMenu();

    Process();

    return 0;

}