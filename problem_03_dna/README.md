# Problem 03 — Complementing a Strand of DNA

**Source** : [Rosalind - Complementing a Strand of DNA (REVC)](https://rosalind.info/problems/revc/)

## Énoncé
Étant donné une chaîne d'ADN $s$ d'une longueur maximale de 1000 paires de bases (bp), retourner son **brin complémentaire réverse** $s^c$. 
Le brin complémentaire réverse est formé en inversant la séquence d'ADN puis en remplaçant chaque nucléotide par son complémentaire (A $\leftrightarrow$ T, et C $\leftrightarrow$ G).

## Approche
1. **Complémentarité** : Utilisation de `str.maketrans("ATCG", "TAGC")` couplé à `.translate()` pour remplacer simultanément toutes les bases sans conflit.
2. **Inversion** : Utilisation du découpage Python (slicing) `[::-1]` pour inverser la chaîne de caractères (lecture $5' \rightarrow 3'$).

## Fichiers
* `solution_q03.py` : Script Python de résolution.
* `rosalind_revc.txt` : Dataset personnel fourni par Rosalind.
* `README.md` : Documentation du problème.