# [![Build Cadê Minhas Oportunidades ?](https://github.com/phillrog/cade-minhas-oportunidades/actions/workflows/build-com-conda.yml/badge.svg?branch=main)](https://github.com/phillrog/cade-minhas-oportunidades/actions/workflows/build-com-conda.yml) - [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cade-minhas-oportunidades.streamlit.app)

O **Cadê Minhas Oportunidades?** é uma ferramenta de geração de **Google Dorking** para buscar no Google oportunidades do LinkedIn de forma muito mais precisa que a busca nativa da plataforma.

![cmo](https://github.com/user-attachments/assets/c9bbb8a6-acfa-45ca-b9d9-e180c082b66e)

🎯 Finalidade
-------------

Muitas vagas publicadas no LinkedIn não aparecem na aba "Vagas" ou se perdem em feeds poluídos. Esta ferramenta permite:

-   Filtrar termos específicos diretamente no título do post ou vaga.

-   Eliminar empresas de recrutamento em massa ou termos indesejados.

-   Buscar em períodos específicos com precisão cirúrgica.

* * * * *

🏗️ Estrutura do Projeto
------------------------


Plaintext

```
├── assets/
│   └── style.css          # Estilização (Marquee animado e Brutalist Design)
├── src/
│   ├── core/
│   │   └── dork.py        # Lógica de negócio: Geração da Query Dork
│   ├── ui/
│   │   └── components.py  # Abstração de componentes visuais e injeção de CSS
│   └── utils/
│       └── system.py      # Ferramentas de suporte e manipulação de estado
└── app.py                 # Ponto de entrada da aplicação Streamlit

```

* * * * *

🔬 Anatomia da Dork Gerada
--------------------------

A aplicação gera uma "Dork" (query de busca avançada). Veja o que cada termo significa na nossa lógica:

`site:br.linkedin.com (inurl:jobs/view OR inurl:posts) intitle:("ANGULAR" OR "C#") ".NET" "BRASIL" ( "REMOTO") -bairesdev`

| **Operador** | **Significado** | **Finalidade no Projeto** |
| --- | --- | --- |
| **`site:br.linkedin.com`** | Restrição de Domínio | Garante que os resultados venham apenas do LinkedIn Brasil. |
| **`inurl:jobs/view OR inurl:posts`** | Filtro de URL | Busca tanto em páginas de vagas oficiais quanto em posts de recrutadores. |
| **`intitle:(...)`** | Busca no Título | Filtra palavras-chave que **precisam** estar no título da vaga. |
| **`"Termo"`** | Correspondência Exata | Garante que o Google não ignore ou substitua a tecnologia (ex: .NET). |
| **`-termo`** | Exclusão | Remove resultados indesejados (ex: empresas que você não quer ver). |
| **`tbs=cdr:1...`** | Parâmetro de URL | (Injetado via Python) Filtra resultados por um intervalo exato de datas. |

* * * * *


## 🚀 Como rodar o projeto

Siga os passos abaixo para configurar o ambiente e executar a aplicação localmente:

### 1. Criar o Ambiente Virtual
Isso garante que as bibliotecas do projeto não conflitem com outras no seu computador.
```bash
python -m venv .venv
```

### 2. Ativar o Ambiente Virtual

No Windows:

```bash
.\.venv\Scripts\activate
```

No Linux/Mac:

```bash
source .venv/bin/activate
```

### 3. Instalar as Dependências
Instale todas as bibliotecas necessárias listadas no arquivo requirements.txt.

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação
Inicie o servidor do Streamlit para abrir a interface no seu navegador.

```bash
python -m streamlit run app.py
```

* * * * *

🛠️ Tecnologias Utilizadas
--------------------------

-   **Python 3.12**

-   **Streamlit** (Interface Web)

-   **Streamlit-Tags** (Gerenciamento de Keywords)

-   **CSS Customizado** (Interface Brutalista com animações dinâmicas)

# Resultado

Exempo dork gerado
```
site:br.linkedin.com (inurl:jobs/view OR inurl:posts) intitle:("C#" OR "ANGULAR") ".NET" "BRASIL" ("REMOTO" OR "HOME OFFICE")
```

Exemplo de URL
```
https://www.google.com/search?q=site%3Abr.linkedin.com%20%28inurl%3Ajobs/view%20OR%20inurl%3Aposts%29%20intitle%3A%28%22C%23%22%20OR%20%22ANGULAR%22%29%20%22.NET%22%20%22BRASIL%22%20%28%22REMOTO%22%20OR%20%22HOME%20OFFICE%22%29&tbs=cdr:1,cd_min:01/17/2026,cd_max:01/20/2026&sort=date:r
```

