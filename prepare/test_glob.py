from glob import glob
RESOURCES_PATH = 'D:/LUNA16_Dataset/LUNA16_Dataset\subset0'
paths = glob(RESOURCES_PATH+'/'+'*.mhd')
# files = glob('D:/LUNA16_Dataset/subset0/*.mhd', recursive = True)

for path in paths:
    print('paths \n\n', path)