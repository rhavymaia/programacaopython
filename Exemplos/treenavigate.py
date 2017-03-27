# Import the os module, for the os.walk function
import os

# Set the directory you want to start from
rootDir = 'C:\\Users\\Rhavy\\OneDrive\\Documentos\\IFPB\\Projeto NutrIF\\Sistema\\Fotos\\temp'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)


file_path = "C:\\Python\\Nutrif\\fotos"
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)