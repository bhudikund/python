import sys

def decrypt(text):
    decrypt_result = []
    lenght = len(text)
    i=0

    while i < lenght:

        if text[i] == '.':
            if i + 1 < lenght and text[i + 1] == '.':
                if decrypt_result:
                    decrypt_result.pop()
                i += 2
            else:
                i += 1
        else:
            decrypt_result.append(text[i])
            i += 1
    return "".join(decrypt_result)


if __name__ == "__main__":
    lines = sys.stdin.readline()
    decrypted = decrypt(lines)
    print (lines + " -> " + decrypted)