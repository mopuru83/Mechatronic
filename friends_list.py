#!/usr/bin/env python

friends = ["Jada", "Lesley", "Moses", "Emmanuel"]    

for friend in friends:
    print(friend)

new_friends = ["Riak", "Grace", "John"]

friends.append("Bob")

friends.extend(new_friends)

#friends.append([]"James", "Jack" , "Mercy]")

print(friends)
print(len(friends))