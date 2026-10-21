class User:
    status = "Active"

    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def get_info(self):
        print("Username:", self.username)
        print("Email:", self.email)
        print("Age:", self.age)


user1 = User("natia", "natia@gmail.com", 37)
user2 = User("lile", "lile@gmail.com", 13)

user1.get_info()
print("Status:", user1.status)

print("----------------")

user2.get_info()
print("Status:", user2.status)
