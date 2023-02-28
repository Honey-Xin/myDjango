# result = [('adfas',[(1,2,3,4),(2,3,4,5),(3,4,5,6),(4,5,6,7)])]
# data = {"matches": []}
# for item in result[0][1]:
#     data_item = {
#         "message": item[0],
#         "short_message": "Uppercase",
#         "offset": 45,
#         "length": "len(item[1])",
#         "context": {
#             "text": item[1],
#             "offset": item[2]
#         },
#         "replacements": [
#             "Word"
#         ],
#     }
#     data["matches"].append(data_item)

a = []
a.extend(['asfdasdf',"jhghfghfh"])
print(a)
a = ''.join(a)
print(a)