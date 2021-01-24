from pathlib import Path


# display_=[str], dir_mode_=[bool], default_=[str(path)]
def get_filename(display_, default_='', dir_mode_=False):
    while True:
        print(display_)
        str_in = input('>>>')
        if not str_in:
            str_in = default_
        py_style_path = (repr(str_in).replace(r'\\', '/'))[1:-1]
        file_Path = Path(py_style_path)
        if dir_mode_ and file_Path.is_dir():
            return file_Path
        elif file_Path.is_file():
            return file_Path
        else:
            print(f'Can not find {file_Path}, try again pls.')


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
