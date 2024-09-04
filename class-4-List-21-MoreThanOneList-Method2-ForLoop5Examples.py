

fruits = ["apple", "banana", "cherry", "kiwi", "mango", "Gava", "beryy"]

newlist = [x for x in fruits if "a" in x]   # latter "a" in each value of list fruits

print(newlist)


# 5 Examples

# Example 1 Linear search
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# Example 2 sorting
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

# Example 3
newlist = [x for x in range(10)]
print(newlist)

# Example 4
newlist = [x for x in range(10) if x < 5]
print(newlist)

# Example 5
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]        # what is the difference between 'hello' and "hello"  ??
print(newlist)

