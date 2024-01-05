
encoded_str = "6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"
ct = bytes.fromhex(encoded_str) # Turns it back into bytes
result = ""


for character in ct:
    # Loops with the valid range of ascii characters and checks
    # Which one it is by using the same formula in the provided code to see if its the right one
    for ascii_value in range(33, 127):
        if ((123 * ascii_value + 18) % 256) == character:
            result += chr(ascii_value)
            break
    
print(result)
    
        