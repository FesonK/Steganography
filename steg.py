#python implementing steganography

#Library used to extract pixels from an image
from PIL import Image

#Ask the user for either encode or decode

#Encode
def encode():
    #ask for image
    img = input("Enter image file with extension: ")
    image = Image.open(img, 'r')

    #ask for data to encode
    data = input("Enter text to encode: ")
    if(len(data) == 0):
        raise ValueError("Data is Empty")
    
    #encode image
    cpyimg = image.copy()
    encode_encrypt(cpyimg, data)

    new_img = input("Enter destination to save steganographed image: ")
    new_img.save(new_img, str(new_img.split(".")[1].upper()))




#Decode

#main
def main():
    a = int(input(":: Welcome to Steganography ::\n"
                        "1. Encode\n2. Decode\n"))
    if (a == 1):
        encode()
 
    elif (a == 2):
        print("Decoded Word :  " + decode())
    else:
        raise Exception("Enter correct input")
 
# Driver Code
if __name__ == '__main__' :
 
    # Calling main function
    main()
