import yaml
import functions as mx

# macro
PJ_PATH = "D:/WorkspaceMX/Python_PJ/KeyBox/"
F_CONFIG = PJ_PATH + "iof/box_rom.yml"

# say hello
print('==== ==== ===== ==== ====')
print('==== === Key_Box === ====')
print('==== ==== ===== ==== ====')

# load config
with open(F_CONFIG, 'r') as f_config:
    rom = yaml.load(f_config, Loader=yaml.FullLoader)
setting = rom['setting']
notes = rom['notes']

if mx.password_check(setting['login_password']):
    print('Welcome to KeyBox 1.0')
