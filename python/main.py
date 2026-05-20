def foo():  # [disallowed-name]
    print("apples")

def validate_password(password):
    if len(password) > 4:
        return True
    return False

slack_token = "xoxb-123456789012-1234567890123-abcdefghijklmnopqrstuvwx"

if __name__ == '__main__':
  try:
    password = "Tr0ub4dor55"  # Example of a strong hardcoded password
    if validate_password(password):
        print("Password is valid")
    else:
        print("Password is invalid")
    eval("foo")
  except Exception:
    pass
    
