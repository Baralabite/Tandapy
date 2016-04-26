from Tandapy.tanda import Tanda
from Tandapy.credentials import TOKEN

tanda = Tanda(TOKEN)

for user in tanda.getUsers():
    print(user.name)

print()
print("Name by ID:")
print(tanda.getUsers()[125093].name)

