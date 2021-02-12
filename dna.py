# Khoa Tran
# CSCI 236
# 2/11/2021
# Program 2 - DNA
# 6 hours
# Grade Version (some programs will have A, B, C versions, this one does not)
# How to not create an infinite loop
# status of the program - Does compile, does it run perfectly (not sure), does it have bugs(no), any limitations, etc

from textwrap import wrap
import re

print("This program reports information about DNA" + "\n" +
      "nucleotide sequences that may encode proteins")
file = open(input("Input file name? "))
out_file=open(input("Output file name? "), "w")
print()
lines = file.readlines()

NUM_NUCLEOTIDES = 4  # number of nucleotides (A,C,G,T)
MASSES = [135.128, 111.103, 151.128, 125.107]
numbersofCodons = 5
nucleotidesperCodon = 3
valid_protein_mass_of_C_and_G = 30


def get_count(list):
    j = 0
    aCount = 0
    tCount = 0
    cCount = 0
    gCount = 0
    junkCount = 0
    seq = lines[i + 1].upper()
    while j < len(seq):
        if seq[j] == 'A':
            aCount += 1
        elif seq[j] == 'T':
            tCount += 1
        elif seq[j] == 'C':
            cCount += 1
        elif seq[j] == 'G':
            gCount += 1
        elif seq[j] == '-':
            junkCount += 1
        j += 1
    return [aCount, cCount, gCount, tCount]


def get_Junk(list):
    j = 0
    aCount = 0
    tCount = 0
    cCount = 0
    gCount = 0
    junkCount = 0
    seq = lines[i + 1].upper()
    while j < len(seq):
        if seq[j] == 'A':
            aCount += 1
        elif seq[j] == 'T':
            tCount += 1
        elif seq[j] == 'C':
            cCount += 1
        elif seq[j] == 'G':
            gCount += 1
        elif seq[j] == '-':
            junkCount += 1
        j += 1
    return junkCount


def get_percentages(countList, junkCount):
    MASSES
    get_count(countList)
    totalMass = (countList[0] * MASSES[0]) + (countList[1] * MASSES[1]) + (countList[2] * MASSES[2]) + (
            countList[3] * MASSES[3]) + (get_Junk(junkCount) * 100.000)
    roundTotal = round(totalMass, 1)
    percentA = ((countList[0] * MASSES[0]) / roundTotal) * 100
    roundA = round(percentA, 1)
    percentC = ((countList[1] * MASSES[1]) / roundTotal) * 100
    roundC = round(percentC, 1)
    percentT = ((countList[2] * MASSES[2]) / roundTotal) * 100
    roundT = round(percentT, 1)
    percentG = ((countList[3] * MASSES[3]) / roundTotal) * 100
    roundG = round(percentG, 1)
    return str([roundA, roundC, roundG, roundT]) + " of " + str(roundTotal)


def get_percentagesCG(countList, junkCount):
    MASSES
    get_count(countList)
    totalMass = (countList[0] * MASSES[0]) + (countList[1] * MASSES[1]) + (countList[2] * MASSES[2]) + (
            countList[3] * MASSES[3]) + (get_Junk(junkCount) * 100.000)
    roundTotal = round(totalMass, 1)
    percentA = ((countList[0] * MASSES[0]) / roundTotal) * 100
    roundA = round(percentA, 1)
    percentC = ((countList[1] * MASSES[1]) / roundTotal) * 100
    roundC = round(percentC, 1)
    percentT = ((countList[2] * MASSES[2]) / roundTotal) * 100
    roundT = round(percentT, 1)
    percentG = ((countList[3] * MASSES[3]) / roundTotal) * 100
    roundG = round(percentG, 1)
    proteinValid = roundG + roundC
    return proteinValid


def get_codons(sequence):
    j = 0
    seq = lines[i + 1].upper()
    while j < len(seq):
        nucleotidesperCodon
        triplets = str(seq).replace("-", "")
        tripletsPerfect = re.findall('...', str(triplets))
        j += 1
    return tripletsPerfect


if __name__ == '__main__':
    # loop thru each pair of input lines
    i = 0
    while i < len(lines):
        # loop thru dna sequence
        sequence = lines[i + 1]
        print("Region Name: " + lines[i] +
              "Nucleotides: " + lines[i + 1] +
              "Nuc. Counts: " + str(get_count(sequence)))
        print("Total Mass%: " + get_percentages(get_count(sequence), get_Junk(sequence)))
        print("Codons List: " + str(get_codons(sequence)))
        if str(get_codons(sequence)[-1]) == 'TAA' and get_percentagesCG(get_count(sequence), get_Junk(
                sequence)) >= valid_protein_mass_of_C_and_G:
            print("Is Protein?: YES")
        elif str(get_codons(sequence)[-1]) == 'TAG' and get_percentagesCG(get_count(sequence), get_Junk(
                sequence)) >= valid_protein_mass_of_C_and_G:
            print("Is Protein?: YES")
        elif str(get_codons(sequence)[-1]) == 'TGA' and get_percentagesCG(get_count(sequence), get_Junk(
                sequence)) >= valid_protein_mass_of_C_and_G:
            print("Is Protein?: YES")
        else:
            print("Is Protein?: NO")
        print()
        i += 2
