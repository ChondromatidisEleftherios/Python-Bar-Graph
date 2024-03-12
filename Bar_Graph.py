import matplotlib.pyplot as plt
import numpy

barWidth = 0.15
fig = plt.subplots(figsize = (13, 9))

Google = [45, 46, 45]
Youtube = [44, 45, 44]
TikTok = [46, 48, 46]
Dit = [15, 17, 16]

br1 = numpy.arange(len(Google))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]

plt.bar(br1, Google, color= 'b', width= barWidth, edgecolor='black', label='Google')
plt.bar(br2, Youtube, color= 'r', width= barWidth, edgecolor='black', label='Youtube')
plt.bar(br3, TikTok, color= 'grey', width= barWidth, edgecolor='black', label='TikTok')
plt.bar(br4, Dit, color= 'g', width= barWidth, edgecolor='black', label='Dit')

plt.ylabel('ms', fontweight= 'bold', fontsize= 35)
plt.xticks([r + barWidth for r in range(len(Google))], ['MIN', 'MAX', 'AVG'])
plt.legend()
plt.show()
