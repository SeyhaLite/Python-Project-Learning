print("ម៉ាសុីនគិតលេខ : ")

#Type conversion: float()
num1 = float(input("សូមបញ្ជូលលេខ : "))
operator = input("សូមបញ្ជូលសញ្ញា : (+), (-), (/), (*), (%)")
num2 = float(input("សូមបញ្ជូលលេខ្ទង់ទី ២ : "))



if operator == "+":
  result = num1 + num2
elif operator == "-":
  result = num1 - num2
elif operator == "*":
  result = num1 * num2
elif operator == "/":
  if num2 != 0:
    result = num1 / num2
  else:
    #print("មិនអាចចែកនិង​ សូន្យ បានទេ")
    result = "មិនអាចចែកនិង​ សូន្យ បានទេ"

elif operator == "%":
  result = num1 % num2

#ប្រើ f-string
print(f"{num1} {operator} {num2} = {result}")
