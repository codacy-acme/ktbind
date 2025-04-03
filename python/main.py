def foo():  # [disallowed-name]
    print("apples")

def validate_password(password):
    if len(password) > 4:
        return True
    return False


if __name__ == '__main__':
  try:
    password = "Tr0ub4dor&3"  # Example of a strong hardcoded password
    if validate_password(password):
        print("Password is valid")
    else:
        print("Password is invalid")
    eval("foo")
  except Exception:
    pass