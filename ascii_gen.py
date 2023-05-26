import pywhatkit as kit

def convert_asci():
    kit.image_to_ascii_art("1140587.jpg","ascy")
    f = open("ascy.txt", "r")
    print(f.read())
  
convert_asci()
