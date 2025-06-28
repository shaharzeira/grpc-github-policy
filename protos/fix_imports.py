import fileinput
import glob

for file in glob.glob('pb/*_grpc.py'):
    with fileinput.FileInput(file, inplace=True) as f:
        for line in f:
            print(line.replace('import ', 'from pb import ') if '_pb2' in line else line, end='')
