from sqlalchemy import create_engine, text
# CRIAR CONEXÃO
engine = create_engine("sqlite:///teste.db", echo = True, future = True)
#CRIAR TABELA
with engine.connect() as conn:
    conn.execute(text("""
                    CREATE TABLE IF NOT EXISTS alunos(
                      id INTEGER  PRIMARY KEY AUTOINCREMENT,
                      nome  VARCHAR(50) NOT NULL,
                      idade INTEGER NOTNULL,
                      email VARCHAR (50) UNIQUE NOT NULL,
                    )                        
                      """))
    conn.commit()
    #INSERIR ALUNOS
    with engine.connect() as conn:
         conn.execute(text("INSERT INTO alunos (nome, idade, email)" "VALUES (:nome, :idade, email )"),
                         [
                             {"nome": "David", "idade": 21, "email": "david@gmail.com"},
                             {"nome": "Geovanni","idade": 25, "email": "geovani@gmail.com"},
                             {"nome": "Silvio","idade": 25, "email": "silvio@gmail.com"}
                          ]         
              
         ) 
         conn.commit()
         with engine.connect() as conn:
              resultado = conn.execute(text("SELECT * FROM alunos"))
              for dado in resultado:
                   print(dado.id, dado.nome, dado.idade, dado.email)