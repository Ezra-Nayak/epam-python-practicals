# Sets

def analyze_roles(roles_a, roles_b):
    set_a = set(roles_a)
    set_b = set(roles_b)

    common_roles = set_a.intersection(set_b)
    exclusive_to_a = set_a.difference(set_b)
    all_unique_roles = set_a.union(set_b)

    return {
        'common_roles': common_roles,
        'exclusive_to_a': exclusive_to_a,
        'all_unique_roles': all_unique_roles
    }


user_a_roles = ['editor', 'viewer', 'commenter', 'viewer']
user_b_roles = ['admin', 'editor', 'editor', 'Match MVP']

print(analyze_roles(user_a_roles, user_b_roles))