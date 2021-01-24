from pathlib import Path


# display_=[str], dir_mode_=[bool], default_=[str(path)]
def get_filename(display_, default_='', dir_mode_=False):
    while True:
        print(display_)
        str_in = input('>>>')
        if not str_in:
            str_in = default_
        # py_style_path = (repr(str_in).replace(r'\\', '/'))[1:-1]
        file_Path = Path(str_in)
        if dir_mode_ and file_Path.is_dir():
            return file_Path
        elif file_Path.is_file():
            return file_Path
        else:
            print(f'Can not find {file_Path}, try again pls.')


# generate output file name. file_in_=[Path], begin_=[str], end_=[str]
def gen_out_file_name(file_in_, begin_='', end_=''):
    if begin_ or end_:
        last_dot_i = file_in_.name.rfind('.')
        file_in_dir = '\\'.join(file_in_.parts[:-1])
        if file_in_dir:
            file_in_dir = file_in_dir + '\\'
        file_in_name = file_in_.name[:last_dot_i] if last_dot_i != -1 else file_in_.name
        file_out_ = file_in_dir + begin_ + file_in_name + end_ + file_in_.suffix
        return Path(file_out_)
    else:
        print("The output file and input file can't be named in same name.")


# show all options, get the choice of user. descrip_=[str], default_=[int], options_=n*[str]
def option_button(descrip_, default_, *options_):
    # show the option description
    print(descrip_)
    options_n = len(options_)
    # get default choice
    try:
        default_ = int(default_)
    except ValueError:
        default_ = 0
        print('[ERROR-option_button]Invalid default option, reset to 0.')
    else:
        if default_ >= options_n:
            default_ = 0
            print('[ERROR-option_button]Invalid default option, reset to 0.')
    # show options
    for n in range(options_n):
        if n != default_:
            print(f'({n}) {options_[n]}')
        else:
            print(f'[{n}] {options_[n]}')
    # get choice of user
    while True:
        button = input('>>>')
        if not button:
            button = default_
            break
        elif button in [str(n) for n in range(options_n)]:
            break
        else:
            print('Invalid option, try again pls.')
    return int(button)
