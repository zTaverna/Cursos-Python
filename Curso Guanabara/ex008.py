medida = float(input('Digite uma distância em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000

print('A medida de {} m corresponde a {:.0f} mm, {:.0f} cm, {:.0f} dm, {} dam, {} hm ou {} km'.format(medida, mm, cm, dm, dam, hm, km))
