# Function to count DNA nucleotides
def count_nucleotides(dna_sequence):
    a_count = dna_sequence.count('A')
    c_count = dna_sequence.count('C')
    g_count = dna_sequence.count('G')
    t_count = dna_sequence.count('T')
    
    return f"{a_count} {c_count} {g_count} {t_count}"

# --- Test avec l'exemple Rosalind ---
sample_dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
print("Résultat sample :", count_nucleotides(sample_dna))

# --- Résolution avec ton dataset personnel ---
with open("rosalind_dna.txt", "r") as f:
    dna_sequence = f.read().strip()

print("Résultat final :", count_nucleotides(dna_sequence))