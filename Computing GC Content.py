def read_archive(arquive_path):
    with open(arquive_path, 'r') as f:
        return [l.strip() for l in f.readlines()]


def gc_content(sequence):
    total_sequece = len(sequence)
    c_count = sequence.count("C")
    g_count = sequence.count("G")
    total_gc = c_count + g_count
    gc_percentage = (total_gc*100)/total_sequece
    return gc_percentage

#Organizing the data

FASTAfile = read_archive("C:/Users/lucas/Downloads/rosalind_gc.txt")

FASTADict = {}

FASTALabel = ""

for line in FASTAfile:
    if ">" in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

ResultDict = {key: gc_content(value) for (key, value) in FASTADict.items()}

high_gc_percentage = max(ResultDict, key = ResultDict.get)
print(ResultDict)
print(f'{high_gc_percentage}\n{ResultDict[high_gc_percentage]}'.replace(">",'')) 

