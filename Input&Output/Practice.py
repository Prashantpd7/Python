with open("Chatgpt.txt","r") as f:
    data = f.read()

new_data = data.replace("Hello","Hii")
print(new_data)

with open("Chatgpt.txt",'w') as f:
    f.write(new_data)