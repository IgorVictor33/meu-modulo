from datetime import datetime
dia = datetime.today()
mes = datetime.today().month
ano_atual = datetime.today().year
now = datetime.now()
mes_atual = datetime.month
dia_atual = datetime.day

def calculo_idade(ano_nascimento):
    idade = ano_atual - ano_nascimento
    
    if mes_atual < mes:
        idade = idade -1
    else:
        mes_atual == mes
        
    if dia_atual < dia:
        idade = idade -1
    return idade  
   
