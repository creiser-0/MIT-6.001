#problem set 1
#part c

while True:
    try:
        base_annual_salary = float(input("Enter your annual salary: "))
        break

    except ValueError:
        print("Please type float or integers only.")

#Fixed data
total_cost = 1000000
months = 36
semmi_annual_raise = .07
portion_down_payment = 0.25
monthly_r = .04 / 12
down_payment = total_cost * portion_down_payment

#Margin of error
epsilon = 100

#Bounds limits
initial_high = 10000
high = initial_high
low = 0

#Values for the while loop
current_savings = 0
steps = 0
portion_saved = (high + low) // 2

while abs(current_savings - down_payment) > epsilon:
    
    steps += 1
    current_savings = 0 
    annual_salary = base_annual_salary
    monthly_salary = annual_salary / 12
    monthly_saving = monthly_salary * (portion_saved / 10000)
    
    for month in range(1, months + 1):
        
        current_savings += (current_savings * monthly_r) + monthly_saving
        
        if (month % 6) == 0:
            annual_salary += (annual_salary * semmi_annual_raise)
            monthly_salary = annual_salary / 12
            monthly_saving = monthly_salary * (portion_saved / 10000)
            
    prev_portion_saved = portion_saved
    if current_savings < down_payment:
        low = portion_saved
    else:
        high = portion_saved
        
    portion_saved = round((high + low) / 2)
    
    if portion_saved == prev_portion_saved:
        break

if portion_saved == initial_high:
    print("The salary is not enough to acquiere this house in 3 years")
else:
    print("Best saving rate:", round((portion_saved / 10000), 4))
    print("Steps in the search :", steps)


#these problem took me a while to resolve only because i was trying to do all
#the steps separate from eachother instead of doing all in a big while loop.
        
        


            
            