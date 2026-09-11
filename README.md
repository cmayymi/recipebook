recipebook/
├── .github/              # Arquivos de fluxo de trabalho e automações
├── apps/
│   ├── backend/          # Lógica do Flask, rotas e banco de dados
│   │   ├── app.py        # Arquivo principal do servidor Flask
│   │   ├── database.py   # Conexão e comandos do SQLite
│   │   ├── ai_parser.py  # Lógica de integração com o LLM
│   │   └── templates/    # Páginas HTML renderizadas pelo Flask
│   │       ├── index.html
│   │       └── receitas.html
│   ├── frontend/         # Arquivos estáticos e de interface
│   │   ├── static/       # Folhas de estilo (CSS) e scripts (JS)
│   │   └── views/        # Componentes visuais adicionais
│   └── libs/             # Módulos utilitários e scripts de apoio
├── design_files/         # Diagramas do banco de dados e protótipos de tela
├── venv/                 # Ambiente virtual Python isolado
├── requirements.txt      # Dependências do projeto (Flask, SDK da IA, etc.)
└── README.md             # Documentação principal do projeto