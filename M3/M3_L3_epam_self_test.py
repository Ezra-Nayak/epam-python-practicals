# Boolean and Comparison Operator

def get_user_status(is_admin: bool, is_active: bool, permission_level: int):
    if not is_active:
        return "Account Disabled"
    elif is_admin:
        return "Admin Access"
    elif permission_level is not None and permission_level >= 5:
        return "Power User"
    elif permission_level is not None:
        return "Standard User"
    else:
        return "Guest Access"


print(get_user_status(False, True, 1))