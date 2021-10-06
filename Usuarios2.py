from Banco2 import Banco


class Usuarios(object):


  def __init__(self, id = "", cpf= "", nome = "", fone = "", email = "", guiche = ""):
    self.info = {}
    self.id = id
    self.cpf = cpf
    self.nome = nome
    self.fone = fone
    self.email = email
    self.guiche = guiche
    
    
    


  def insertUser(self):

    banco = Banco()
    try:
      c = banco.conexao.cursor()

      c.execute("INSERT INTO morador(cpf, nome, fone, email, guiche) VALUES  ('" + self.cpf + "', '" + self.nome + "', '" + self.fone + "', '" + self.email + "', '" + self.guiche +"' )")
      #"'" + cpf + "', '" + nome + "', '"
      banco.conexao.commit()
      c.close()


      return "Usuário cadastrado com sucesso!"
    except:
      return "Atenção: Ocorreu um erro na inserção do usuário" 

  def updateUser(self):

    banco = Banco()
    try:

        c = banco.conexao.cursor()

        c.execute("UPDATE morador SET cpf = '" + self.cpf + "', nome = '" + self.nome + "', fone = '" + self.fone + "', email = '" + self.email +
         "' , guiche = '" + self.guiche + "' WHERE id = '" + self.id + "' ")

        '''"UPDATE  morador set WHERE cpf = '" + self.cpf +
       "', nome = '" + self.nome + "', casa = '" + self.casa + "', rg = '" + self.rg + "' , email ='" + self.email + "', fone ='" + self.fone 
       + "', placa='" + self.placa + "', modelo='" + self.modelo + "', data='" + self.data + " ")'''

        banco.conexao.commit()
        c.close()

        return "Usuário atualizado com sucesso!"
    except:
        return "Ocorreu um erro na alteração do usuário"

 
  def deleteUser(self):

    banco = Banco()
    try:

        c = banco.conexao.cursor()

        c.execute("delete from morador where cpf = '" + self.cpf + "' ")

        banco.conexao.commit()
        c.close()

        return "Usuário excluído com sucesso!"
    except:
        return "Ocorreu um erro na exclusão do usuário"

  def selectUser(self, pesquisandou,pesquisado):
    banco = Banco()
    try:

        c = banco.conexao.cursor()

        c.execute("SELECT * FROM morador WHERE " + pesquisandou + " = '" + pesquisado + "'")

        #lista = c.FETCHALL()
        #lista=c.execute("""SELECT cpf, nome, casa, rg, email, fone, placa, modelo, data FROM morador ORDER BY nome ASC """)
        
        for linha in c:
            self.cpf = linha[0]
            self.nome = linha[1]
            self.casa = linha[2]
            self.rg = linha[3]
            self.email = linha[4]
            self.fone = linha[5]
            self.placa=linha[6]
            self.modelo=linha[7]
            self.data=linha[8]
            
            
        c.close()
        return "Busca feita com sucesso!"
    except:
        return "Ocorreu um erro na busca do usuário"

  def selectidic(self, tb_movimento):
    banco = Banco()

    try:

      c = banco.conexao.cursor()

      c.execute("SELECT * FROM morador WHERE guiche = 0 ORDER BY id ")

      tb_movimento.delete(*tb_movimento.get_children())


      #tb_movimento.delete(*tb_movimento.get_children())
      for linha in c:
        self.cpf = linha[0]
        self.nome = linha[1]
        self.fone = linha[2]
        self.email = linha[3]
        self.guiche = linha[4]
        self.id = linha[5]

        tb_movimento.insert("","end",values=(self.id,self.cpf,self.nome,self.fone,self.email,self.guiche))

      c.close()
      return "Atualizado com sucesso!"
    except banco.conexao.Error as error:
      return "Ocorreu um erro na atualização"

  def selesenhas(self, tb_movimento2):
    banco = Banco()

    try:

      c = banco.conexao.cursor()

      c.execute("SELECT * FROM morador WHERE guiche > 0 ORDER BY id DESC")

      tb_movimento2.delete(*tb_movimento2.get_children())


      #tb_movimento.delete(*tb_movimento.get_children())
      for linha in c:
        self.cpf = linha[0]
        self.nome = linha[1]
        self.fone = linha[2]
        self.email = linha[3]
        self.guiche = linha[4]
        self.id = linha[5]

        tb_movimento2.insert("","end",values=(self.id,self.nome,self.guiche))

      c.close()
      return "Atualizado com sucesso!"
    except banco.conexao.Error as error:
      return "Ocorreu um erro na atualização"
 