//input field, table, and result div
const zarAmountInput = document.getElementById('zar-amount');
const resultDiv = document.getElementById('result');

// the conversion rates
const conversionRates = {
    USD: 18.24,
    EUR: 19.89,
    GBP: 23.60,
    JPY: 0.12,
    AUD: 12.22,
    CAD: 13.31,
    CHF: 20.56,
    CNY: 2.51,
    INR: 0.22,
    BRL: 3.37
};

// event listener to the convert button
document.getElementById('convert-btn').addEventListener('click', () => {
    // the entered amount in ZAR
    const zarAmount = parseFloat(zarAmountInput.value);
    
    // Check if the amount is valid
    if (isNaN(zarAmount)) {
        resultDiv.innerText = 'Please enter a valid amount';
        return;
    }
    
    // Convert the amount to each currency and display the results
    resultDiv.innerHTML = '';
    for (const [currency, rate] of Object.entries(conversionRates)) {
        const convertedAmount = zarAmount * rate;
        resultDiv.innerHTML += `${currency}: ${convertedAmount.toFixed(2)}<br>`;
    }
});
