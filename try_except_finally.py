# Python 3: Deep Dive (Part 1 - Functional)

# try...except...finally - finally will run regardless at the end
print('Example 1:\n')
a = 10
b = 2

try:
    a / b
except ZeroDivisionError:
    print("Can't divide by zero.")
finally:
    print("Try/except/finally block complete.")

# continue in the except block will still allow the finally block to run. This is powerful for making a block always executes (closing a file, merging db, rollback a transaction, etc). If you take out the continue statement, the main loop block will still run because continue allowed us to break that iteration
# break - if you break instead of continue, the finally block will still run but the while loop will stop
print('\nExample 2:\n')

x = 0
y = 2

while x < 4:
    print('------------')
    x += 1
    y -= 1

    try:
        x / y
    except ZeroDivisionError:
        print(f'{x}, {y} - division by 0')
        continue
    finally:
        print(f'{x}, {y} - always executes in the finally block')
    
    print(f'{x}, {y} - in main loop')
else:
    print('Code executed without a zero division error')