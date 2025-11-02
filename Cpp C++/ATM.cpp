#include <iostream>

using namespace std;

int main() {
	
	double balance=0, accountNumber, n=4; int menu;
	
	cout << "Welcome" << endl;
	
	cout << "account number: ";
	cin >> accountNumber;
	
	while (menu !=4) {
	    
    	cout << "menu" << endl;
    	
    	for (int i = 1; i <= n; i++) {
    		cout << i++ << "Check balance" << endl;
    		cout << i++ << "Withdraw" << endl;
    		cout << i++ << "Deposit" << endl;
    		cout << i++ << "exit" << endl;
    	};
    	
    	cout << "choose number: ";
    	cin >> menu;
    	
    	switch (menu) {
    	    case 1:
    	        cout << "Balance" << endl;
    	        cout << "R" << balance << endl;
    	    break;
    	    
    	    case 2:
    	        double withdrawal, available;
    	        
    	        cout << "Withdrawals"<< endl;
    	        
    	        cout << "Enter amount: R";
    	        cin >> withdrawal;
    	        
    	        if (withdrawal > balance) {
    	            cout << "insufficient balance" << endl;
    	        } else if (withdrawal <= 0) {
    	            cout << "invalid number" << endl;  
    	        } else {
    	            available = balance -= withdrawal;
    	            cout << "withdrawal successful" << endl;
    	            cout << "available balance: R" << available << endl;
    	        }
    	    break;
    	    
    	    case 3: 
    	        double deposit, total;
    	        
    	        cout << "deposit" << endl;
    	        
    	        cout << "Enter amount: R";
    	        cin >> deposit;
    	        
    	        if (deposit <= 0) {
    	            cout << "unavailable amount" << endl;
    	        } else {
    	            total = balance += deposit;
    	            
    	            cout << "Balance: R" << total << endl;
    	        }
    	   break;
    	   case 4: 
    	        cout << "Exitting..." << endl;
    	   break;
    	        
    	   default: 
    	   cout << "invalid choice" << endl;
    	}       
	}
	
	return 0;
	
}
