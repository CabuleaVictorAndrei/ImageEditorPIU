class UndoRedoManger:
    def __init__(self):
        self.nextImages = []
        self.previousImages = []

    def undo(self):
        image = self.previousImages[len(self.previousImages) - 1]
        self.previousImages.pop()
        return image

    def redo(self):
        image = self.nextImages[len(self.nextImages) - 1]
        self.nextImages.pop()
        return image

    def get_next_images(self):
        return self.nextImages

    def get_previous_images(self):
        return self.previousImages
