# verifies passwords using SHA256 hashing without storing actual passwords, ensuring secure login.
from hashlib import sha256

def hash_password(pwd):
    return sha256(pwd.encode()).hexdigest()

def login(email, logins, pwd):
    return logins[email] == hash_password(pwd)

def main():
    logins = {
        "a@gmail.com": hash_password("apple"),
        "b@gmail.com": hash_password("banana")
    }

    print(login("a@gmail.com", logins, "apple"))   # True
    print(login("b@gmail.com", logins, "orange"))  # False

if __name__ == '__main__':
    main()
