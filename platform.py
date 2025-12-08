from platformio.public import PlatformBase

class VignisPlatform(PlatformBase):
    def is_embedded(self):
        return True
