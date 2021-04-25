from django.shortcuts import render
from webpage.modules.database import Database


#  from webpage.models import TestModal
def item(request, itemId):
    print(itemId)
    db = Database()
    item = db.getItemById(itemId)
    return render(request,
                  'webpage/item.html',
                  context={
                      'itemId': itemId,
                      "items": item
                  })
