import re


class DNA:
    def __init__(self, sequence: str):
        self.sequence = sequence
        self.__is_dna_check()

    def __is_dna_check(self):
        not_dna = r'[^atgcnATGCN]'
        if re.search(not_dna, self.sequence):
            raise ValueError("It is not DNA sequence. "
                             "Check that the string contains only "
                             "the nucleotides A, T, G, C, N.")

    def gc_content(self):
        if len(self.sequence) == 0:
            return 0
        gc_count = 0
        for nucleotide in self.sequence:
            if nucleotide.upper() == 'C' or nucleotide.upper() == 'G':
                gc_count += 1
        content = gc_count / len(self.sequence) * 100
        return content

    def reverse_complement(self):
        complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'N': 'N',
                      'a': 't', 't': 'a', 'g': 'c', 'c': 'g', 'n': 'n'}
        complement_sequence = []
        for nucleotide in self.sequence:
            complement_sequence.append(complement[nucleotide])
        complement_sequence.reverse()
        reverse_complement_sequence = ''.join(map(str, complement_sequence))
        return reverse_complement_sequence

    def transcribe(self):
        transcribe_complement = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G',
                                 'N': 'N',
                                 'a': 'u', 't': 'a', 'g': 'c', 'c': 'g',
                                 'n': 'n'}
        complement_rna_sequence = []
        for nucleotide in self.sequence:
            complement_rna_sequence.append(transcribe_complement[nucleotide])
        str_sequence = ''.join(map(str, complement_rna_sequence))
        return RNA(str_sequence)

    def __iter__(self):
        return iter(self.sequence)

    def __eq__(self, other):
        if not isinstance(other, DNA):
            return NotImplemented
        return self.sequence.upper() == other.sequence.upper()

    def __hash__(self):
        return hash(self.sequence)


class RNA:
    def __init__(self, sequence: str):
        self.sequence = sequence
        self.__is_rna_check()
        self.index = 0

    def __is_rna_check(self):
        not_dna = r'[^augcnAUGCN]'
        if re.search(not_dna, self.sequence):
            raise ValueError("It is not RNA sequence. "
                             "Check that the string contains only"
                             " the nucleotides A, U, G, C, N.")

    def gc_content(self):
        if len(self.sequence) == 0:
            return 0
        gc_count = 0
        for nucleotide in self.sequence:
            if nucleotide.upper() == 'C' or nucleotide.upper() == 'G':
                gc_count += 1
        content = gc_count / len(self.sequence) * 100
        return content

    def reverse_complement(self):
        complement = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G',
                      'N': 'N',
                      'a': 'u', 'u': 'a', 'g': 'c', 'c': 'g',
                      'n': 'n'}
        complement_sequence = []
        for nucleotide in self.sequence:
            complement_sequence.append(complement[nucleotide])
        complement_sequence.reverse()
        return ''.join(map(str, complement_sequence))

    def __iter__(self):
        return iter(self.sequence)

    def __eq__(self, other):
        if not isinstance(other, RNA):
            return NotImplemented
        return self.sequence.upper() == other.sequence.upper()

    def __hash__(self):
        return hash(self.sequence)
