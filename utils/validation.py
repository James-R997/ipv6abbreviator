
VALID_HEX_DIGITS = "0123456789ABCDEFabcdef"

def validate(ipv6Addr:str, prefix:int) -> bool:
    '''
    Checks if the the given ipv6 address/prefix is a valid one.
    Raises a type error with the explaination of why the address/prefix is invalid. 
    '''

    if prefix > 128 or prefix < 0:
        raise TypeError(f"Prefix [{prefix}] is out of range")   #works
    
    

    if ipv6Addr.count("::") > 1:
        raise TypeError("Invalid use of '::'")    # works

    if "::" in ipv6Addr:
        head, sep, tail = ipv6Addr.partition("::")
        headParts = head.split(":") if head else []
        tailParts = tail.split(":") if tail else []

        quartets = headParts + ["0"] * ( 8 - len(headParts) - len(tailParts) )

    else:
        quartets = ipv6Addr.split(":")

    print(quartets)

    if len(quartets) != 8:
        raise TypeError("Invalid amount of quartets (more than 8)") # works

    for q in quartets:
        if len(q) > 4:
            raise TypeError(f"Quartet [{q}] has more than 4 digits") # works

        for digit in q:
            if digit not in VALID_HEX_DIGITS:
                raise TypeError(f"Invalid hexadecimal values in [{q}]") # works
        
    return True # meaning the address and the prefix are valid.


    
    

        
# print(validate("2001:0db8:abcd:ef::", 128))