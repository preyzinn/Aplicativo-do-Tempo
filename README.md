# **Verificador Do TEMPO**

Aplicativo simples desenvolvido em Python utilizando **Tkinter** e a API da OpenWeather para consultar informações climáticas de uma cidade.

---

# Funcionalidades

- Consulta de temperatura em tempo real
- Exibição da descrição do clima
- Interface gráfica utilizando Tkinter
- Tratamento de erro para cidades inválidas

---

# Tecnologias Utilizadas

- Python 3
- Tkinter
- Requests
- OpenWeather API

---

# Instalação

Clone o repositório:

```bash
git clone https://github.com/preyzinn/verificador-clima.git
```

Acesse a pasta do projeto:

```bash
cd verificador-clima
```

Instale a dependência necessária:

```bash
pip install requests
```

---

# Como Executar

Execute o arquivo principal:

```bash
python main.py
```

---

# Funcionamento

O programa:

1. Recebe o nome de uma cidade digitada pelo usuário
2. Faz uma requisição para a API OpenWeather
3. Obtém a temperatura e descrição do clima
4. Converte a temperatura de Kelvin para Celsius
5. Exibe as informações na interface gráfica

---

# Exemplo

## Entrada

```txt
São Paulo
```

## Saída

```txt
Temperatura: 22°C
Descrição: céu limpo
```

---

# Estrutura do Projeto

```txt
📦 verificador-clima
 ┣ 📜 main.py
 ┗ 📜 README.md
```

---

# Autor

Desenvolvido por **preyzin**.
