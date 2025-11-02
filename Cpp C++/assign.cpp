#include <iostream>
#include <limits> 

using namespace std;

unsigned long long fineOnDay(int N) {
    if (N < 1) return 0;
    
    unsigned long long fine = 10;

    for (int i = 2; i <= N; ++i) {
        if (fine > numeric_limits<unsigned long long>::max() / 2) {
            cout << "Overflow occurred at day " << i << endl;
            return 0;
        }
        fine *= 2;  
    }

    return fine;
}

int daysToReachFine(unsigned long long D) {
    if (D <= 10) return 1;
    
    unsigned long long fine = 10;
    int days = 1;

    while (fine < D) {
        if (fine > numeric_limits<unsigned long long>::max() / 2) {
            cout << "Overflow occurred before reaching R" << D << endl;
            return -1;
        }

        fine *= 2; 
        days++;
    }

    return days;
}

int main() {
    int N;
    unsigned long long D;

    cout << "Enter day N to calculate fine: ";
    cin >> N;

    if (N <= 0) {
        cout << "Day must be at least 1." << endl;
        return 1;
    }

    unsigned long long fine = fineOnDay(N);
    if (fine > 0)
        cout << "Fine on day " << N << " is R" << fine << endl;

    cout << "Enter fine amount D to find required number of days: ";
    cin >> D;

    int requiredDays = daysToReachFine(D);
    if (requiredDays != -1)
        cout << "Fine will reach at least R" << D << " on day " << requiredDays << endl;

    return 0;
}