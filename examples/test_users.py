from Tandapy.tanda import Tanda

tanda = Tanda('7b644150f008d07360869b9b3e3ab3a67fabb6c6f7ac6ecc0a8c7967d210ccb2')

objectList = tanda.getUsers()
objectIDs = objectList.getIDs()
objecti = objectList.getEntry(objectIDs[0])
print(objectIDs)
