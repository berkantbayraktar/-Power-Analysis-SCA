def modPower(b,exp,n):
    r = 1
    for bit in exp:
        r *= r
        r %= n

        if(bit == "1"):
            r *= b
            r %= n
    return r



if __name__ == "__main__":

    ciphertext = input()
    n = input()
    
    ciphertext = int(ciphertext,16)
    n = int(n,16)

    f = open('ptrace.trc', 'r') 
    lines = f.readlines() 
    f.close()

    binary_str = ""
    is_changed = False
  

    count = 0
    for line in lines: 
        if(float(line.strip()) < 3 ):
            if(count == 125):
                binary_str += "1"

            elif(count == 75):
                binary_str += "0"
            count = 0

        else:
            count+=1

            
    res = modPower(ciphertext,binary_str,n)

    hex_str = format(res,'x')
    bytes_obj = bytes.fromhex(hex_str)
    ascii_str = bytes_obj.decode("ASCII")
    print(ascii_str)