def cats():
    cat =  {
          'voto ind': lambda x : 'indeciso' if x==4 else 
                                 'ninguem' if x==3 else
                                 'não respondeu' if x==5 else
                                 'candidato ' + str(x),
               'sexo': lambda x :'masculino' if x==1 else 
                                 'feminino' if x==2 else 
                                 'indefinido' if x==3 else None,
        'escolaridade': lambda x : 'analfabeto' if x==1 else 
                                 'f incompleto' if x==2 else 
                                 'f completo' if x==3 else 
                                 'm incompleto' if x==4 else 
                                 'm completo' if x==5 else 
                                 's incompleto' if x==6 else 
                                 's completo' if x==7 else 
                                 'pos-grad' if x==8 else None,
        'renda ind': lambda x : 'até 1 salário' if x==1 else 
                                 '1 a 2 salários' if x==2 else 
                                 '2 a 5 salários' if x==3 else 
                                 '3 a 10 salários' if x==4 else 
                                 '10 a 20 salários' if x==5 else 
                                 '+20 salários' if x==6 else 
                                 'sem rendimento' if x==7 else 
                                 'não respondeu'if x==8 else None,
              'idade' : lambda x : '16 a 18' if x==1 else 
                                 '18 a 25' if x==2 else 
                                 '25 a 30' if x==3 else 
                                 '30 a 40' if x==4 else 
                                 '40 a 50' if x==5 else 
                                 '50 a 60' if x==6 else
                                 '60+' if x==7 else None,
              'religiao' : lambda x : 'Catolica' if x==1 else \
                                    'Protestante' if x==2 else \
                                    'Espírita' if x==3 else \
                                    'Matriz Africana' if x==4 else \
                                    'Ateu' if x==5 else \
                                    'Outras'if x==6 else None,
              'renda familia': lambda x : 'até 1' if x==1 else
                                         '1 a 2' if x==2 else
                                         '2 a 5' if x==3 else
                                         '5 a 10' if x==4 else
                                         '10 a 20' if x==5 else
                                         'mais de 20' if x==6 else
                                         'sem rendimento' if x==7 else
                                         'não respondeu' if x==8 else None,
             'interesse': lambda x : 'muito' if x==1 else
                                      'médio' if x==2 else
                                      'pouco' if x==3 else
                                      'nenhum' if x==4 else
                                      'nao sabe' if x==5 else
                                      'nao respondeu' if x==6 else None,
             'rejeicao': lambda x : 'candidato 1' if x==1 else
                                     'candidato 2' if x==2 else
                                     'ninguem' if x==3 else
                                     'não sabe' if x==4 else
                                     'não respondeu' if x==5 else
                                     'todos' if x==6 else None,
             'rejeicao 2': lambda x : 'candidato 1' if x==1 else
                                       'candidato 2' if x==2 else
                                       'ninguem' if x==3 else
                                       'não sabe' if x==4 else
                                       'não respondeu' if x==5 else
                                       'todos' if x==6 else None,
             'rejeicao partido': lambda x : 'PT' if x==10 else
                                             'nao sabe' if x==15 else
                                             'nao quer opinar' if x==16 else
                                             'PTB' if x==2 else
                                             'MDB' if x==6 else 
                                             'PSDB' if x==9 else
                                             'PSD' if x==5 else
                                             'PSOL' if x==8 else
                                             'AVANTE' if x==11 else
                                             'DEM' if x==3 else
                                             'PV' if x==7 else
                                             'Cidadania' if x==12 else
                                             'Republicanos' if x==1 else
                                             'DC',
             'rejeicao partido 2': lambda x : 'PT' if x==10 else
                                             'nao sabe' if x==15 else
                                             'nao quer opinar' if x==16 else
                                             'PTB' if x==2 else
                                             'MDB' if x==6 else 
                                             'PSD' if x==5 else
                                             'PSDB' if x==9 else
                                             'PSOL' if x==8 else
                                             'AVANTE' if x==11 else
                                             'Republicanos' if x==1 else
                                             'Cidadania',
             'avaliacao adm': lambda x : 'ótima' if x==1 else
                                         'boa' if x==2 else
                                         'regular' if x==3 else
                                         'ruim' if x==4 else
                                         'péssima' if x==5 else
                                         'nao respondeu' if x==6 else
                                         'nao sabe' if x==7 else None,
             'aprovacao adm': lambda x : 'aprova' if x==1 else 
                                         'desaprova' if x==2 else
                                         'não sabe' if x==3 else
                                         'não respondeu' if x==4 else None,
             'area maior problema' : lambda x : 'Nenhuma destas' if x==21 else
                                             'saúde' if x==2 else
                                             'não respondeu' if x==23 else
                                             'calçamento' if x==1 else
                                             'geração de empregos' if x==7 else 
                                             'educação' if x==3 else
                                             'abastecimento de água' if x==14 else
                                             'iluminação pública' if x==8 else
                                             'opções de lazer' if x==18 else                                   
                                             'meio ambiente' if x==13 else
                                             'transporte coletivo' if x==9 else
                                             'limpeza pública' if x==5 else
                                             'rede de esgoto' if x==19 else
                                             'assistencia social' if x==6 else
                                             'atividades esportivas' if x==4 else
                                             'corrupção' if x==20 else
                                             'segurança pública' if x==15 else
                                             'habitação' if x==11 else
                                             'administração pública' if x==12 else
                                             'atividades culturais' if x==17 else
                                             'trânsito' if x==16 else
                                             'impostos e taxas' if x==14 else
                                             'não sabe' if x==24 else None
                                  }
    
    return cat

def remove_especial_chars():
    chars = {'chars': lambda x :  'a' if x in list('ÀÁÃÂàáãâ') else \
                                  'e' if x in list('ÉÊéê') else \
                                  'i' if x in list('Íí') else \
                                  'o' if x in list('ÓÕÔóõô') else \
                                  'u' if x in list('Úu') else 
                                  'c' if x in list('Çç') else x}
    return chars