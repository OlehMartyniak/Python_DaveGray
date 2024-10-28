# Dictionaries (similar to objects in JS)


band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals = "Plant", guitar = "Page")

print(band)
print(band2)

# Access items
print(band["vocals"]) # Plant
print(band.get("guitar")) # Page

# list all keys
print(band.keys()) # dict_keys(['vocals', 'guitar']) 

# list all values
print(band.values()) # dict_values(['Plant', 'Page'])

# list of key / value pairs as tuples
print(band.items()) # dict_items([('vocals', 'Plant'), ('guitar', 'Page')])

# verify a key exists
print("guitar" in band) # True


# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band) # {'vocals': 'Coverdale', 'guitar': 'Page', 'bass': 'JPJ'}


# Remove items - pop() (removes both key and value)
band.pop("bass")
print(band) # {'vocals': 'Coverdale', 'guitar': 'Page'}


# Delete and clear
band["drums"] = "Bohnam"
del band["drums"]
print(band)

band2.clear()
print(band2)

# Copy dictionaries - copy() or dict() constructor

# band2 = band - wring way since you create a referrence

band2 = band.copy()
band2["drums"] = "Oleg"
print(band2)

band3 = dict(band)
print(band3)



# Nested dictionaries

member1 = {
    "vocals": "Waters",
    "instrument": "Gilmour"
}
member2 = {
    "vocals": "Lindemann",
    "instrument": "Kruspe"
}
rockBand = {
    "group1": member1,
    "group2": member2
}

print(rockBand)
# {'group1': {'vocals': 'Waters', 'instrument': 'Gilmour'}, 'group2': {'vocals': 'Lindemann', 'instrument': 'Kruspe'}}



# Sets
nums = {1, 2, 3, 4, 5}
nums2 = set((1,2,3))

print(nums) # {1, 2, 3, 4, 5}
print(nums2) # {1, 2, 3}

# Sets do not allow duplicates
nums3 = {1, 2, 2, 3}
print(nums3) # {1, 2, 3}


# check if a value is in the set
print(2 in nums3) # True
# but you cannot refer to an element in the set with an index position or a key

# Add a new element to a set
nums3.add(8)
print(nums3) # {8, 1, 2, 3}

# Add elements from one set to another
morenums = {11,12}
nums3.update(morenums)
print(nums3) # {1, 2, 3, 8, 11, 12}

# Merge two sets to create a new one
one = {1, 2, 3}
two = {4, 5, 6}

mynewset = one.union(two)
print(mynewset) # {1, 2, 3, 4, 5, 6}




