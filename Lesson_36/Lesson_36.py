import json
jdata = {
    "people" : [{
        "firstname" : "Akmalbek",
        "lastname" : "Abdurakh",
        "Location" : ["Tashkent", "Kirgiston"]
    },{
        "firstname" : "Benjamin",
        "lastname" : "Tate",
        "Location" : ["London", "Wales"]
    }
    ]
}
for x in jdata["people"]:
    print("His mom lives in",x["Location"][0])
    print("His dad lives in",x["Location"][1])
data_dict = """JSON (англ. JavaScript Object Notation, обычно произносится как) -
текстовый формат обмена данными,
 основанный на JavaScript. Как и многие другие текстовые форматы, 
JSON легко читается людьми. Формат JSON был разработан Дугласом Крокфордом.
"""

"""
Python              JSON
dict              object
list,tuple          array
str                  string
int,long,float      number
True              true
False              false
None              null

"""
convert = {}
with open("semester_1\Lesson_36\json_data.json", "r") as file:
    countries = json.load(file)
with open("semester_1\Lesson_36\city.json", "r") as file:
    cities = json.load(file)
    counter = 0
    for x in countries:
        x["city"] = cities[counter]["city"]
        counter += 1
    countries = json.dumps(countries)
countries = json.loads(countries)
print(countries)
with open("semester_1\Lesson_36\json_data.json", "w") as file:
    json.dump(countries,file)

# json.loads
# json.sortkeys()
