from os import path
from string import ascii_letters


def processong_text(file, options):
    
    
    def validation_to_file(file):
        if not path.splitext(file.name)[1] in (".txt"):
            raise "Invalid file extension"
        if len(file) == 0 or len(file) < 0:
            raise "The file is empty"
        elif len(file) >= 1000000:
            raise "The file size is too large"
        return ("Verification passed", True)

    if True in validation_to_file(file=file):
        _file = file.read().decode('utf-8')
        if options == "d_space":
            _file = _file.replace('\n', ' ').replace(' ', '')
            return _file.rstrip().strip().rstrip()
        elif options == "d_symbols":
            pass
    
    
    
    

# class ProcessingText:
#     def __init__(self, file):
#         self.verifity = self.validation_to_file(file)
#         self.__file = file
         
#     def __str__(self):
#         return f"{self.__file}"

#     def _get_text(self) -> str:
#         return self.decode()

#     def _read_text(self) -> str:
#         return self.__file.read()
    
#     def decode(self) -> str:
#         return self._read_text().decode("UTF-8")