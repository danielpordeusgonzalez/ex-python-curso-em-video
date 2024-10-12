n = input('digite algo: ')
print('o tipo primitivo desse valor é {}, só tem espaços {}, é um alfanumerico? {}, é alfabetico? {}, é numerico? {}, está em maiusculo? {}'.format(type(n),n.isspace() ,n.isalnum(), n.isalpha(), n.isnumeric(), n.isupper()))

