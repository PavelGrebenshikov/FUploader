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
        _file = str(file.read().decode('Windows-1251'))
        if options == "r_spaces":
            return _file.replace('\n', '').replace(' ', '')
        if options == "d_char":
            content = "".join(c for c in _file if c.isalpha())
            return content
        if options == "s_text":
            return _file
    
    
    
    

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