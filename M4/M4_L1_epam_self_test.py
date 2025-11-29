# What Are Functions?

def is_long_enough(password):
    return len(password) >= 8

def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False

def has_special_char(password):
    for char in password:
        if char in "!@#$%^&*()":
            return True
    return False

def validate_password(password, rules):
    for rule in rules:
        if not rule(password):
            return False
    return True

def validate_password_v2(password, rules):
    return all(rule(password) for rule in rules)


password = "SwaHWAGRA!"
list_o_rules = [is_long_enough, has_uppercase, has_special_char]
print(validate_password(password, list_o_rules))
print(validate_password_v2(password, list_o_rules))