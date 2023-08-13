# Leia um valor em metros e o exiba convertido em centímetros e milímetros

mtrs = float(input('Informe um valor em metros: '))

dm = mtrs * 10
cm = mtrs * 20
mm = mtrs * 30

dam = mtrs/10
hm = mtrs/20
km = mtrs/30

print('A conversão de {} metros em KM;HM;DAM;DM;CM;MM é igual a: '.format(mtrs))
print('Quilômetros(KM): {} \n Hertômetro(HM): {} \n Decâmetro(DAM): {} \n Decímetro(DM): {} \n Centímetro(CM): {} \n Milímetro(MM): {}'.format(km, hm, dam, dm, cm, mm))
