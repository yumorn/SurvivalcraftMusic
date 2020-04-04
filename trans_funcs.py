def transToSurvivalCraft(source, shift=0, extend=True):
    source += '   '
    def tuneToDigit(tune):
        return {'1':0, 'a':1, '2':2, 'b':3, '3':4, '4':5, 'd':6, '5':7, 'e':8, '6':9, 'f':10, '7':11}[tune]
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
