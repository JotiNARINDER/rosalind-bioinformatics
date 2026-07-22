def dna_to_rna(dna_sequence):  
    return dna_sequence.replace('T', 'U')

# Test avec l'exemple Rosalind 
sample_dna = "GATGGAACTTGACTACGTAAATT"
print("Résultat sample :", dna_to_rna(sample_dna))

# Avec le dataset personnel
with open("rosalind_rna.txt", "r") as f:
    dna_sequence = f.read().strip()

print("\nRésultat final :", dna_to_rna(dna_sequence))
