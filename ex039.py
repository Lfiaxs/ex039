from datetime import date
atual = date.today().year
nasc = int(input('Qual ano do seu nascimento? '))
idade = atual - nasc
print ('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))
if idade < 18:
    print ('Você ainda não está na idade correta para se alistar ao serviço militar, faltam {} ano(os).'.format(18 - idade))
elif idade == 18:
    print ('É a hora de se alistar ao serviço militar!')
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
