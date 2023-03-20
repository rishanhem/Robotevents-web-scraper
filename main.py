import requests
import csv

numbers = ["1","2","3","4","5","6","7","8","9","0"]


line_count = 0
f = open('vrc1.csv', 'w')
x = open ('vrc.csv', 'r')

csv2 = csv.writer(f,delimiter=',')
csv1 = csv.reader(x, delimiter=',')

for row in csv1:
  if line_count == 0:
    row.append("World skills rank")
    csv2.writerow(row)
    line_count += 1
  else:
    url = "httpsww.robotevents.com/teams/VRC/" + row[0]
    req = requests.get(url)
    content = req.text
    num = content.rfind("<td>")
    for y in range(num+4,num+7):
      if content[y] in numbers:
        max = y + 1
    rank = content[num+4:max]
    row.append(rank)
    csv2.writerow(row)
    line_count += 1
f.close()
x.close()
print(f'Processed {line_count} lines.')

