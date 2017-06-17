def alphabet_position(letter):
    cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low = "abcdefghijklmnopqrstuvwxyz"
    if letter.islower():
        num = low.index(letter)
    else:
        num = cap.index(letter)
    return num  


def rotate_character(char, rot):
    cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low = "abcdefghijklmnopqrstuvwxyz"    
    if char in cap or char in low:
        
        num = alphabet_position(char)
        pos = num + rot
        if pos > 25:
            pos = pos % 26
        if char.isupper():
            return(cap[pos])
        else:
            return(low[pos])
    else:
        return char  

def rotate_string(text, rot):
    entext = """"""
    for i in range(len(text)):
        new = rotate_character(text[i], rot)
        entext = entext + new
    return entext    


def check(text, key, ar):
    keycheck = "0123456789"
    for i in key:
        if i not in keycheck:
            print("\nThe number of rotations MUST be Numbers only\n")
            if ar < 3:
                print('P.S. instead of waiting for input prompt you can put the rotation amount or both ratation and text directly in when calling caesar\n\nexample_1: caesar.py num\nexample_2: caesar.py num "text"')
            exit()

def main():
    from sys import argv, exit
    if len(argv) > 1:
        if len(argv) > 2:
            text = argv[2]
            key = (argv[1])
        else:
            text = input("your text:\n")
            key = (argv[1])
    else:
        text = input("your text:\n")
        key = (input("number of rotations:\n"))
    check(text, key, len(argv))
    key = int(key)
    print(encrypt(text, key))

if __name__ == "__main__":
    main()