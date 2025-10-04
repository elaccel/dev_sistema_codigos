#02/10/25

from sqlalchemy import create_engine, \
Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, \
sessionmaker, relationship

# method factory (fabrica de classes)
Base = declarative_base()

# criar classe "real"(vai ser a tabela pelo ORM)
class Aluno(Base):
    __tablename__ = 'alunos'

    id = Column(Integer, primary_key=True, \
                autoincrement=True)
    nome = Column(String(62), nullable=False)
    idade = Column(Integer, nullable=False)
    email = Column(String(62), unique=True, \
                   nullable=False)
    # back_populates -> referencia reciproca , quando vc associa aluno a AlunoDisciplina
    # e AlunoDisciplina, é associada a Aluno

    desciplinas = relationship('AlunoDisciplina', back_populates='Aluno')
    
    # metodo magico (printar um objeto)
    def __repr__(self):
        return f"<Aluno(id={self.id},  nome='{self.nome}',idade={self.idade}, email='{self.email}')>"
       
         
     # ---------------------------------------------------------------------
    class Disciplina(Base):
        __tablename__ = 'disciplina'
        id = Column(Integer, primary_key=True,  autoincrement=True,)
        nome = Column(String(62), nullable=False, unique=True)
        caragaHoraria = Column('cargaHoararia' , Integer,nullable=False)
        CheckConstraint('cargaHoraria >0')



        def__repr__(self):
            return f"<Disciplina(id={self.id},nome ='{self.nome}', cargaHoraria={self.cargaHoraria})>"

      #-----------------------------------------------
       class AlunoDisciplina(base):
        __tablename__ = 'alunodisciplina'
        id = Column(Integer, primary_key=True, autoincrement=True)
        id_aluno_fk = Column(Integer,ForeignKey('alunos.id'),nullable=False)
        id_disciplina_fk = Column(Integer, ForeignKey('disciplina.id'),nullable=False)           

        aluno= relationship('Aluno', back_populates='disciplina')
        Disciplina = relationship('Disciplina',back_populates= 'alunos')



# criar engine (cria conexão com o BD)
engine = create_engine("sqlite:///tec_dev.db",\
                       echo=True, future=True)

# criar a sessão (isso conecta o engine ao ORM)
Session = sessionmaker(bind=engine,future=True)

# criar as tabelas
Base.metadata.create_all(engine)

# Insert -> inserir alunos na tabela
with Session() as session:
    alunos = [
        Aluno(nome='David', idade=21, \
              email='davidvarao@senai.br'),
        Aluno(nome='Geovanni', idade=23, \
              email='geovanicuricica@senai.br'),
        Aluno(nome='Silvio', idade= 25, \
              email='silviogaladaglobo@senai.br')
    ]
    session.add_all(alunos)
    # session.add(alunos[1])
    session.commit()

with Session() as session:
    bd Disciplina(nome='Banco de Dados', cargaHoraria=-80)


# fazer select - consultar o banco
with Session() as session:
    resultado = session.query(Aluno).all()

    for aluno in resultado:
        print(aluno.id, aluno.nome, \
              aluno.idade, aluno.email)
