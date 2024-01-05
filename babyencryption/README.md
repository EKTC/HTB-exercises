# CHALLENGE DESCRIPTION

You are after an organised crime group which is responsible for the illegal weapon market in your country. As a secret agent, you have infiltrated the group enough to be included in meetings with clients.
During the last negotiation, you found one of the confidential messages for the customer. It contains crucial information about the delivery. Do you think you can decrypt it?

# Files

- msg.enc : Contains the encoded message
- chall.py : Contains the source code of how the message was encoded

# Solution

1. We can notice that in the `chall.py` file there that the message is encoded into hexadecimal from bytes
2. Those bytes were created from the unmodified versions of the characters that were changed however
3. Those characters were changed with a formula which is this `(123 * char + 18) % 256`

- Now recognising all these features we can create a solution which takes the encoded string we are given and convert it back into bytes
- Having the raw bytes we recognise that there is a range of possible values possible based on the ASCII table
- The viable values range from 33 to 127 so, we can check what the letter is by brute forcing by using the same formula and checking if the characters match

Flag: HTB{l00k_47_y0u_r3v3rs1ng_3qu4710n5_c0ngr475}
