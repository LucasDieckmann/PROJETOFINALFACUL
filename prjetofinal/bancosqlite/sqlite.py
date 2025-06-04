from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
db = create_engine('sqlite:///brawlhalla.db')  
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Brawlhalla(Base):  
    __tablename__ = 'brawlhalla' 
    id = Column(Integer, primary_key=True, autoincrement=True) 
    personagens = Column(String, nullable=False)
    preco = Column(Integer, nullable=False)
    
    forca = Column(Integer,)
    defesa = Column(Integer,)
    destreza = Column(Integer,)
    agilidade = Column(Integer,)
    
    armaum = Column(String(50)) 
    armadois = Column(String(50))

    def __init__(self, personagens, preco, forca, defesa, destreza, agilidade, armaum, armadois):
        self.personagens = personagens
        self.preco = preco
        self.forca = forca
        self.defesa = defesa
        self.destreza = destreza
        self.agilidade = agilidade
        self.armaum = armaum
        self.armadois = armadois


Base.metadata.create_all(bind=db)

brawlhalla1 = Brawlhalla(personagens='Bodvar', preco=900, forca=6, defesa=5, destreza=6, agilidade=5, armaum='Martelo', armadois='Espada')
brawlhalla2 = Brawlhalla(personagens='Cassidy', preco=2300, forca=6, defesa=4, destreza=8, agilidade=4, armaum='Pistolas', armadois='Martelo')
brawlhalla3 = Brawlhalla(personagens='Orion', preco=2300, forca=4, defesa=6, destreza=6, agilidade=6, armaum='Foguete', armadois='Lança')
brawlhalla4 = Brawlhalla(personagens='Lord', preco=2300, forca=4, defesa=4, destreza=8, agilidade=6, armaum='Foguete', armadois='Arma')
brawlhalla5 = Brawlhalla(personagens='Gnash', preco=2300, forca=7, defesa=5, destreza=3, agilidade=7, armaum='Martelo', armadois='Lança')
brawlhalla6 = Brawlhalla(personagens='Queen', preco=2300, forca=7, defesa=8, destreza=4, agilidade=3, armaum='Lança', armadois='Adagas')
brawlhalla7 = Brawlhalla(personagens='Hatori', preco=2300, forca=4, defesa=4, destreza=6, agilidade=8, armaum='Espada', armadois='Lança')
brawlhalla8 = Brawlhalla(personagens='Sir Roland', preco=2300, forca=5, defesa=8, destreza=5, agilidade=4, armaum='Foguete', armadois='Espada')
brawlhalla9 = Brawlhalla(personagens='Scarlet', preco=3900, forca=8, defesa=5, destreza=5, agilidade=4, armaum='Martelo', armadois='Foguete')
brawlhalla10 = Brawlhalla(personagens='Thatch', preco=3900, forca=7, defesa=3, destreza=5, agilidade=7, armaum='Espada', armadois='Arma')
brawlhalla11 = Brawlhalla(personagens='Ada', preco=3900, forca=6, defesa=3, destreza=7, agilidade=6, armaum='Arma', armadois='Lança')
brawlhalla12 = Brawlhalla(personagens='Sentinel', preco=2300, forca=5, defesa=7, destreza=4, agilidade=6, armaum='Martelo', armadois='Adagas')
brawlhalla13 = Brawlhalla(personagens='Lucien', preco=2300, forca=3, defesa=6, destreza=5, agilidade=8, armaum='Adagas', armadois='Arma')
brawlhalla14 = Brawlhalla(personagens='Teros', preco=3900, forca=8, defesa=6, destreza=3, agilidade=5, armaum='Machado', armadois='Martelo')
brawlhalla15 = Brawlhalla(personagens='Bryann', preco=900, forca=5, defesa=5, destreza=5, agilidade=7, armaum='Machado', armadois='Lança')
brawlhalla16 = Brawlhalla(personagens='Asuri', preco=3900, forca=4, defesa=5, destreza=7, agilidade=6, armaum='Adagas', armadois='Espada')
brawlhalla17 = Brawlhalla(personagens='Barraza', preco=3900, forca=6, defesa=8, destreza=4, agilidade=4, armaum='Machado', armadois='Arma')
brawlhalla18 = Brawlhalla(personagens='Ember', preco=900, forca=6, defesa=3, destreza=6, agilidade=7, armaum='Arco', armadois='Adagas')
brawlhalla19 = Brawlhalla(personagens='Azoth', preco=5400, forca=7, defesa=6, destreza=5, agilidade=4, armaum='Arco', armadois='Machado')
brawlhalla20 = Brawlhalla(personagens='Koji', preco=5400, forca=5, defesa=4, destreza=8, agilidade=5, armaum='Arco', armadois='Espada')
brawlhalla21 = Brawlhalla(personagens='Ulgrim', preco=5400, forca=6, defesa=7, destreza=3, agilidade=6, armaum='Machado', armadois='Foguete')
brawlhalla22 = Brawlhalla(personagens='Diana', preco=5400, forca=5, defesa=5, destreza=6, agilidade=6, armaum='Arco', armadois='Arma')
brawlhalla23 = Brawlhalla(personagens='Jhala', preco=5400, forca=7, defesa=3, destreza=7, agilidade=5, armaum='Machado', armadois='Espada')
brawlhalla24 = Brawlhalla(personagens='Kor', preco=5400, forca=6, defesa=7, destreza=5, agilidade=4, armaum='Luva', armadois='Martelo')
brawlhalla25 = Brawlhalla(personagens='Wu Shang', preco=5400, forca=5, defesa=5, destreza=7, agilidade=5, armaum='Luva', armadois='Lança')
brawlhalla26 = Brawlhalla(personagens='Val', preco=5400, forca=4, defesa=6, destreza=5, agilidade=7, armaum='Luva', armadois='Espada')
brawlhalla27 = Brawlhalla(personagens='Ragnir', preco=5400, forca=5, defesa=6, destreza=6, agilidade=5, armaum='Adagas', armadois='Machado')
brawlhalla28 = Brawlhalla(personagens='Cross', preco=5400, forca=7, defesa=6, destreza=4, agilidade=5, armaum='Arma', armadois='Luva')
brawlhalla29 = Brawlhalla(personagens='Mirage', preco=5400, forca=7, defesa=4, destreza=6, agilidade=5, armaum='Foice', armadois='Lança')
brawlhalla30 = Brawlhalla(personagens='Nix', preco=5400, forca=4, defesa=7, destreza=5, agilidade=6, armaum='Foice', armadois='Arma')
brawlhalla31 = Brawlhalla(personagens='Mordex', preco=5400, forca=5, defesa=5, destreza=4, agilidade=7, armaum='Foice', armadois='Luva')
brawlhalla32 = Brawlhalla(personagens='Yumiko', preco=5400, forca=4, defesa=4, destreza=7, agilidade=7, armaum='Arco', armadois='Martelo')
brawlhalla33 = Brawlhalla(personagens='Artemis', preco=5400, forca=5, defesa=4, destreza=5, agilidade=7, armaum='Foguete', armadois='Foice')
brawlhalla34 = Brawlhalla(personagens='Caspian', preco=5400, forca=7, defesa=4, destreza=5, agilidade=6, armaum='Luva', armadois='Adagas')
brawlhalla35 = Brawlhalla(personagens='Sidra', preco=5400, forca=6, defesa=6, destreza=4, agilidade=6, armaum='Canhão', armadois='Espada')
brawlhalla36 = Brawlhalla(personagens='Xull', preco=5400, forca=9, defesa=5, destreza=4, agilidade=4, armaum='Canhão', armadois='Machado')
brawlhalla37 = Brawlhalla(personagens='Kaya', preco=5400, forca=4, defesa=7, destreza=4, agilidade=7, armaum='Lança', armadois='Arco')
brawlhalla38 = Brawlhalla(personagens='Isaiah', preco=5400, forca=5, defesa=7, destreza=6, agilidade=4, armaum='Canhão', armadois='Arma')
brawlhalla39 = Brawlhalla(personagens='Iiro', preco=5400, forca=5, defesa=3, destreza=7, agilidade=7, armaum='Espada', armadois='Foice')
brawlhalla40 = Brawlhalla(personagens='Lin Fei', preco=5400, forca=3, defesa=4, destreza=8, agilidade=7, armaum='Adagas', armadois='Canhão')
brawlhalla41 = Brawlhalla(personagens='Zariel', preco=5400, forca=7, defesa=7, destreza=4, agilidade=4, armaum='Luva', armadois='Arco')
brawlhalla42 = Brawlhalla(personagens='Rayman', preco=5400, forca=5, defesa=6, destreza=5, agilidade=6, armaum='Luva', armadois='Machado')
brawlhalla43 = Brawlhalla(personagens='Dusk', preco=5400, forca=6, defesa=4, destreza=7, agilidade=5, armaum='Lança', armadois='Orbe')
brawlhalla44 = Brawlhalla(personagens='Fait', preco=5400, forca=7, defesa=4, destreza=4, agilidade=7, armaum='Foice', armadois='Orbe')
brawlhalla45 = Brawlhalla(personagens='Thor', preco=5400, forca=6, defesa=6, destreza=4, agilidade=6, armaum='Martelo', armadois='Orbe')
brawlhalla46 = Brawlhalla(personagens='Petra', preco=5400, forca=9, defesa=4, destreza=4, agilidade=6, armaum='Luva', armadois='Orbe')
brawlhalla47 = Brawlhalla(personagens='Vector', preco=5400, forca=5, defesa=6, destreza=4, agilidade=7, armaum='Foguete', armadois='Arco')
brawlhalla48 = Brawlhalla(personagens='Volkov', preco=5400, forca=4, defesa=6, destreza=8, agilidade=4, armaum='Machado', armadois='Foice')
brawlhalla49 = Brawlhalla(personagens='Onyx', preco=5400, forca=5, defesa=8, destreza=4, agilidade=5, armaum='Luva', armadois='Canhão')
brawlhalla50 = Brawlhalla(personagens='Jaeyun', preco=5400, forca=6, defesa=5, destreza=5, agilidade=6, armaum='Espada', armadois='Espadão')
brawlhalla51 = Brawlhalla(personagens='Mako', preco=5400, forca=6, defesa=4, destreza=4, agilidade=8, armaum='Adagas', armadois='Espadão')
brawlhalla52 = Brawlhalla(personagens='Magnar', preco=5400, forca=5, defesa=9, destreza=4, agilidade=4, armaum='Martelo', armadois='Espadão')
brawlhalla53 = Brawlhalla(personagens='Reno', preco=5400, forca=4, defesa=6, destreza=7, agilidade=5, armaum='Arma', armadois='Orbe')
brawlhalla54 = Brawlhalla(personagens='Munin', preco=5400, forca=5, defesa=4, destreza=6, agilidade=7, armaum='Arco', armadois='Foice')
brawlhalla55 = Brawlhalla(personagens='Arcadia', preco=5400, forca=7, defesa=4, destreza=7, agilidade=4, armaum='Lança', armadois='Espadão')
brawlhalla56 = Brawlhalla(personagens='Ezio', preco=5400, forca=5, defesa=4, destreza=7, agilidade=6, armaum='Espada', armadois='Orbe')
brawlhalla57 = Brawlhalla(personagens='Tezca', preco=5400, forca=7, defesa=5, destreza=5, agilidade=5, armaum='Bota', armadois='Luva')
brawlhalla58 = Brawlhalla(personagens='Thea', preco=5400, forca=4, defesa=3, destreza=6, agilidade=9, armaum='Bota', armadois='Foguete')
brawlhalla59 = Brawlhalla(personagens='Red Raptor', preco=5400, forca=6, defesa=4, destreza=6, agilidade=6, armaum='Bota', armadois='Orbe')
brawlhalla60 = Brawlhalla(personagens='Loki', preco=5400, forca=4, defesa=5, destreza=8, agilidade=5, armaum='Adagas', armadois='Foice')
brawlhalla61 = Brawlhalla(personagens='Seven', preco=5400, forca=7, defesa=8, destreza=3, agilidade=4, armaum='Lança', armadois='Canhão')
brawlhalla62 = Brawlhalla(personagens='Vivi', preco=5400, forca=6, defesa=4, destreza=5, agilidade=7, armaum='Bota', armadois='Arma')
brawlhalla63 = Brawlhalla(personagens='Imugi', preco=5400, forca=8, defesa=8, destreza=3, agilidade=3, armaum='Machado', armadois='Espadão')
brawlhalla64 = Brawlhalla(personagens='King Zuva', preco=5400, forca=8, defesa=6, destreza=4, agilidade=4, armaum='Martelo', armadois='Bota')
brawlhalla65 = Brawlhalla(personagens='Priya', preco=7400, forca=4, defesa=5, destreza=6, agilidade=7, armaum='Chakram', armadois='Espada')
session.add_all([
    brawlhalla1, brawlhalla2, brawlhalla3, brawlhalla4, brawlhalla5, 
    brawlhalla6, brawlhalla7, brawlhalla8, brawlhalla9, brawlhalla10,
    brawlhalla11, brawlhalla12, brawlhalla13, brawlhalla14, brawlhalla15,
    brawlhalla16, brawlhalla17, brawlhalla18, brawlhalla19, brawlhalla20,
    brawlhalla21, brawlhalla22, brawlhalla23, brawlhalla24, brawlhalla25,
    brawlhalla26, brawlhalla27, brawlhalla28, brawlhalla29, brawlhalla30,
    brawlhalla31, brawlhalla32, brawlhalla33, brawlhalla34, brawlhalla35,
    brawlhalla36, brawlhalla37, brawlhalla38, brawlhalla39, brawlhalla40,
    brawlhalla41, brawlhalla42, brawlhalla43, brawlhalla44, brawlhalla45,
    brawlhalla46, brawlhalla47, brawlhalla48, brawlhalla49, brawlhalla50,
    brawlhalla51, brawlhalla52, brawlhalla53, brawlhalla54, brawlhalla55,
    brawlhalla56, brawlhalla57, brawlhalla58, brawlhalla59, brawlhalla60,
    brawlhalla61, brawlhalla62, brawlhalla63, brawlhalla64, brawlhalla65
])
session.commit()
print("Todos os 65 personagens foram inseridos com sucesso!")

