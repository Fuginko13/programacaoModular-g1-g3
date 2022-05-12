import hashlib

def hash(hasher, password, salt):
  to_be_hashed = (salt + password).encode()
  hasher.update(to_be_hashed)
  return salt + hasher.hexdigest()  
