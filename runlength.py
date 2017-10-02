runlength = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"


## encoder

def encoder(x):
    
    encoded = []
    i = 1
    j = 0
    input = list(x)

    while (i < len(input)):
        if (input[i] == input[i-1]):
            i += 1
        else:
            encoded.append(i-j)
            encoded.append(input[i-1])
            j=i
            i += 1
                
    encoded.append(i-j)
    encoded.append(input[i-1])

    return encoded

print "Encoded run-length:"
print encoder(runlength)


## decoder

def decoder(encoded):
    
    decoded = []
    i = 1
    
    while (i < len(encoded)):
       decoded.append(encoded[i] * encoded[i-1])
       i += 2

    decoded = ''.join(decoded)
    return decoded

print ""
print "Decoded:"
print decoder(encoder(runlength))
