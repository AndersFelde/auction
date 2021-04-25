from webpage.submodels.item import Item


class Database():
    def __init__(self):
        pass

    def getAllItems(self):
        return Item.objects.all()

    def getItemById(self, id):
        return Item.objects.filter(id=id)
