from io import BytesIO as _BytesIO
from PIL import Image
import numpy as np
from logger import Logger
import base64
import time
import os


class Converter_ImgToNum:

    def ImgToNum(file_path):
        
        try:
            # To convert Image into Base64 String 
            encoded_string = Converter_ImgToNum.ImgToB64(file_path)
            Logger.write_logs('info', 'Created base64 string')

            # To convert Base64 into Numpy Array
            np_array = Converter_ImgToNum.B64ToNum(encoded_string)
            
            return np_array
        
        except Exception as e:
            
            Logger.write_logs('error', e)
            return e
    
    def ImgToB64(file_path, enc_format="png", verbose=False, **kwargs):

        img = Image.open(file_path)

        # buff object to save image as bytes in memory buffer.
        buff = _BytesIO()

        # saved image into buffer 
        img.save(buff, format=enc_format, **kwargs)

        # Converting image into base64
        encoded = base64.b64encode(buff.getvalue()).decode("utf-8")

        return encoded
    
    def B64ToNum(encoded_string, to_scalar=True): 
        # String: base64 encoded string
        
        # base64 decoding into image
        decoded = base64.b64decode(encoded_string)

        # Saving image bytes into buffer
        buffer = _BytesIO(decoded)
        im = Image.open(buffer)

        # Converting image into numpy array
        np_array = np.asarray(im)

        # to scale values into 0-1
        if to_scalar:
            np_array = np_array / 255.0

        return np_array

class Converter_NumToImg:

    def NumToImg(np_array):
        
        try:
            # To convert np array into Base64
            encoded_string = Converter_NumToImg.NumToB64(np_array)
            Logger.write_logs('info', 'Converted Numpy array to base64 string')

            # To convert Base64 into Image
            filepath = Converter_NumToImg.B64ToImg(encoded_string)

            return filepath
        except Exception as e:

            Logger.write_logs('error',e)

    def NumToB64(np_array, enc_format="png", scalar=True, **kwargs):
        # np_array for convertion

        # Convert from 0-1 to 0-255
        if scalar:
            np_array = np.uint8(255 * np_array)
        else:
            np_array = np.uint8(np_array)

        # Creating image object from nparray
        pil_img = Image.fromarray(np_array)

        # Converting image to Base64
        buff = _BytesIO()
        pil_img.save(buff, format=enc_format, **kwargs)
        encoded = encoded = base64.b64encode(buff.getvalue()).decode("utf-8")

        return encoded

    def B64ToImg(encoded_string, enc_format = 'png'):
        
        decoded = base64.b64decode(encoded_string)

        # Saving decoded bytes into buffer
        buffer = _BytesIO(decoded)
        img = Image.open(buffer)

        # Saving Image into Folder named Images
        filename = input("Enter filename without extension:")
        filename = os.getcwd()+"/images/"+ filename +"."+enc_format

        img.save(filename, enc_format)

        return filename

