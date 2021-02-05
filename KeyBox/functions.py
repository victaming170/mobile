

def password_check(pre_password_, max_fail_times_=3):
    permit = False
    scan = ''
    fail_times = 0
    last_fail = ''
    while True:
        scan = input('Password: >>>')
        if scan == pre_password_:
            # print('Success.')
            permit = True
            break
        elif scan == last_fail:
            print('Repeat the wrong password.')
        else:
            fail_times += 1
            if fail_times == max_fail_times_:
                print('Wrong. Reaching the failure limit, exit.')
                break
            else:
                print(f'[{fail_times}/{max_fail_times_}]Wrong. Try again, pls.')
    return permit


def get_legal_str(show_='Input:', ban_list_={'/', '\\', '@', '|', ':', '*', '<', '>', '?', '"'}):
    while True:
        scan = input(show_ + '\t>>>')
        check = set(scan) &ban_list_
        if check == set():
            return scan
        else:
            print("Don't contain the following characters: ", end='')
            for c in ban_list_:
                print(c, ' ', end='')
            print()

