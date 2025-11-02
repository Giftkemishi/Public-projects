#include <iostream>
#include <string>

using namespace std;

int main() {
    
    cout << "affordable cars" << endl;
    
    char name [10];
    
    cout << "user info" << endl;
    
    cout << "enter name ";
    cin >> name;
    
    double salary;
    
    cout << "welcome customer" << endl;
    
    cout << "please enter your annual salary ";
    cin >> salary;
    
    double monthly;
    monthly = salary / 12;
    
    cout << "your monthly salary is R" << monthly << endl;
    
    cout << "please wait..." << endl;
    
    double polo = 3400, bmw = 15000, benz = 9000, mazda = 3000, ford = 4500;
    
    double installment;
    installment = monthly *  25 / 100;
    cout << "Your install me will be R" << installment << endl;
    
    if (installment >= 2500 && installment <= 5000){
        cout << "visit your nearest branch for polo negotiations" << endl;
    }else if (installment >= 5000 && installment <= 7000){
        cout << "no car found for that amaount" << endl;
    }else if (installment >= 7100 && installment <= 12000){
        cout << "visit your nearest branch to negotiate for Benz" << endl;
    }else if (installment >= 12200 && installment <= 20000){
        cout << "visit your nearest branch for negotiation for Bmw or other vehicles" << endl;
    }else{
        cout << "sorry we don't have any vehicle for you. " << endl;
    }
    
    string service;
    
    cout << "did you enjoy our service? y/n? " ;
    cin >> service;
    
    if (service == "y"){
        double rating;
        cout << "rate us 1 to 5: ";
        cin >> rating;
    
        if (rating >= 1 && rating <= 3){
            cout << "thanks for your feedback, we will do better";
        }else if (rating >= 4 && rating <= 5){
            cout << "thanks for the feedback, it means alot!";
        }else{
            cout << "you did not rate";
        }
    }else if (service == "n"){
        cout << "next time, visit when you have money";
    }
    
}
