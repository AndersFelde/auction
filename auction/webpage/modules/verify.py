class Verify():
    def isInt(self, input):
        try:
            int(input)
            return True
        except:
            return False
