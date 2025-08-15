## FAQ e problemas frequentes

Nesta seção, você encontrará perguntas e respostas comuns e solução de problemas mais frequentes na utilização do PAINEEL.

1. **Do que é preciso para instalar o PAINEEL?** <br>
As instruções detalhadas de instalação estão [neste link](https://gestaogovbr.github.io/PAINEEL/como_utilizar/instalacao/).

1. **Como configurar os parâmetros de pesquisa do PAINEEL?** <br>
Os parâmetros devem ser editados no arquivo em formato yml. 

1. **Qual a configuração mínima para a instalação do PAINEEL?** <br>
É recomendado 4 Gb de memória RAM e 2 Gb de espaço em disco pelo menos.

1. **Posso rodar o PAINEEL no meu computador pessoal?** <br>
Sim. O PAINEEL pode ser instalado em qualquer sistema operacional com suporte ao Docker.

1. **Quais são as fontes de dados do PAINEEL?** <br>
 Os dados são obtidos via INLABS, API da Imprensa Nacional e API do Querido Diário.

1. **De que forma o PAINEEL é capaz de enviar relatórios?** <br>
Via e-mail, Slack, Discord.

1. **Preciso pagar pra usar o PAINEEL?** <br>
Não, ele é gratuito.

1. **Posso usar o PAINEEL para fazer buscas nas edições mais antigas do DOU?** <br>
Sim, basta indicar a data desejada no campo "trigger_date" ao disparar manualmente a DAG.

1. **Como receber atualizações de versão do PAINEEL?** <br>
Sim, basta acompanhar o change log (log de atualizações) disponível [aqui](https://gestaogovbr.github.io/PAINEEL/changelog/changelog/).

1. **Posso utilizar o PAINEEL em meu órgão?** <br>
Sim. Confira as instruções [aqui](https://gestaogovbr.github.io/PAINEEL/como_utilizar/usuarios/).

1. **Posso utilizar o PAINEEL na minha empresa privada?** <br>
Sim. Não são cobrados direitos autorais ou de exclusividade.

1. **Existe um limite de acessos diário para buscas com o PAINEEL?** <br>
Não. Os acessos são ilimitados.

1. **É necessário fazer alguma configuração de fuso horário para o PAINEEL?** <br>
Sim. O padrão é América-São Paulo para o ambiente Airflow que dá sustentação ao PAINEEL através da variável de ambiente chamada AIRFLOW__CORE__DEFAULT__TIMEZONE.

1. **Posso usar o PAINEEL no exterior?** <br>
Sim. O PAINEEL pode ser executado em qualquer lugar desde que tenha acesso à internet.
