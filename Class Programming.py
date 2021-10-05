#!/usr/bin/env python
# coding: utf-8

# In[65]:


import random
class Book:
    __file = []
    def __init__(self,title,price):
        self.bk_title = title
        self.id = random.randint(1,10000)
        self.views = 0
        self.price = price
        self.file ="".join([x[0] for x in title.split()]) + ".txt"
        Book._file.append(self.file)
    def create_file(self):
        raise NotImplementedError("Only Admins have this access")
#     def __del__(self):
#         del self.file
#         del self


# In[66]:


#Inheritance
#PolyMorphism
#Abstraction
#Data Encapsulation


# In[68]:


Book._Book__file


# In[52]:


newBook = Book("NEW",90000)


# In[53]:


newBook.create_file()


# In[54]:


class Admin(Book):
    _password = 123456
    def __init__(self,title,price):
        super().__init__(title,price)
        password = int(input("Enter Admin password : "))
        if password == Admin._password:
            self.password = password
        else:
            raise NotImplementedError("You don't have access to this class")
    def create_file(self):
        content = input("Paste your book's content : \n")
        with open(self.file,"w") as f:
            f.write(f"""{content}""")
    def read(self):
        with open(self.file,"r") as f:
            print(f.read())
        self.views += 1


# In[55]:


class Regular(Book):
    def __init__(self,name,price):
        super().__init__(price)
    def read(self):
        bk_read = input("What book do you want to read : ")
        with open(Book._file,"r") as f:
            print(f.read())
        self.views += 1


# In[59]:


reg = Regular(90334)


# In[56]:


admin = Admin("LMVFKSBVKM M FBVND ",345434)


# In[57]:


admin2 = Admin("bhgauhfus hbvsjhbh bfihifb",23452352)


# In[58]:


admin._


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[60]:


reg._file


# In[19]:


new_admin = Admin("Lord of the Flies",1500)


# In[20]:


new_admin.create_file()


# In[27]:


class Animal:
    def __init__(self,name):
        self.name = name
    def mksound(self):
        print("I am an animal!!!")


# In[ ]:





# In[34]:


Max.mksound()


# In[31]:


Max = Dog("Max","German Shepherd")


# In[30]:


felix = Cat("felix","yoruba")


# In[29]:


any_animal = Animal("Duck")


# In[28]:


class Dog(Animal):
    def __init__(self,name,specie):
        super().__init__(name)
        self.specie = specie
    def mksound(self):
        print("Woof : I am a Dog!!!")
class Cat(Animal):
    def __init__(self,name,specie):
        super().__init__(name)
        self.specie = specie
    def mksound(self):
        print("Meow : I am a Cat!!!")

