""" Set and Dictionaries Module"""
from random import randint
# """
# first = {1,2,3,4,5,5,3,2,1}
# first.add(6)
# first.update(["Tunde","Wale","Desmond"])
# # first.remove("Wale")
# # first.remove("Tunde")
# second = {3,4,7}
# first.symmetric_difference(second)
# # first.clear()
# print(first)
# """
 # Dictionaries
# peoples  = {
#     "person1": "Desmond",
#     "person2" : "Michael",
#     "person3" : "Adewale",
#     "person4" : "Favour"
#  }
#
#
#
#
# newdict = peoples.fromkeys(["admin1","admin2","admin3","admin4"])
# newdict.update({"admin1":"Code Warlock","admin2" : "Desmond","admin3":"Michael","admin4":"Me"})
#
#
# newdict["admin4"] = "Rita"
#
#
# no_of_admin = int(input("Enter the number of Administrators : "))
#
# for each in range(no_of_admin):
#     key = input("Enter the key : ")
#     val = input("Enter the value : ")
#     newdict[key] = val
# print(newdict)


eyeglasses = {
    "categories" : [
            {
            "id" : 1,
            "name" : "Ray-Ban",
            "product" :
                    {
                    "id" : randint(1,99990),"size" :
                        [{
                        "large" : f"${randint(100,300):,.2f}",
                        "medium" : f"${randint(100,300):,.2f}",
                        "small" : f"${randint(100,300):,.2f}"
                        }]
                    }
            },
            {
            "id" : 2,
            "name" : "ZENNI",
            "product" :
                    {
                    "id" : randint(1,99990),"size" :
                        [{
                        "large" : f"${randint(100,300):,.2f}",
                        "medium" : f"${randint(100,300):,.2f}",
                        "small" : f"${randint(100,300):,.2f}"
                        }]
                    }
            },
            {
            "id" : 3,
            "name" : "NIKE",
            "product" :
                    {
                    "id" : randint(1,99990),"size" :
                        [{
                        "large" : f"${randint(100,300):,.2f}",
                        "medium" : f"${randint(100,300):,.2f}",
                        "small" : f"${randint(100,300):,.2f}"
                        }]
                    }
            },
            {
            "id" : 4,
            "name" : "LACOSTE",
            "product" :
                    {
                    "id" : randint(1,99990),"size" :
                        [{
                        "large" : f"${randint(100,300):,.2f}",
                        "medium" : f"${randint(100,300):,.2f}",
                        "small" : f"${randint(100,300):,.2f}"
                        }]
                    }
            },
            {
            "id" : 5,
            "name" : "FRESHLOOK",
            "product" :
                    {
                    "id" : randint(1,99990),"size" :
                        [{
                        "large" : f"${randint(100,300):,.2f}",
                        "medium" : f"${randint(100,300):,.2f}",
                        "small" : f"${randint(100,300):,.2f}"
                        }]
                    }
            }
    ]
}
brands = []
for x in eyeglasses["categories"]:
    brands.append(x["name"])
print(f"""
                    ================================================================
                        {brands}
                        Select 1-5 to pick a brand
""")
select = int(input())
if select == 1:
    print(f"""
            ID  ========= > {eyeglasses["categories"][0]["id"]}
            BRAND  ========= > {eyeglasses["categories"][0]["name"]}
    """)










# COUNT = 1
# for key,value in peoples.items():
#     print(f"The key for the no {COUNT} item is ",key,"It's value is ",value)
#     COUNT += 1
#
#
# print(peoples.items())
#
# print(peoples.get("person5"))
