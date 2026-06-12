# Verificador do Tempo

Aplicativo desktop em Python com Tkinter que consulta a API OpenWeather e mostra o clima atual de uma cidade.

## Funcionalidades

- Consulta de temperatura atual por cidade
- Descrição do clima em português
- Interface gráfica com Tkinter
- Tratamento de cidade inválida, chave inválida e falhas de conexão
- Arquitetura separada por responsabilidade: configuração, cliente da API, interface e entrypoint
- Chave pública padrão da OpenWeather incluída no projeto

## Tecnologias

- Python 3.12+
- Tkinter
- Requests
- OpenWeather API
- GitHub Actions

## Estrutura do Projeto

```txt
Aplicativo-do-Tempo/
|-- .github/workflows/python-checks.yml
|-- main.py
|-- tempo.py
|-- requirements.txt
|-- weather_app/
|   |-- __init__.py
|   |-- config.py
|   |-- ui.py
|   `-- weather_client.py
`-- README.md
```

## Como Instalar

```bash
git clone https://github.com/preyzinn/Aplicativo-do-Tempo
cd Aplicativo-do-Tempo
pip install -r requirements.txt
```

## Como Executar

```bash
python main.py
```

Também é possível usar o entrypoint legado:

```bash
python tempo.py
```

## Configuração da API

O projeto já possui uma chave pública padrão da OpenWeather em `weather_app/config.py`, então não é necessário configurar variáveis de ambiente para executar.

Se quiser usar outra chave localmente, defina a variável `OPENWEATHER_API_KEY`.

### PowerShell

```powershell
$env:OPENWEATHER_API_KEY="sua-chave-da-openweather"
python main.py
```

### Arquivo `.env`

Crie um arquivo `.env` na raiz do projeto:

```env
OPENWEATHER_API_KEY=sua-chave-da-openweather
```

O `.env` é ignorado pelo git.

## Como Funciona

1. `main.py` carrega a configuração e inicia a interface.
2. `weather_app/config.py` lê `OPENWEATHER_API_KEY`, `.env` ou usa a chave padrão.
3. `weather_app/ui.py` controla a janela Tkinter e eventos do usuário.
4. `weather_app/weather_client.py` consulta a OpenWeather com HTTPS, timeout, `units=metric` e `lang=pt_br`.
5. A resposta é convertida em `WeatherReport` e exibida na tela.

## Exemplo

Entrada:

```txt
São Paulo
```

Saída:

```txt
Cidade: São Paulo
Temperatura: 19°C
Descrição: nublado
```

## Autor

Desenvolvido por **preyzin**.

