def to_int(text):
    try:
        return int(text)
    except Exception as e:
        print(f"'{text}' is not a number")
        print(f"{e} occurred")
        return None

print(to_int("42"))
to_int([2,3])   