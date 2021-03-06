from trans_funcs import transToSurvivalCraft

SecretBase = \
' 0 6+1+2'+\
'+2+3+3+3+3+3+0+3  +0+2+2+2+2+2+0+2'+\
'+0+1+1+1+1+1+0+1  +0 5 5 5 0 5+1+2'+\
'+3+3+3+3+3+3+3+5  +0+3+3+3+3+3+2+1'+\
'+2 0+3+3+0 0 0 0  +5 0+4 0+3 0+2+3'+\
'+2 0+1+1+0 0 0 0   0 0 0 0 0 0+2+3'+\
'+2 0+1+1+0 0 0 0   0 0 0 0 0 0 0 0'+\
'+1+1+1+1+1+1+1+0  +1 0 7 5 0 0 0 5'+\
'+1+1+1+1+1 0+1 0  +1+1 7 5 0 0 0 5'+\
'+1+1+1+1+1+1+0+1  +2 5 0 5 0 5 5 3'+\
' 5 0 6 6 0 0 0 0   2 0 0 0 3 0 0 0'+\
'+1+1+1+1+1+1+1+0  +1 0 7 5 0 0 0 5'+\
'+1+1+1+1+1+1+1+0  +1+1 7 5 0 0 0 5'+\
'+1+1+1+1+1+1+0+1  +2 5 0 5 0 5 5 3'+\
' 5 0 6 6 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 6 0 0 0 6 6 6 5   6 0 7 7 0 7 7 6'+\
' 7 0+1+1+0 5 5 3   5 0 6 6 0 0 0 0'+\
' 6 0 0 0 6 6 6 5   6 0 7 7 0 7 7 6'+\
' 7 0+1+1+0 0 0 0   3 0 0 0 0 0+2+3'+\
'+2 0+1 6 0 0+2+3  +2 0+1 6 0 0+2+3'+\
'+2 0+1 5 0 5 5 3   5 0 6 6 0 0+3 0'+\
'+2 0+1 6 0 0+2+3  +2+1+0 6 0 6+2 0'+\
' 3 0 0 0 1 0 0 0   3 0 0 0 0 0 0 0'+\
'+2+3+3+3+3+3+0+3  +0+2+2+2+2+2+0+2'+\
'+0+1+1+1+1+1+0+1  +0 0 0 0 0 0+1+2'+\
'+2+3+3+3+3+3+3+5  +0+3+3+3+3+3+2+1'+\
'+2 0+3+3+0 0 0 0  +3 0 0 0+3 0 0 0'+\
'+2+3+3+3+3+3+0+3  +0+2+2+2+2+2+0+2'+\
'+0+1+1+1+1+1+0+1  +0 0 0 0 0 0+1+2'+\
'+0+3+3+3+3+3+3+5  +5+3+3+3+3+3+2+1'+\
'+2 0+3+3+0 0 0 0  +3 0 0 0+3 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
'+2 0+1+1+0 0+4 0   5 0 0 0'

shift = 7+10
transToSurvivalCraft(SecretBase, shift, 2)

SecretBase = \
' 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 4 0 0 0 0 0 0 0   4 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 2 0+1-6-0 0 2 3   2 1 0-6-0-6 2 0'+\
' 1 0 0 0-4 0 0 0   1 0 0 0 0 5+1+2'+\
' 5 5 5 5 5 5 0 5   0 5 5 5 5 5 0 5'+\
' 0 5 5 5 5 5 0 5   0 5 5 5 0 5 5 5'+\
' 5 5 5 5 5 5 5 5   0 5 5 5 5 5 5 5'+\
' 5 0 5 5 0 0 0 0  +1 0+4 0+1 6+1+2'+\
' 5 5 5 5 5 5 0 5   0 5 5 5 5 5 0 5'+\
' 0 5 5 5 5 5 0 5   0 5 5 5 0 5 5 5'+\
' 5 5 5 5 5 5 5 5   0 5 5 5 5 5 5 5'+\
' 5 0 5 5 0 0 0 0  +1 0+4 0+1 0+2+3'+\
'+2 0+1+1+0 0+0 0  +0 0 0 0 0 0+2+3'+\
' 0 0 0 0 0 0 0 0  +1 0 0 0'
transToSurvivalCraft(SecretBase, shift, 2)

