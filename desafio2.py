"""
Desafio
A Inteligência Artificial no Microsoft Azure oferece uma ampla gama de recursos que permitem às organizações automatizar tarefas, analisar grandes volumes de dados, personalizar experiências e garantir segurança com conformidade regulatória.
Esses benefícios ajudam empresas a aumentar a eficiência, tomar decisões orientadas por dados, melhorar a experiência do usuário e proteger informações sensíveis, tudo isso com a escalabilidade da nuvem da Microsoft.

Neste desafio, você irá relacionar os benefícios da IA no Azure com suas respectivas descrições.

Entrada
A entrada consistirá no benefício da IA no Azure para o qual você deve retornar a descrição. Os seguintes benefícios são considerados válidos para este desafio:

"automação inteligente"
"análise de dados em larga escala"
"customização de experiências"
"segurança e conformidade"
Saída
A saída esperada é a descrição associada ao benefício fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa associar corretamente:

"garante proteção de dados e conformidade com regulamentações"
"permite automatizar processos repetitivos com inteligência"
"oferece insights detalhados de grandes volumes de dados"
"adapta serviços e aplicações para experiências personalizadas"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
automação inteligente	permite automatizar processos repetitivos com inteligência
análise de dados em larga escala	oferece insights detalhados de grandes volumes de dados
customização de experiências	adapta serviços e aplicações para experiências personalizadas
Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.
"""
# TODO: Preencha o dicionário que associa benefícios da IA no Azure às suas descrições
beneficios_azure = {
    "automação inteligente": "permite automatizar processos repetitivos com inteligência",
    "análise de dados em larga escala": "oferece insights detalhados de grandes volumes de dados",
    "customização de experiências": "adapta serviços e aplicações para experiências personalizadas",
    "segurança e conformidade": "garante proteção de dados e conformidade com regulamentações"
}

# Recebe a entrada do usuário
entrada = input().lower()  # converte para minúscula

# Retorna a descrição correspondente ao benefício informado
if entrada in beneficios_azure:
  print(beneficios_azure[entrada])
else:
  print("Entrada Inválida")