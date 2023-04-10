#problem set 1
#part b

total_cost = float(input("Enter the cost of your dream house: "))
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary, as a decimal: "))
semmi_annual_raise = float(input("Enter the semmi-anual raise, as a decimal: "))
portion_down_payment = 0.25
current_savings = 0
r = .04
down_payment = total_cost * portion_down_payment

months = 0

def salary_increase(salary, increase, months):
    if months == 0 or (months % 6) != 0:
        return salary
    else:
        salary = salary + (salary * increase)
        return salary
    
def invest_monthly(invest, rate):
    profit = (invest * rate) / 12
    return profit


while current_savings < down_payment:
    annual_salary = (salary_increase(annual_salary, semmi_annual_raise, months))
    monthly_salary = annual_salary / 12
    monthly_saving = monthly_salary * portion_saved
    current_savings += (monthly_saving + invest_monthly(current_savings, r))
    months += 1
print("Number of months:", months)