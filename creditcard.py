#enter your initial Balance here
balance = 42
#to get balance from 0-12 month
for i in range(0,13):
	min_payment = balance*0.04
	#print('this year min_payment ', min_payment)
	unpaid = balance - min_payment
	#print('this year unpaid ', unpaid)
	interest = (0.2/12)*unpaid
	#print('this year interest ', interest)
	new_unpaid = unpaid + interest
	print("this year payment",i,new_unpaid)
	print("Remaining balance:", round(balance, 2))
	balance=new_unpaid
