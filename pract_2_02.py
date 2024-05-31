# 2. Складіть чотири складних логічних вирази за допомогою 
# оператора and, два з яких повинні давати істину, а два інших 
# - хибність
a=10
b=10
result1 = (a > 0 and b > 0) #True
result2 = (a == 10 and b == 10) #True
result3 = (a < 0 and b > 0) #False
result4 = (a > 0 and b < 0) #False

print(result1,result2,result3,result4)
