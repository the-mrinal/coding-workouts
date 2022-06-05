class TextEditor:

    def __init__(self):
        self.notepad = ""
        self.index = 0
        

    def addText(self, text: str) -> None:
        before_text = self.notepad[:self.index]
        after_text =  self.notepad[self.index:]
        self.notepad = before_text + text + after_text
        self.index = len(before_text) + len(text)
 
    def deleteText(self, k: int) -> int:
        leftBound = self.index - k if self.index - k >= 0 else 0
        before_text = self.notepad[:leftBound]
        deletedText = self.notepad[ leftBound:self.index]
        self.notepad = before_text + self.notepad[self.index:]
        self.index = len(before_text)
        return len(deletedText)

    def cursorLeft(self, k: int) -> str:
        leftBound = self.index  - k if self.index - k >= 0 else 0
        self.index = leftBound
        before_text = self.notepad[:leftBound]
        if len(before_text) > 10:
            return before_text[len(before_text) - 10:]
        return before_text
            

    def cursorRight(self, k: int) -> str:
        rightBound = self.index + k if self.index + k < len(self.notepad) else len(self.notepad)
        self.index = rightBound
        before_text = self.notepad[:rightBound]
        if len(before_text) > 10:
            return before_text[len(before_text) - 10:]
        return before_text


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)