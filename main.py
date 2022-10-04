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
    salt = input("Enter salt: ")
    return salt


def getUID():
    UIDArray = []
    try:
        f = open("UID.txt", 'r', encoding="utf-8")
    except:
        print("File not found")
    finally:
        with open("UID.txt", encoding="utf-8") as f:
            for line in f:
                UIDArray = f.read().splitlines()
        f.close()
    return UIDArray


def getPass():
    passw = input("Please input password: ")
    return passw


def cmpHash():
    hashArray = []
    try:
        f = open("Hash.txt", 'r', encoding="utf-8")
    except:
        print("File not found")
    finally:
        lines = f.readlines()
        hashArray = [line.rstrip() for line in lines]
        f.close()
        password = getPass()
        salt = getSalt()
        computedhash = computeMD5hash(password+salt)
        if (computedhash in hashArray):
            print("Credentials in database.")
        else:
            print("Credentials not in database.")


def main():
    cmpHash()
    return 0


if __name__ == "__main__":
    main()
