
dna_to_rna = {
  'G': 'C',
  'C': 'G',
  'T': 'A',
  'A': 'U'
}

def to_rna(dna_strand):
  rna_strand = ''
  for nucleotide in dna_strand:
    if nucleotide not in dna_to_rna:
      return ''
    rna_strand += dna_to_rna[nucleotide]
  return rna_strand
