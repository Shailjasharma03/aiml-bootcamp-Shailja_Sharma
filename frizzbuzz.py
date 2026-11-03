# for i in range(1,101):
#     if i%105==0:
#         print("FizzBuzzBazz")
#     elif i%35==0:
#         print("BuzzBazz")
#     elif i%21==0:
#         print("FizzBazz")
#     elif i%15==0:
#         print("FizzBuzz")
#     elif i%7==0:
#         print("Bazz")
#     elif i%5==0:
#         print("Buzz")
#     elif i%3==0:
#         print("Fizz")
#     else:
#         print(i)

def fizzbuzzbazz(n: int) -> str:
    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    if n % 7 == 0:
        result += "Bazz"
    return result or str(n)  #Return the FizzBuzzBazz word for n, or n itself if no rule applies.

for i in range(1, 101):
    print(fizzbuzzbazz(i))

