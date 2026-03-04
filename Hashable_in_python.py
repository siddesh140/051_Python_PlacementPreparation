--------------------------- Hashable in Python ---------------------------------

Hashable means an object can be used as a dictionary key or added to a set.

Simple Explanation:
A hashable object has a hash value that never changes and can be used to uniquely identify it.

Python
# Hashable - can be dictionary key
dict = {1: 'one', 'two': 2, (1, 2): 'tuple'}  # ✅ Works

# Hashable - can be added to set
my_set = {1, 'hello', (3, 4)}  # ✅ Works
Why Dictionary Needs Hashable Keys?
Python
# Dictionaries use hash values to find values quickly (O(1))
person = {'name': 'Alice', 'age': 25}

# When you do person['name'], Python:
# 1. Calculates hash of 'name'
# 2. Uses that hash to find the value instantly

print(hash('name'))  # Output: -8835372099674341033 (consistent)
Same key always gives same hash:

Python
print(hash('hello'))  # -2642124086249066823
print(hash('hello'))  # -2642124086249066823 (same!)
Hashable vs Non-Hashable:
✅ HASHABLE (Can be dict keys & in sets)
Python
# Integers
d = {1: 'one', 2: 'two'}  # ✅

# Strings
d = {'name': 'Alice', 'age': '25'}  # ✅

# Tuples (if they contain hashable items)
d = {(1, 2): 'coordinates', (3, 4): 'point'}  # ✅

# Booleans
d = {True: 'yes', False: 'no'}  # ✅

# None
d = {None: 'nothing'}  # ✅

# Check hash
print(hash(5))        # ✅ Works
print(hash('hello'))  # ✅ Works
print(hash((1, 2)))   # ✅ Works
❌ NON-HASHABLE (Cannot be dict keys or in sets)
Python
# Lists - mutable, can change
d = {[1, 2]: 'list'}  # ❌ TypeError: unhashable type: 'list'

# Dictionaries - mutable
d = {{'a': 1}: 'dict'}  # ❌ TypeError: unhashable type: 'dict'

# Sets - mutable
d = {{1, 2}: 'set'}  # ❌ TypeError: unhashable type: 'set'

# Check hash
print(hash([1, 2]))   # ❌ TypeError: unhashable type: 'list'
print(hash({'a': 1})) # ❌ TypeError: unhashable type: 'dict'
Why Lists/Dicts are Non-Hashable:
Python
# Lists can CHANGE - hash would become unreliable
my_list = [1, 2, 3]
my_dict = {my_list: 'value'}  # ❌ Can't do this

# If we could, what happens when list changes?
my_list.append(4)  # Now it's [1, 2, 3, 4]
# Hash would be invalid - dictionary lookup would break! 💥

# Tuples are IMMUTABLE - hash never changes
my_tuple = (1, 2, 3)
my_dict = {my_tuple: 'value'}  # ✅ Safe!
my_tuple[0] = 5  # ❌ Can't modify anyway - TypeError
Rule of Thumb:
Immutable = Hashable

Python
Hashable:     int, str, tuple, bool, None, frozenset
Non-hashable: list, dict, set
Why? Because if an object can't change, its hash will always be the same, making it safe for dictionary keys and sets.

Real Example:
Python
# ✅ This works - tuple is hashable
locations = {
    (40.7128, -74.0060): 'New York',
    (51.5074, -0.1278): 'London',
    (35.6762, 139.6503): 'Tokyo'
}
print(locations[(40.7128, -74.0060)])  # New York ✅

# ❌ This doesn't work - list is not hashable
locations = {
    [40.7128, -74.0060]: 'New York'  # ❌ TypeError
}
Interview Question Answers:
Q: Why can't lists be dictionary keys? A: Because lists are mutable (can change), so their hash value would become unreliable. Dictionaries rely on hash values being constant for fast lookups.

Q: Can you have a tuple inside a tuple as a key? A: Yes! {(1, (2, 3)): 'value'} ✅ - tuples are immutable and hashable.

Q: What about a tuple containing a list? A: No! {(1, [2, 3]): 'value'} ❌ - the inner list is non-hashable, making the whole tuple non-hashable.

Quick Test:
Python
# What's hashable?
print(hash(123))           # ✅
print(hash('hello'))       # ✅
print(hash((1, 2, 3)))     # ✅
print(hash([1, 2, 3]))     # ❌ TypeError
print(hash({'a': 1}))      # ❌ TypeError
print(hash({1, 2, 3}))     # ❌ TypeError
Key Point: Hashability = Can be a dictionary key or element in a set 🎯