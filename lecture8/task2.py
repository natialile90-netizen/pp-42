student = {
    "name": "Ana" ,
    "age" : 20 ,
    "contacts": {
        "email" : "ana@example.com" ,
        "phone" :  "599123456"
    } ,
    "courses" : {
        "python" : {
            "score" : 95,
            "passed" : True
        },
        "web" : {
            "score" : 58,
            "passed" : False

        },
    }
}
print (student ["contacts"]["email"])

print (student ["courses"]["python"]["score"])

student ["courses"]["web"]["passed"]=True
student ["courses"]["web"]["score"]=65

phone = student ["contacts"] .pop("phone")

print(student)