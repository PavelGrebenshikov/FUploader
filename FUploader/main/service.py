from os import path

class ProcessingText:
    def __init__(self, file):
        self.verifity = self.validation_to_file(file)
        self.__file = file
         
    def __str__(self):
        return f"{self.__file}"

    def _get_text(self) -> str:
        return self.decode()

    def _read_text(self) -> str:
        return self.__file.read()
    
    def decode(self) -> str:
        return self._read_text().decode("UTF-8")

    def validation_to_file(self, file) -> None:
        # checking the file for extension and size
        if not path.splitext(file.name)[1] in (".txt"):
            raise "Invalid file extension"
        if len(file) == 0 or len(file) < 0:
            raise "The file is empty"
        elif len(file) >= 1000000:
            raise "The file size is too large"
        return "Verification passed"