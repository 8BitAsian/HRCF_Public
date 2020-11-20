import base64

def isodecode():
    inVal = input("Please enter Base64-compatible string:\n")
    output = base64.b64decode(inVal +'=======')
    print(output)
    inVal2 = input('Please enter bytes to be converted to ISO-2022-JP:\n')
    output2 = inVal2.decode('ISO-2022-JP')
    print(output2)
        
def main():
    isodecode()

if __name__ == "__main__": main()


