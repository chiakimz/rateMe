import ijson

amazon_file = 'reviewMeProject/All_Amazon_Review.json'
with open(amazon_file, 'r') as f:
    objects = ijson.items(f, 'item')
    columns = list(objects)
print(columns[0])