class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    if len(user) == 0:
        return "user argument can't be empty"
    else:
        if len(group.get_groups()) == 0:
            return False
        for group in group.get_groups():
            if is_user_in_group(user, group):
                return True
        return False

if __name__ == "__main__":
    
    # Test 1 (user is in the group)
    print("Test 1 (user is in the group)")
    print(is_user_in_group('sub_child_user', parent))
    print("#"*60)
    # Test 2 (user is not in the group)
    print("Test 2 (user is not in the group)")
    print(is_user_in_group('test_dir', parent))
    print("#"*60)
    # Test 3 (empty user)
    print("Test 3 (empty user)")
    print(is_user_in_group('', parent))