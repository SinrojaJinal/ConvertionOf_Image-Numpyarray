from Converter import Converter_ImgToNum, Converter_NumToImg
from logger import Logger

filepath = input("Enter Image path:")
Logger.write_logs('info', 'Convertion Started......')
Numpy_Array = Converter_ImgToNum.ImgToNum(filepath)
print(Numpy_Array)
Logger.write_logs('info', 'Successful Convertion!!!')

Logger.write_logs('info', 'Convertion Started......')
file_path = Converter_NumToImg.NumToImg(Numpy_Array)
print(file_path)
Logger.write_logs('info', 'Successful Convertion!!!')