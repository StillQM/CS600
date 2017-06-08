# Calculate method definition
def getMonthlyUnpaidBalance(balance, minMonthlyPayFixed):
	return balance - minMonthlyPayFixed

def getUpdatedMonthlyBalance(balance, monthlyInterestRate):
	return balance + (monthlyInterestRate * balance)

# Test Cases
balance = 3329
annualInterestRate = .2

# Variables
monthlyInterestRate = .2 / 12
monthlyUnpaidBalance = getMonthlyUnpaidBalance(balance, monthlyInterestRate)
updatedBalance = getUpdatedMonthlyBalance(balance, monthlyInterestRate)

def getMinimumFixedMonthlyPay
