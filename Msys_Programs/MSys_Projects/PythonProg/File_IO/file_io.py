with open("file.txt","r") as file:
    b = file.readlines()
    print(b)

# # a - appends to, preserving orignal contents
# # NO CONTROL OVER CURSOR
# # with open("FILE.txt","a") as file:
# #     file.seek(0)
# #     file.write("APPENDIG LATER!!!")

# # r+ 
# # with open("file.txt", "r+")as file:
# #     file.write(":)")
# #     file.seek(10)
# #     file.write(":(")

# # r+ will not create a file if it doesn't exist
# with open("hello.txt", "a") as file:
#     file.write("HELLO!!!")
