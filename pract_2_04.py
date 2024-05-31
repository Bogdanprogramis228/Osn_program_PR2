# 4. Спробуйте використати в складних логічних виразах 
# роботу зі змінними рядкового типу.

str1 = "hello"
str2 = "world"

result9 = (str1 == "hello" and str2 == "world")  # True
result10 = (str1 == "hello" or str2 == "python") # True

result11 = (str1 == "hi" and str2 == "world")   # False
result12 = (str1 == "hi" or str2 == "python")   # False

print(result9,result10,result11,result12)