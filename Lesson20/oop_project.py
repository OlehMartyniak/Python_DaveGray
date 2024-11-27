from bank_accs import *

Oleg = BankAccount(2000, "Oleg")
Anna = BankAccount(1000, "Anna")

Oleg.getBalance()
Anna.getBalance()

Oleg.deposit(300)

Oleg.withdraw(5000)
Oleg.withdraw(200)

Oleg.transfer(10000, Anna)
Oleg.transfer(500, Anna)



Jim = InterestRewardAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Oleg)



Kyle = SavingsAccount(1000, "Kyle")

Kyle.getBalance()

Kyle.deposit(300)

Kyle.transfer(10000, Anna)

Kyle.transfer(600, Anna)
