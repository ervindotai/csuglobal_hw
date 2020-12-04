budget = input('Enter amount budgeted for a month: ')
budget = int(budget)
print('Type 0 to finish entering expenses')
print()

total = []
loop = 1

while loop == 1:
  i = input('Enter each of your expenses for the month: ')
  i = float(i)
  total.append(i)
  if i == 0:
    break

expenses = sum(total)

print()
print('Budget: ', budget)
print('Expenses: ', expenses)
print()

if expenses > budget:
  overbudget = expenses - budget
  print('You were over budget by: ', overbudget)

if expenses < budget:
  underbudget = budget - expenses
  print('You were underbudget by: ', underbudget)

if expenses == budget: 
  print('Your budget was equal to expenses!')

""""""
#Running the script, prints:
Enter amount budgeted for a month: 1000
Type 0 to finish entering expenses

Enter each of your expenses for the month: 550
Enter each of your expenses for the month: 250
Enter each of your expenses for the month: 250
Enter each of your expenses for the month: 100
Enter each of your expenses for the month: 0

Budget:  1000
Expenses:  1150.0

You were over budget by:  150.0
""""""
