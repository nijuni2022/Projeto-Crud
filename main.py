from teste import db



def apaga_um(param):
    db.cadastro.delete_one(param)

def apaga_varios(param):
    db.cadastro.delete_many(param)    

def cria_varios():
    db.cadastro.insert_many([
    
        {"id": 1,"nome":"Andre","sobrenome": "Ramos","idade": 25,"email":"gjfgjk@jkhh.com"},
        {"id": 2,"nome":"Nivaldo","sobrenome": "Junior","idade": 35,"email":"gjfgjk@jkhh.com"},
        {"id": 3,"nome":"Anderson","sobrenome": "Faustino","idade": 27,"email":"gjfgjk@jkhh.com"},
        {"id": 4,"nome":"Joao","sobrenome": "Silva","idade": 45,"email":"gjfgjk@jkhh.com"},
        {"id": 5,"nome":"TESTE","sobrenome": "TESTE","idade": 31,"email":"gjfgjk@jkhh.com"}
        
    ])

def atualiza():
    db.cadastro.update_one()


if __name__=="__main__":
    apaga_um({"id": 1})
    #apaga_varios({})
    #atualiza({})
    #cria_varios()
