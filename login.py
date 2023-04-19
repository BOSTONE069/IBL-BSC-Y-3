class Login():
    def __init__(self, username, password=None):
        self.username = username
        self.password = password

class User(Login):
    def __init__(self, username, password, first_name, last_name, email_address):
        super().__init__(username, password)
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

    def __str__(self):
        return f"Your name is {self.first_name} {self.last_name} and your username is {self.username} and password is {self.password} and the email address is {self.email_address}"

def  main():
    user = User("Bostone001", "TUK001", "Ochieng", "Kevin", "bostone@gmail.com")
    print(user)

if __name__ == '__main__':
    main()