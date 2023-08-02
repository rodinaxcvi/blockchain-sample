import bcrypt



def generate_salt():
    # Generate a random salt using bcrypt
    return bcrypt.gensalt()

def hash_data_with_salt(data, salt):
    # Combine the salt and data, then hash the result
    salted_data = data.encode() + salt
    hashed_data = bcrypt.hashpw(salted_data, salt)
    return hashed_data

# Example usage 
password = "my_secret_password"
salt = generate_salt()
hashed_password = hash_data_with_salt(password, salt)

print("Salt", salt)
print("Hashed Password", hashed_password)
