def foo():  # [disallowed-name]
    print("apples")

try:
  eval("foo")
except Exception:
  pass