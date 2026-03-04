# -------------------------- 1️⃣ What is a Dictionary? ------------------------------------

Python dictionary is a hash table.

Example:

d = {
    "name": "Siddesh",
    "age": 23
}

Internally:

key → hash → memory index → value
Example
d["age"]

Python steps:

hash("age")

find index

return value

That’s why lookup O(1).

2️⃣ Why Keys Must Be Immutable

Example:

d = {}

d[[1,2,3]] = "hello"

Error:

TypeError: unhashable type: 'list'

Because list change ho sakti hai:

[1,2,3] → [1,2,3,4]

Hash change ho jayega → dictionary break.

3️⃣ Valid Dictionary Keys

Valid:

int
str
tuple
frozenset
bool

Invalid:

list
set
dict
4️⃣ Dictionary Collision

Kabhi kabhi different keys ka hash same ho sakta hai.

Example conceptually:

hash("ab") = 100
hash("ba") = 100

Then collision hota hai.

Python internally open addressing use karta hai.

But interviewer rarely asks details beyond this.

5️⃣ Important Dictionary Operations
Operation	Complexity
lookup	O(1)
insert	O(1)
delete	O(1)
iterate	O(n)
6️⃣ Most Important Interview Pattern

Frequency Counting

Example:

arr = [1,1,2,3,3,3]

Solution:

freq = {}

for i in arr:
    freq[i] = freq.get(i,0) + 1

print(freq)

Output:

{1:2, 2:1, 3:3}
Better Way

Using Counter

from collections import Counter

Counter(arr)
7️⃣ Dictionary Trap (Interview Favorite)

Output?

d = {1: "a", 2: "b", 1: "c"}
print(d)

Answer:

{1: 'c', 2: 'b'}

Because key duplicate → last value overwrite.

8️⃣ Another Interview Trap
d = {}

d[True] = "yes"
d[1] = "no"

print(d)

Output?

{True: 'no'}

Because:

True == 1

Same hash.

9️⃣ Important Trick
d = {}

for i in range(5):
    d[i] = i*i

Result:

{0:0,1:1,2:4,3:9,4:16}
Now Your Turn (Real Interview Traps)

Predict outputs without running.

Question 1
d = {1: "a", 2: "b", 3: "c"}
print(d[1])
Question 2
d = {1: "a", 2: "b"}
d[3] = "c"
print(len(d))
Question 3 (Tricky)
d = {}

d[(1,2)] = "hello"
print(d)

Will this work or error?