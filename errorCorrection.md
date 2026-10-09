# Error Correction

## Even Parity Check

When bits are sent across a network, they are sometimes corrupted by interference or errors. Adding some redundant bits to the end of th transmission can help to detect these errors. The simplest error detection algorithm is known as *parity checking*. A bit string has *even parity* if it has an even number of ones, and is of *odd parity* otherwise. In an even parity scheme, the sender adds a single bit to th end of the bit string so that the final bit string has an even number of ones. For example, if we wished to send the data 1101011, would actually send 11010111 instead so that the bit string has an even number of ones. If we wished to send 1101001 instead, we would actually send 11010010. The receiver then checks whether the received bit string has even parity; if it does not, then an error must have occurred so it requests a retransmission. 

a. Parity can only detect very simple errors. Give an example of an error that cannot be detected by an even parity scheme.

a. Write a function ```evenParity(bits)``` that uses the ```count``` method to return ```True``` if the string bits has even parity and ```False``` otherwise. For example, ```evenParity('110101')``` should return ```True``` and ```evenParity('110001')``` should return ```False```.

a. Now write the ```evenParity``` function without using the ```count``` method.

a. Write a function ```makeEvenParity(bits)``` that returns a string consisting of bits with one additional bit concatenated so that the returned string has even parity. Your function should call your ```evenParity``` function. For example, ```makeEvenParity('110101')``` should return '1101010' and ```makeEvenParity('110001')``` should return `1100011'.

## Checksums

A *checksum* can be added to more general strings to detect errors in their transmission. The simplest way to compute a checksum for a string is to convert each character to an integer representing its position in the alphabet (a=0, b=1, .... , z=25), add all of these integers, and then convert the sum back to a character. For simplicity assume that the string contains only lower case letters. Because the sum will likely be greater than 25, we will compute the sum modulo 26. 

Write a function ```checksum(word)``` that returns word with the appropriate checksum character added to the end. For example, ```checksum('snow')``` should return ```snowp```. ***Hint:*** use ```chr``` and ```ord```.

Write a function ```checksumCheck(word)``` that determines whether the checksum character at the end of word is correct. For example, ```checksumCheck('snowp')``` should return ```True``` but ```checksumCheck('snowy')``` should return ```False```.

## Hamming Distance

*Hamming Distance*, defined to be the number of bit positions that are different between two bit strings, is used to measure the error that is introduced when data is sent over a network. For example, suppose we sent the bit sequence 011100110001 over a network, but the destination received 011000110101 instead. To measure the transmission error, we can find the Hamming distance between the two sequences by lining them up as follows:

  - Sent: 011100110001
  - Received: 011000110101

Since the bit sequences are different in two positions, the Hamming distance is 2. Write a function, ```hamming(bit_seq1, bit_seq2)``` that returns the Hamming distance between the two giveen bit strings. Assume that the two strings have the same length.

*Note:* These exercises are from Chaptr 6 in *Discovering Computer Science* by Jessen Havill.