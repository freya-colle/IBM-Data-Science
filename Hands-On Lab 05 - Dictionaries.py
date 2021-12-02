"""
Week 2:
Hands-On Lab 5: Dictionaries
"""

'''
Dictionaries: {"key": value} IMMUTABLE
'''
#Create my first Dict
Dict = {"key2":2, "key3":3, "key4":4, (3,9):5}
print(Dict)
print('Access to the value by the key:\t', Dict["key2"])
print(Dict[(3,9)])

release_year_dict = {"Thriller": "1982", "Back in Black": "1980",
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992",
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976",
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
print(release_year_dict)
print('Get value by key: ', release_year_dict['Bat Out of Hell'])
print("KeyError: release_year_dict['1980']")
print('Get all the keys: ', release_year_dict.keys()) #keys NOT key
print('Get all the values: ', release_year_dict.values())

#ADD values to the dictionary
release_year_dict['Freya'] = '1996'
print('Dict after appending a value:\t',release_year_dict)

#DELETE an entry
del(release_year_dict['Thriller'])
print('Dict after deleting an entry:\t',release_year_dict)

#VERIFY the key is in the dictionary
print('Checking if the key -The Bodyguard is in the dictionary:\t','The Bodyguard' in release_year_dict)







