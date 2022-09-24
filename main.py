# James Cato
# ⣐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⣿⣅⡠⠃⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⢹⣿⣇⡀⠀⠀⠀⢀⣤⣤⣤⣾⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀
# ⢸⣿⣿⣷⡀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣶
# ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⡀⠀⠀⠀⣀⣀⣤⣾
# ⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
# ⠀⠀⠉⠙⠉⠉⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⠟⠋⠁⠀⠀
#
# its morbin time
import hashlib


def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()


def getSalt():
    fileName = input("Enter salt file name: ")
    saltArray = []
    try:
        f = open(fileName, 'r', encoding="utf-8")
    except:
        print("File not found")
    finally:
        with open(fileName, encoding="utf-8") as f:
            for line in f:
                saltArray = f.read().splitlines()
        f.close()
        return saltArray


def getUID():
    fileName = input("Enter UID file name: ")
    UIDArray = []
    try:
        f = open(fileName, 'r', encoding="utf-8")
    except:
        print("File not found")
    finally:
        with open(fileName, encoding="utf-8") as f:
            for line in f:
                UIDArray = f.read().splitlines()
        f.close()
    return UIDArray


def getPass():
    fileName = input("Enter Password file name: ")
    passArray = []
    try:
        f = open(fileName, 'r', encoding="utf-8")
    except:
        print("File not found")
    finally:
        with open(fileName, encoding="utf-8") as f:
            for line in f:
                passArray = f.read().splitlines()
        f.close()
    return passArray


def cmpHash():
    fileName = input("Enter HASH list file name: ")
    hashArray = []
    try:
        f = open(fileName, 'r', encoding="utf-8")
    except:
        print("File not found")
    finally:
        with open(fileName, encoding="utf-8") as f:
            for line in f:
                hashArray = f.read().splitlines()
        f.close()
        # computedHashArray = computeMD5hash(getPass(), getSalt())
        # for i in uid, call computeMD5hash(getPass[i]+getSalt[i])
        UID = getUID()
        password = getPass()
        salt = getSalt()
        computedHashArray = []
        # print(UID, password, salt)
        for i in range(len(password)):
            computedHashArray.append(computeMD5hash(password[i] + salt[i]))
        for i in range(len(hashArray)):
            if i in range(len(computedHashArray)):
                print("Credentials in database:", "UID", UID[i], "| PASS", password[i], "| SALT", salt[i], "| MD5", hashArray[i], computedHashArray[i])


def main():
    cmpHash()
    return 0


if __name__ == "__main__":
    main()