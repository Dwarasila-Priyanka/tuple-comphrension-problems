#1. l = 5200  o/p : 10 500 notes 1 200 notes
amount = 5200
notes_500 = amount // 500
amount %= 500
notes_200 = amount // 200
amount %= 200
if notes_500 > 0:
    print(f"{notes_500} 500 notes")
if notes_200 > 0:
    print(f"{notes_200} 200 notes")

#  2. p = ["Python", "java", "c++"]   # print only python from the list using tuple comprehension

v = ['python', 'java', 'c++']
result = tuple(x for x in v if x == 'python')
print(result)

# 3. print prime numbers between 10 to 20 using tuple comprehension
primes = tuple(x for x in range(10, 21) if all(x % i != 0 for i in range(2, x)))
print(primes)

# 4. given a string "abcd" create a tuple of ASCII value of each character

s = "abcd"
ascii_values = tuple(ord(i) for i in s)
print(ascii_values)

#  5. l= [1,2,3,4,5,6]       o/p: [[1,2],[3,4],[5,6]]

l = [1, 2, 3, 4, 5, 6]
result = [l[i:i+2] for i in range(0, len(l), 2)]
print(result)



