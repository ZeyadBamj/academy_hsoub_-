class VideoFile:
    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def save():
        print("Saving....")


class OggCodec:
    pass

class MPEG4Codec:
    pass

class CodecFactory:
    @staticmethod
    def extract(file):
        print("Extracting....")
        return file, "With Codec"

class BitRender:
    @staticmethod
    def read(filename, src):
        print("Reading....", filename)
        return filename

    @staticmethod
    def convert_br(buffer, dest):
        print("Convert.....", buffer)

class AudioMixer:
    @staticmethod
    def fix(file):
        print("Fixing....")
        return "Fixed File Name=", file


class VideConverterFacade:
    @staticmethod
    def convert(filename, formate):
        file = VideoFile(filename)
        sourceCodec = CodecFactory.extract(file)
        if formate == "mp4":
            dest = MPEG4Codec()
        else:
            dest = OggCodec()

        buffer = BitRender.read(filename, sourceCodec)
        result = BitRender.convert_br(buffer, dest)
        result = (AudioMixer()).fix(result)
        return VideoFile(result)

class Application:
    @staticmethod
    def main():
        convertor = VideConverterFacade()
        mp4 = convertor.convert("Movie.ogg", "mp4")
        mp4.save()


if __name__ == "__main__":
    Application.main()