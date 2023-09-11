from Classes import *
from functions import *

accounts  = {}

game = sign_up()
update_dict = {game[1]:game[2]}
accounts.update(update_dict)

print(accounts)

