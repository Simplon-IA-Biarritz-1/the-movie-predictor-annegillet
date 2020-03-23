class Cleaning:

    def __init__(self):
        pass
    
    def spliter(self, data, key):
        data[key] = data[key].split("_")
        return data
        
    def integer(self, data, key):
        if data[key] != "\\N":
            data[key] = int(data[key])
        return data
    
    def replace_nan(self, data, key):
        if data[key] == "\\N":
            data[key] = data.update(key = "")
        return data

    def replace_id_tconst(self, data):
        data["_id"] = data["tconst"]
        del data["tconst"]
        return data

    def replace_id_nconst(self, data):
        data["_id"] = data["nconst"]
        del data["nconst"]
        return data


#test_liste = {"_id": "5e4e8557abd9601c864f67d7", "tconst": "tt0000001", "averageRating": "5.6", "numVotes": "1584", "test" : "\\N"}

#test_liste = Names(test_liste)
#test_liste.replace_nan(test_liste, key="test")

#test_liste["_id"] = test_liste["tconst"]
#del test_liste["tconst"]

#print(test_liste)
