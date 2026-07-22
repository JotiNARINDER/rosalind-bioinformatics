def inverser_mot(DNA):
    return DNA[::-1]

with open("rosalind_revc.txt", "r") as f:
    dna_sequence = f.read().strip()

def complementary(dna_sequence):
    table = str.maketrans("ATCG", "TAGC")
    resultat = dna_sequence.translate(table)
    return(inverser_mot(resultat))  

print("Résultat final :", complementary(dna_sequence))