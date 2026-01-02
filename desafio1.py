
"""
Desafio
A IA Responsável é guiada por princípios que garantem o uso ético, inclusivo e confiável da tecnologia. Neste desafio, você deve associar cada princípio de IA responsável com a sua descrição correspondente. O objetivo é reforçar o entendimento sobre como esses pilares são aplicados em soluções práticas.

Entrada
A entrada será o nome de um princípio de IA responsável, para o qual você deverá retornar a descrição associada. Os seguintes princípios são considerados válidos neste desafio:

"imparcialidade"
"confiabilidade e segurança"
"privacidade e segurança"
"transparência"
Saída
A saída esperada é a descrição correspondente ao princípio fornecido como entrada.Seguem as descrições possíveis, listadas aleatoriamente, para que você faça a associação correta:

"explicar de forma clara como a IA funciona e toma decisões"
"garantir que sistemas sejam robustos, seguros e funcionem de forma confiável"
"proteger informações pessoais e respeitar a privacidade dos usuários"
"assegurar que sistemas não tenham vieses e tratem todas as pessoas de forma justa"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
imparcialidade	assegurar que sistemas não tenham vieses e tratem todas as pessoas de forma justa
confiabilidade e segurança	garantir que sistemas sejam robustos, seguros e funcionem de forma confiável
privacidade e segurança	proteger informações pessoais e respeitar a privacidade dos usuários
Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.
"""

# TODO: Preencha o dicionário com a descrição dos princípios
principios = {
    "imparcialidade": "assegurar que sistemas não tenham vieses e tratem todas as pessoas de forma justa",
    "confiabilidade e segurança": "garantir que sistemas sejam robustos, seguros e funcionem de forma confiável",
    "privacidade e segurança": "proteger informações pessoais e respeitar a privacidade dos usuários",
    "transparência": "Explicar de forma clara como a IA funciona e toma decisões"
}

# Lê a entrada do usuário (um princípio de IA responsável)
entrada = input().strip()
# Exibe a descrição correspondente
if entrada in principios:
  print(principios[entrada])
else:
  print ("principios invalidos")

