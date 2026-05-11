import pandas

data = pandas.read_csv("C:/Users/Nathan/Desktop/The Complete Guide to Python/Angela Yu Python Programming/Python Projects/Squirrel Data/squirrel_data.csv")

fur_color = []
gray_count = 0
cinnamon_count = 0
black_count = 0

for color in data["Primary Fur Color"]:
  if color == 'Gray':
    gray_count += 1
  elif color == 'Cinnamon':
    cinnamon_count += 1
  elif color == 'Black':
    black_count += 1

  if color in fur_color:
    pass
  else:
    fur_color.append(color)

fur_color[2] = 'Red'

fur_count = []
fur_count.append(gray_count)
fur_count.append(cinnamon_count)
fur_count.append(black_count)



data_dict = {
  'Fur Color' : fur_color[1:],
  'Count' : fur_count
}

final_data = pandas.DataFrame(data_dict)
final_data.to_csv("C:/Users/Nathan/Desktop/The Complete Guide to Python/Angela Yu Python Programming/Python Projects/Squirrel Data/squirrel_count.csv")