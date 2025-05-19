# Bifid Cipher Algorithm

## Overview
The Bifid cipher is a classical encryption technique invented by French cryptographer Félix Delastelle in 1901. It combines the Polybius square with fractionation to create a more secure cipher than simple substitution methods.

## How It Works

### 1. Polybius Square Construction
A 6×6 grid containing all letters (A-Z) and digits (0-9) is created with a random or predefined arrangement:


```
Classical alphabet
['A', 'B', 'C', 'D', 'E', 'F'],  
['G', 'H', 'I', 'J', 'K', 'L'],  
['M', 'N', 'O', 'P', 'Q', 'R'],  
['S', 'T', 'U', 'V', 'W', 'X'],  
['Y', 'Z', '0', '1', '2', '3'],  
['4', '5', '6', '7', '8', '9']

Shuffled example alphabet
['K', 'V', '4', 'R', '0', 'X']
['C', '5', '6', 'D', '9', 'J']
['7', 'H', 'E', 'Y', 'M', '8']
['S', 'O', 'L', 'Z', 'I', '3']
['A', 'B', 'W', 'F', 'T', '2']
['P', 'N', 'Q', 'G', '1', 'U']
```

### 2. Encryption Process
1. **Find coordinates** for each character in the plaintext
2. **Separate** row and column numbers into two sequences
3. **Concatenate** the sequences
4. **Split** into pairs to form new coordinates
5. **Map back** to ciphertext characters

Example with "HELLO":  
H(1,1), E(0,4), L(1,5), L(1,5), O(2,2)  
Rows: 1 0 1 1 2  
Columns: 1 4 5 5 2  
Combined: 1 0 1 1 2 1 4 5 5 2  
Regrouped: (1,0), (1,1), (2,1), (4,5), (5,2)  
Ciphertext: G H N 3 6 → "GHN36"


### 3. Decryption Process
1. **Find coordinates** for each ciphertext character
2. **Flatten** into a single sequence
3. **Split** into row and column halves
4. **Recombine** into coordinate pairs
5. **Map back** to plaintext

Example with "GHN36":  
Ciphertext: G   H   N   3   6  
Coordinates: (1,0) (1,1) (2,1) (4,5) (5,2)  
Flattened: 1 1 2 4 5 | 0 1 1 5 2  
Regrouped: (1,0) (1,1) (2,1) (4,5) (5,2)  
Realization: Need original square mappings:  
(1,1)→H, (0,4)→E, (1,5)→L, (2,2)→O  


## Example Usage

```python
from bifid import bifid_encrypt, bifid_decrypt, shuffle_table, classical_table


text = "OUR TRUE MENTOR IN LIFE IS SCIENCE. (MUSTAFA KEMAL ATATURK - 1924)"

table = shuffle_table(classical_table)
ciphertext = bifid_encrypt(text, classical_table)
plaintext = bifid_decrypt(ciphertext, classical_table)
```

```
['U', 'Q', 'D', '4', 'H', 'L']
['V', 'W', 'X', 'T', 'K', 'C']
['Y', 'M', '7', 'N', '1', '6']
['B', 'Z', 'O', 'G', 'A', '9']
['2', '5', '8', 'P', 'I', 'F']
['J', '3', 'E', 'S', 'R', '0']

PPP CCUN NGBVBC AP VABC BD DUK86RL. (QEHRN68 MCQIY MG42A4G - I8XY)
OUR TRUE MENTOR IN LIFE IS SCIENCE. (MUSTAFA KEMAL ATATURK - 1924)
