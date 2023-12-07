class UndoRedoManger:
    def __init__(self):
        self.nextImages = []
        self.previousImages = []

    def undo(self):
        if len(self.previousImages) > 300:
            self.previousImages.pop(0)
        image = self.previousImages.pop() if self.previousImages else None
        return image

    def redo(self):
        if len(self.nextImages) > 300:
            self.nextImages.pop(0)
        image = self.nextImages[len(self.nextImages) - 1]
        self.nextImages.pop()
        return image

    def get_next_images(self):
        return self.nextImages

    def get_previous_images(self):
        return self.previousImages

    def add_previous_images(self, qImage):
        self.previousImages.append(qImage)

        if len(self.previousImages) > 300:
            self.previousImages.pop(0)
        print("Length previousImages: " + str(len(self.previousImages)))

    def add_next_images(self, qImage):
        self.nextImages.append(qImage)

        if len(self.nextImages) > 300:
            self.nextImages.pop(0)
        print("Length nextImages: " + str(len(self.nextImages)))

    def reset_next_images(self):
        self.nextImages = []

    def reset_previous_images(self):
        self.previousImages = []
