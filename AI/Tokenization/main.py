import  tiktoken

enc  = tiktoken.encoding_for_model("gpt-4o")
text = "Hey There! My name is Yuvraj Soni"
token = enc.encode(text)
print(token)



decoded = enc.decode(token)
print(decoded)