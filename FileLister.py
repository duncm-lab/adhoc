import os

class Filelister():
  
    def __init__(self, directory='/tmp'):
        self._directory = directory
        self.fileList = []
        self._populateFileList()
        
    def _populateFileList(self):
        for i,j,k in os.walk(self._directory):
            for m in k:
                f = os.path.join(i,m)
                self.fileList.append(f)
