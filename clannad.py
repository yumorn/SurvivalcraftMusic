from trans_funcs import transToSurvivalCraft

clannad = \
'''
 0 0 0 0 0 0*6*5  ^1 0^1 0^2 0^2 0  ^3 0^1 0*5 0*6*5  ^1 0^1 0^2 0^2 0
^3^3^1 0 0 0*6*5  ^1 0^1 0^2^2^1 0   0 0 0 0 0 0*6*5  *1 0*1 0*2 0*2 0
*3 0*1 0+5 0+6+5  *1 0*1 0*2 0*2 0  *3 0*2 0 0 0+6+5  *1 0*1 0*2 0*1 0
 0 0 0 0 0 0+6+5  *1 0*1 0*2 0*2 0  *3 0*1 0+5 0+6+5  *1 0*1 0*2 0*2 0
*3 0*2 0 0 0+6+5  *1 0*1 0*2 0*1 0   0 0 0 0 0 0 0 0  *4*3*1+6 0*1*2+6
'''
shift = -12
transToSurvivalCraft(clannad, shift, 1)

# 暂未完成