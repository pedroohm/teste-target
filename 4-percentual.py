'''
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53
'''

SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53

total = SP + RJ + MG + ES + OUTROS

percentual_SP = SP/total*100
percentual_RJ = RJ/total*100
percentual_MG = MG/total*100
percentual_ES = ES/total*100
percentual_OUTROS = OUTROS/total*100

print("Percentual de faturamento por estado:")
print("SP: %.2f%%" % percentual_SP)
print("RJ: %.2f%%" % percentual_RJ)
print("MG: %.2f%%" % percentual_MG)
print("ES: %.2f%%" % percentual_ES)
print("Demais estados: %.2f%%" % percentual_OUTROS)