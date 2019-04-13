'''
Author: Luke Hebert
Date begun: 2019 04 13
Description:
    takes a string of someone's name & converts the string to any matching Amino Acids
        outputs that amino acid string
    then it converts the amino acid string to DNA codons for a template DNA strand
        outputs those DNA bases
Note: these can then be turned into a 3D DNA structure with the predictive in-browser tool: http://structure.usc.edu/make-na/server.html
'''

def getCodon(aa):
    #returns a 3-base long codon for the amino acid argument using a codon table;
    #due to the redundancy of genetic code, a random codon is chosen from the possible amino acid's codons
    import random
    codon_dict = {'A': ['GCT','GCC','GCA','GCG'],
              'R': ['CGT','CGC','CGA','CGG','AGA','AGG'],
              'N': ['AAT','AAC'],
              'D': ['GAT','GAC'],
              'C': ['TGT','TGC'],
              'Q': ['GAA','GAG'],
              'E': ['CAA','CAG'],
              'G': ['GGT','GGC','GGA','GGG'],
              'H': ['CAT','CAC'],
              'I': ['ATT','ATC','ATA'],
              'L': ['TTA','TTG','CTT','CTC','CTA','CTG'],
              'K': ['AAA','AAG'],
              'M': ['ATG'],
              'F': ['TTT','TTC'],
              'P': ['CCT','CCC','CCA','CCG'],
              'S': ['TCT','TCC','TCA','TCG','AGT','AGC'],
              'T': ['ACT','ACC','ACA','ACG'],
              'W': ['TGG'],
              'Y': ['TAT','TAC'],
              'V': ['GTT','GTC','GTA','GTG']}
    codon_str = random.choice(codon_dict[aa]) if aa.upper() in codon_dict else '...'
    return codon_str

#the user inputs a name
name_str_in = input('Enter a name:')
name_str = name_str_in.replace(' ','').upper() #remove any spaces
print('Original name: ' + name_str)

#the name is translated to available amino acids (usually looks weird, but recognizeable)
aa_list = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']
aa_name = ''.join([acid for acid in list(name_str) if acid in aa_list])
print('\nAmino acid version of name: ' + aa_name)

#the amino acid version of the name is then reverse-translated to DNA codons
dna_name = ''.join([getCodon(aa) for aa in list(aa_name)])
print('\nDNA version of name: ' + dna_name)

#output these versions of the name to a text file
with open(name_str + '.txt', 'w') as outFile:
    outFile.write(name_str + '\n')
    outFile.write(aa_name + '\n')
    outFile.write(dna_name + '\n')
