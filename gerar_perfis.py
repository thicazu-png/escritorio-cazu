import os

def gerar_estrutura_escritorio():
    # Nome da pasta principal
    pasta_raiz = "Site_Escritorio"
    pasta_img = os.path.join(pasta_raiz, "img")

    # Cria as pastas se não existirem
    if not os.path.exists(pasta_raiz):
        os.makedirs(pasta_raiz)
    if not os.path.exists(pasta_img):
        os.makedirs(pasta_img)

    # Configurações de Estilo (Inspirado no TozziniFreire)
    estilos = {
        "cor_primaria": "#003366",   # Azul Institucional
        "cor_hover": "#00509d",      # Azul mais claro para interação
        "cor_fundo": "#f4f4f4",      # Cinza muito claro de fundo
        "cor_card": "#ffffff",       # Branco para os cards
        "fonte_titulos": "'Montserrat', sans-serif",
        "fonte_corpo": "'Open Sans', sans-serif"
    }

    # Dados Fictícios
    equipe = [
        {"nome": "Ricardo Menezes", "cargo": "Sócio Diretor", "sigla": "RM"},
        {"nome": "Juliana Cavalcanti", "cargo": "Coordenadora Jurídica", "sigla": "JC"},
        {"nome": "Lucas Silveira", "cargo": "Especialista Tributário", "sigla": "LS"},
        {"nome": "Mariana Fontes", "cargo": "Consultora de Compliance", "sigla": "MF"}
    ]

    # Conteúdo do CSS
    css_content = f"""
body {{
    background-color: {estilos['cor_fundo']};
    font-family: {estilos['fonte_corpo']};
    margin: 0;
    padding: 0;
}}

.header-section {{
    text-align: center;
    padding: 60px 20px;
    background-color: {estilos['cor_primaria']};
    color: white;
}}

.header-section h1 {{
    font-family: {estilos['fonte_titulos']};
    font-weight: 700;
    margin: 0;
    letter-spacing: 1px;
}}

.container {{
    max-width: 1100px;
    margin: -40px auto 60px auto;
    padding: 0 20px;
}}

.grid-equipe {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
}}

.card {{
    background: {estilos['cor_card']};
    border-radius: 4px;
    overflow: hidden;
    box-shadow: 0 10px 20px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
    text-align: center;
}}

.card:hover {{
    transform: translateY(-10px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.15);
}}

.foto-perfil {{
    width: 100%;
    height: 300px;
    background-color: #e0e0e0;
    object-fit: cover;
    display: block;
}}

.info {{
    padding: 25px 15px;
}}

.info h3 {{
    font-family: {estilos['fonte_titulos']};
    color: {estilos['cor_primaria']};
    margin: 0 0 10px 0;
    font-size: 1.2rem;
}}

.info p {{
    color: #666;
    font-size: 0.9rem;
    margin: 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}

.btn-perfil {{
    display: inline-block;
    width: 100%;
    padding: 15px 0;
    background-color: #f8f8f8;
    color: {estilos['cor_primaria']};
    text-decoration: none;
    font-weight: 600;
    font-size: 0.85rem;
    border-top: 1px solid #eee;
    transition: background 0.3s;
}}

.btn-perfil:hover {{
    background-color: {estilos['cor_primaria']};
    color: white;
}}
"""

    # Conteúdo do HTML
    html_cards = ""
    for pessoa in equipe:
        # Usando placeholder que simula uma foto corporativa (cinza com iniciais)
        foto_url = f"https://ui-avatars.com/api/?name={pessoa['nome'].replace(' ', '+')}&size=400&background=003366&color=fff"
        
        html_cards += f"""
        <div class="card">
            <img src="{foto_url}" alt="{pessoa['nome']}" class="foto-perfil">
            <div class="info">
                <h3>{pessoa['nome']}</h3>
                <p>{pessoa['cargo']}</p>
            </div>
            <a href="#" class="btn-perfil">CONHECER PERFIL</a>
        </div>"""

    html_content = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Equipe | Escritório de Advocacia</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <section class="header-section">
        <h1>NOSSAS PESSOAS</h1>
    </section>

    <div class="container">
        <div class="grid-equipe">
            {html_cards}
        </div>
    </div>

</body>
</html>
"""

    # Gravando os arquivos dentro da pasta Site_Escritorio
    with open(os.path.join(pasta_raiz, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    
    with open(os.path.join(pasta_raiz, "style.css"), "w", encoding="utf-8") as f:
        f.write(css_content)

    print(f"Sucesso! Estrutura criada na pasta: {pasta_raiz}")

if __name__ == "__main__":
    gerar_estrutura_escritorio()
    