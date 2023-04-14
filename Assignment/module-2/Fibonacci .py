n = int(input("Enter the number of terms: "))

num1, num2 = 0, 1
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(num1)
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(num1)
       nth = num1 + num2
   
       num1 = num2
       num2 = nth
