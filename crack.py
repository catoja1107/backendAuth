import hashlib


def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()


def crack():
    hashArray = []
    # Must get user input (uid+pass) and compare to DB files.
    try:
        f = open("Hash.txt", 'r', encoding="utf-8")
    except:
        print("File not found")
    finally:
        with open("Hash.txt", encoding="utf-8") as f:
            for line in f:
                hashArray = f.read().splitlines()
    f.close()
    i = 000  # UID salt lower bound
    j = 100  # UID salt upper bound
    k = 0000  # Pass lower bound
    l = 1000  # Pass upper bound
    print("Attemping crack for UID salt range 000-" + str(j), "and pass range 0000-" + str(l))
    for a in range(i, j+1):  # check every pass for UID 000, then 001, 002...
        tmpa = '{:>03}'  # 3 digits min, zero prefix
        resa = tmpa.format(str(a))  # formats UID to include trailing 0's
        for b in range(k, l+1):  # check every pass for single UID at a time
            tmpb = '{:>04}'  # 4 digits min, zero prefix
            resb = tmpb.format(str(b))  # formats pass to include trailing 0's
            test = computeMD5hash(resb + resa)  # pass + salt
            if test in hashArray: print("Password:", resb + "; Salt:", resa + "; Hash match:", test)


def main():
    crack()
    return 0


if __name__ == "__main__":
    main()
