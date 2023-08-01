import pandas as pd

# data = pd.read_csv('weather_data.csv')
#
# data_dict = data.to_dict()
# #print(data_dict)
#
# temp_list =  data['temp'].to_list()
# #print(temp_list)

# sum=0
# for temp in temp_list:
#     sum = sum+temp
# avg = sum/len(temp_list)
# #print(avg)

#print(data[data['day']=='Monday']['temp'])

# data = {
#     'students': ["Amy", "James", "Angela"],
#     "scores": [76,56,65]
# }
#
# data_df = pd.DataFrame(data)
#
# print(data_df)
squirrel = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
#print(squirrel['Primary Fur Color'].value_counts())
# squirrel_count = squirrel['Primary Fur Color'].value_counts().to_frame()
# print(squirrel_count)

gray_squirrel_count= len(squirrel[squirrel['Primary Fur Color'] == 'Gray'])
red_squirrel_count= len(squirrel[squirrel['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count= len(squirrel[squirrel['Primary Fur Color'] == 'Black'])

data_dict = {
    "Fur color":["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}
sf = pd.DataFrame(data_dict)
sf.to_csv('squirrel_count.csv')