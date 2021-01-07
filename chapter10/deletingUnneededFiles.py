from pathlib import Path
import pyinputplus as pyip
import os

for subdir, dirs, file in os.walk(Path.cwd):
    size = os.path.getsize(str(subdir, file))
    
    if size > 1000000 :
        print(Path(subdir, file, '-->' , size))
        ques = 'Do you want to delete this file?'
        response = pyip.inputYesNo(ques)
    
        if response == 'yes':
            os.unlink(file)
        else:
            continue