SecretBaseChord =\
' 0 0'+\
' 4 0 0 0 2 0 0 0   1 0 0 0-7 0 0 0'+\
' 4 0 0 0 2 0 0 0   1 0 0 0-5 0 0 0'+\
' 4 0 0 0-6 0 0 0   1 0 0 0-5 0 0 0'+\
' 1 0 0 0 1 0 0 0  -6 0 0 0-6 0 0 0'+\
'-4 0 0 0-5 0 0 0  -6 0 0 0-7 0 1 0'+\
'-4 0 0 0 0 0 0 0  -3 0 0 0 0 0 0 0'+\
'-4 0 0 0-5 0 0 0  -6 0 0 0 1 0-5 0'+\
'_4-1-4-6_5-2-5-2  _6-3-6-3_6-3-6 1'+\
'_4-1-4-6_5-2-5-2  -1-5 1 2 2 0 1 0'+\
'-4 1 4 0-5 2 5 0  -6 3-5 1-3 1 3 5'+\
' 0 0-4-6 0 0-5 0  -1 0 0 0-1 0 0 0'+\
'_4 0-4-6_5 0-7-5  _6 0-6-3_5 0-7-5'+\
'_4 0-4-6_5 0-7-5   0 0 0 0 1 0 3 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 1 0 3 0'+\
' 0 0 0 0 0 0-2 0  -1-5 2 1 3 0'
transToSurvivalCraft(SecretBaseChord, shift)
SecretBaseChord =\
' 0 0'+\
' 1 0 0 0-7 0 0 0  -6 0 0 0-5 0 0 0'+\
' 1 0 0 0-7 0 0 0  -5 0 0 0-3 0 0 0'+\
' 1 0 0 0-4 0 0 0  -5 0 0 0-3 0 0 0'+\
'-6 0 0 0-6 0 0 0  -3 0 0 0-3 0 0 0'+\
'-1 0 0 0-2 0 0 0  -3 0 0 0 0 0 0 0'+\
'-1 0 1 0 1 0 1 0  -1 0 3 0 3 0 3 0'+\
'-2 0-6 0-2 0-7 0  -3 0 0 0-5 0-2 0'+\
' 4 0 4 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0-5 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 3'+\
'_4-1-1-4_5-2-2-2   0-1-5-1 0 0 0 0'+\
' 0_4-1-1 0_5-2_7   0-3-1_6 0_5-2_5'+\
' 0_4-1-1 0_7-2_7  -1-5 1-5-5 0 1 0'+\
'_4 0-4-6_5 0-7-5  _6 0-6-3_5 0-7-5'+\
'_4 0-4-6_5 0-7-5  -1-5 1-5-5 0 1 0'+\
' 0 0 6 0 0 0 7 0   0 0 0 0 1 0'
transToSurvivalCraft(SecretBaseChord, shift)
SecretBaseChord =\
' 0 0'+\
'-6 0 0 0-5 0 0 0  -3 0 0 0-3 0 0 0'+\
'-6 0 0 0-5 0 0 0  -3 0 0 0-1 0 0 0'+\
'-6 0 0 0-1 0 0 0  -3 0 0 0-1 0 0 0'+\
'-4 0 0 0-4 0 0-5  _6 0 0 0_6 0 0-3'+\
'_4 0 0 0_5 0 0 0  _6 0 0 0-1 0-3 0'+\
'_4 0-5 0-5 0-5-4  _4 0 1 0 1 0 1-5'+\
'_6 0-4 0_5 0-5 0  _6 0-6-7-3-3_5_5'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0-3 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0  +1 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0 0 0 0 0 0 0 0'+\
' 0 0 0 0 0 0 0 0   0-1-5-1+5 0-5 0'+\
' 0_4-1-1 0_5-2_7   0-3-1_6 0_7-2_5'+\
' 0_4-1-1 0_5-2_7   0-1-5-1+5 0-5 0'+\
'-4 1 4 1-5 5 5 0   0 0 0 0+3 0'
transToSurvivalCraft(SecretBaseChord, shift)
