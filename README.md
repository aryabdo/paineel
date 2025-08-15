# PAINEEL

Ferramenta de clipping de diários oficiais e execução de tarefas agendadas.

## Instalação

1. Clone este repositório e acesse a pasta principal do projeto:

   ```bash
   git clone https://github.com/aryabdo/paineel.git
   cd paineel/paineel
   ```

2. Inicie os contêineres:

   ```bash
   make run
   ```

3. A interface web estará disponível em `http://localhost:5050` com credenciais padrão `airflow` / `airflow`.

## Configuração de DAGs

Os arquivos YAML em `pa_dag_confs` descrevem o agendamento e os comandos de cada fluxo de trabalho. Exemplo:

```yaml
dag:
  id: exemplo
  schedule: "0 0 * * *"
  owner: ["Ary Abdo"]
  commands:
    - task_id: diga_ola
      type: bash
      script: echo
      args: ["olá"]
```

Salve seus arquivos de configuração no diretório apontado pela variável de ambiente `PA_DAG_CONF_DIR`. Cada arquivo cria uma DAG visível na interface para ativação e consulta de logs.

## Licença

Consulte o arquivo `LICENSE` para obter informações sobre a licença do software.

---

Mantenedor: Ary Abdo
