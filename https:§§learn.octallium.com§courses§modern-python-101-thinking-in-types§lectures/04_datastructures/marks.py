marks = {}

# k,v pairs

marks = {
    "math": 80,
    "scienze" : 82,
    "english" : 55
}

for sub in marks.keys():
    print(sub)
    
for v in marks.values():
    print(v)
    
# update values
marks["english"]= 70

# add new pair
marks["geo"] = 60

math_score = marks.get("math")
unknows_score = marks.get("italian")

# def type
marks2: dict[str, int] = {}

# delete 
del marks["geo"]
print(marks)

# safe del
try:
    del marks['italian']
except KeyError:
    pass
print(marks)