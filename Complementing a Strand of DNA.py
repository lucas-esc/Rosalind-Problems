#Function to compliment the previous inversed sequence 
def compli_data(sequence):
    for i in range(len(sequence)):
        if sequence[i] == "A":
            sequence[i] = "t"

        if sequence[i] == "C":
            sequence[i] = "g"

        if sequence[i] == "G":
            sequence[i] = "c"

        if sequence[i] == "T":
            sequence[i] = "a"
            
    return sequence

#Inicial data
data = "AAAACCCGGT"

#Inverse the sequence
split_data = list(data)
split_data.reverse()

#Complement the sequence using the function
compli_sequen = compli_data(split_data)
sequen_str = ''.join(compli_sequen)
sequence_compliment = sequen_str.upper()
print(sequence_compliment)
