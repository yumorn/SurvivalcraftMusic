def transToSurvivalCraft(source, shift=0, extend=True):
    source += '   '
    def tuneToDigit(tune):
        return {'1':0, '2':2, '3':4, '4':5, '5':7, '6':9, '7':11}[tune]
    pitch = []
    octave = []
    oct = 12
    for tune in source:
        if tune == ' ':
            continue
        elif tune == '*':
            oct = 36
        elif tune == '+':
            oct = 24
        elif tune == '-':
            oct = 0
        elif tune == '_':
            oct = -12
        else:
            if tune == '0':
                pitch.append('F')
                octave.append('F')
            else:
                p = oct + tuneToDigit(tune) + shift
                if p < 0:
                    raise Exception('Lower Bound Exceeded')
                elif p > 48: #一共4个八度加上一个do（49种频率）
                    raise Exception('Upper Bound Exceeded')
                # octave=3 pitch=c 为最后一个do
                pitch.append('0123456789ABCDE'[p%12 if p<36 else p-36])
                octave.append(str(p//12 if p<36 else 3))
            oct = 12
    pitch = ''.join(pitch)
    octave = ''.join(octave)
    l = len(pitch)
    if extend:
        times = 256 // l
        return pitch * times, octave * times, l
    else:
        return pitch, octave, l

def split(source):
    A = []
    B = []
    turnA = True
    oct = ''
    for tune in source:
        if tune == ' ':
            continue
        elif tune == '+' or tune == '-':
            oct = tune
        else:
            (A if turnA else B).append(oct + tune)
            turnA = not turnA
            oct = ' '
    # 确保两者等长
    if not turnA:
        B += ' 0'
    return ''.join(A), ''.join(B)

PlayingLove =\
'123-50032120021-7-500234300'+\
'565145003200432-7121-600'+\
'123-50032120021-7-500235+100'+\
'13221-5-3-60013221-5-3-200'+\
'-5-6-556531004542-700'+\
'1-721-712130021232-6-7100'+\
'1213003452001213002321-700'
#print(transToSurvivalCraft(PlayingLove))
IAndMyCountry =\
'56543210-5013+1763500067654320-60'+\
'-7-6-5512300056543210-5013+17+2+16000'+\
'+1765065430-7-6-5-521000+1+2+3+2+167635000'+\
'+1+2+3+2+167536000543207665304021'+\
'1000+1+2+3+2+167635000+1+2+3+2+16'+\
'76360054320-7-6-53050+2+1+1000000000000000'
#print(transToSurvivalCraft(IAndMyCountry))
MyCountry =\
'12-6-5506035+1650005065323053-612000'+\
'2531-6-5-60265630201235+16505-6124066'+\
'5632100055+10+2+1656053+165230'+\
'356+1+2+3+2+1+23567+2675000'+\
'12-6-5506035+1650005065323053-612000'+\
'2531-6-5-60265630201235+16505-6124066'+\
'5632100055+10+2+1656053+165230'+\
'356+1+2+3+2+1+2765356+2+1'
#print(transToSurvivalCraft(MyCountry))
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

SecretBaseA, SecretBaseB = split(SecretBase)
shift = 7+10
print(transToSurvivalCraft(SecretBaseA, shift))
print(transToSurvivalCraft(SecretBaseB, shift))

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
SecretBaseA, SecretBaseB = split(SecretBase)
print(transToSurvivalCraft(SecretBaseA, shift))
print(transToSurvivalCraft(SecretBaseB, shift))

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
print(transToSurvivalCraft(SecretBaseChord, shift))
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
print(transToSurvivalCraft(SecretBaseChord, shift))
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
print(transToSurvivalCraft(SecretBaseChord, shift))
