res = {
    "students": [],
    "active": [],
    "usernames": []
}
data = {
    "students":["Adam Levine", "Monica Muller", "John Deere", "John Deere", "John Deere", "John Deere"],
    "active":[True, False, True, True, True, True]
}
# key = []


# get a list of students only
s = data['students']

# access dictionary by key
for i in range(len(s)):
    if data['active'][i]:
        # split name
        res["students"].append(s[i])
        res["active"].append(data["active"][i])
        firstname, surname = s[i].split(' ')[0], s[i].split(' ')[1]
        #create unique id 
        user = f"{surname[:5].lower()}{firstname[:3].lower()}"
        
        # check if user already exists 
        if user in res["usernames"]:
            # take the last item from user and replace with increasing unqiue user
            count_dupl = i - res["usernames"].count(user)
            user = f"{user[0:7]}{count_dupl}"
        res["usernames"].append(user) 

        
print(res)   