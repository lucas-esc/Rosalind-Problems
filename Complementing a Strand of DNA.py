data = "AAAACCCGGT"

split_data = list(data)

def transc_data(sequence):
    for i in range(len(sequence)):
        if sequence[i] == "A":
            sequence[i] = "c"

        if sequence[i] == "C":
            sequence[i] = "a"

        if sequence[i] == "G":
            sequence[i] = "t"

        if sequence[i] == "T":
            sequence[i] = "g"
            
    return sequence

new_data = transc_data(split_data)
new_str = ''.join(new_data)
print(new_str.upper())