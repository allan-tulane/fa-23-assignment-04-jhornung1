import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))

## INCOMPLETE: I was unable to get this to work, I got really close but ran out of time (which is 100% my fault)
def fast_MED(S, T, MED={}):
  if (S, T) in MED:
    return MED[(S, T)]

  if S == "":
    result = len(T)
  elif T == "":
    result = len(S)
  else:
    if S[0] == T[0]:
        result = fast_MED(S[1:], T[1:], MED)
    else:
        result = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED))

  MED[(S, T)] = result
  return result

def fast_align_MED(S, T, MED={}):
  if (S, T) in MED:
    return MED[(S, T)]

  if S == "":
    result = len(T)
    alignment_S = "-" * len(T)
    alignment_T = T
  elif T == "":
    result = len(S)
    alignment_S = S
    alignment_T = "-" * len(S)
  else:
    sub_result, sub_alignment_S, sub_alignment_T = fast_align_MED(S[1:], T[1:], MED)
    del_result, del_alignment_S, del_alignment_T = fast_align_MED(S[1:], T, MED)
    ins_result, ins_alignment_S, ins_alignment_T = fast_align_MED(S, T[1:], MED)

    if S[0] == T[0]:
        result = sub_result
        alignment_S = S[0] + sub_alignment_S
        alignment_T = T[0] + sub_alignment_T
    else:
        if del_result < ins_result:
            result = 1 + del_result
            alignment_S = S[0] + del_alignment_S
            alignment_T = "-" + del_alignment_T
        else:
            result = 1 + ins_result
            alignment_S = "-" + ins_alignment_S
            alignment_T = T[0] + ins_alignment_T

  MED[(S, T)] = (result, alignment_S, alignment_T)
  return result, alignment_S, alignment_T

              
def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        edit_distance, align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
