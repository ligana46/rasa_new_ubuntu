import json
import unidecode


class UtilitiesJSON:
    jsonData = ""

    def __init__(self, path="data/LIBdata.json"):
        # body of the constructor
        f = open(path, encoding="utf8")

        # returns JSON object as
        # a dictionary
        self.jsonData = json.load(f)
        f.close()

    def getKeyWord(self, keyword):
        for data in self.jsonData:
            for kw in data["kw"]:
                unaccented_keyword = unidecode.unidecode(keyword)
                unaccented_kw = unidecode.unidecode(kw)
                if unaccented_keyword.lower() in unaccented_kw.lower():
                    return data
        return None
