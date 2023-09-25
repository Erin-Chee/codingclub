


#Translate RNA string to protein (example: AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA)



RNA = str(input('Please provide an RNA string to translate:'))

proteindict ={'AUG':'M','UAA':'STOP','UAG':'STOP','UGA':'STOP','UUU':'F','UUC':'F','UUA':'L',
'UUG':'L','CUU':'L','CUC':'L','CUA':'L','CUG':'L','AUU':'I','AUC':'I','AUA':'I','GUU':'V',
'GUC':'V','GUA':'V','GUG':'V','UCU':'S','UCC':'S','UCA':'S','UCG':'S','CCU':'P','CCC':'P','CCA':'P',
'CCG':'P','ACU':'T','ACC':'T','ACA':'T','ACG':'T','GCU':'A','GCC':'A','GCA':'A','GCG':'A','UAU':'Y',
'UGC':'C','UGG':'W','CGU':'R','CGC':'R','CGA':'R','CGG':'R','AGU':'S','AGC':'S','AGA':'R','AGG':'R',
'GGU':'G','GGC':'G','GGA':'G','GGG':'G','GAG':'E','GAA':'E','GAC':'D','GAU':'D','AAG':'K','AAA':'K',
'AAC':'N','AAU':'N','CAG':'Q','CAA':'Q','CAC':'H','CAU':'H'}

protein = [] #list for all of the translated amino acids


start = 0 #set position of start codon to 0


#iterate through all nucleotides in groups of 3 to find position of the start codon
          
for x in range(len(RNA)):
  if RNA[x:x+3] == 'AUG':
    start += x
    break



#translate each codon into its respective amino acid, then append the AA to list 'protein'

while 1:
  if start < len(RNA):
    codon = RNA[start:start + 3]
    start += 3
    if codon in proteindict and proteindict[codon] != 'STOP':
      protein.append(proteindict[codon])
      continue
    elif proteindict[codon] == 'STOP':
      break
    else:
      protein.append('X')
      continue
  else:
    break
  break

      
  
print('The translated protein string is {0}'.format(''.join(protein)))


