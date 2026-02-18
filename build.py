import os

def gerar_site_v3_final():
    diretorio_atual = os.getcwd()
    
    estilos = {
        "cor_primaria": "#003366",
        "cor_menu_bg": "#ffffff",
        "fonte_titulos": "'Montserrat', sans-serif",
        "fonte_corpo": "'Open Sans', sans-serif"
    }

    equipe = [
        {"id": "marcio", "nome": "Marcio Antonio Cazu", "cargo": "Sócio Fundador", "img": "marcio.jpg"},
        {"id": "maria", "nome": "Maria Lucia Madalena", "cargo": "Sócia", "img": "maria.jpg"},
        {"id": "rafael", "nome": "Rafael Valério Morillas", "cargo": "Associado", "img": "rafael.jpg"},
        {"id": "thiago", "nome": "Thiago Gialorenço Cazu", "cargo": "Associado", "img": "thiago.jpg"},
        {"id": "anna", "nome": "Anna Julia Madalena", "cargo": "Associada", "img": "anna.jpg"}
    ]

    css_content = f"""
* {{ box-sizing: border-box; }}
body {{ font-family: {estilos['fonte_corpo']}; margin: 0; color: #333; }}

/* Barra de Menu Branca */
nav {{ 
    background: {estilos['cor_menu_bg']}; 
    padding: 10px 5%; 
    display: flex; 
    align-items: center; 
    justify-content: center; 
    position: sticky; 
    top: 0; 
    z-index: 1001; 
    box-shadow: 0 2px 10px rgba(0,0,0,0.1); 
}}

.nav-logo img {{ max-height: 50px; }}

/* Menu Hambúrguer */
.menu-icon {{
    position: absolute;
    left: 5%;
    font-size: 24px;
    cursor: pointer;
    color: {estilos['cor_primaria']};
}}

#menu-toggle {{ display: none; }}

.nav-links {{
    position: fixed;
    top: 0;
    left: -100%;
    width: 250px;
    height: 100vh;
    background: white;
    display: flex;
    flex-direction: column;
    padding: 60px 20px;
    transition: 0.4s;
    list-style: none;
    z-index: 1000;
}}

#menu-toggle:checked ~ .nav-links {{ left: 0; }}

.nav-links li {{ margin: 20px 0; }}
.nav-links a {{ 
    text-decoration: none; 
    color: {estilos['cor_primaria']}; 
    font-weight: 600; 
    font-size: 1rem; 
    text-transform: uppercase; 
}}

/* Imagem de Fundo (Sem logo sobreposta) */
.brand-area {{ 
    position: relative; 
    height: 450px; 
    overflow: hidden; 
}}
.bg-image {{ 
    width: 100%; 
    height: 100%; 
    background-image: url('img/frete_escritorio.png'); 
    background-size: cover; 
    background-position: center; 
    filter: blur(4px); 
    transform: scale(1.05); 
}}

/* Slider de Notícias RSS */
.news-slider {{ 
    background: #f4f4f4; 
    padding: 40px 0; 
    text-align: center; 
}}

/* Grid Profissionais (2x3) */
.container {{ max-width: 1200px; margin: 0 auto; padding: 40px 20px; }}
.grid-equipe {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 25px; }}
.card {{ background: #fff; border: 1px solid #eee; display: flex; align-items: center; padding: 20px; text-decoration: none; color: inherit; border-radius: 4px; }}
.card-marcio, .card-maria {{ grid-column: span 3; }}
.card-rafael, .card-thiago, .card-anna {{ grid-column: span 2; }}

.foto-box {{ width: 130px; height: 130px; position: relative; margin-right: 25px; flex-shrink: 0; overflow: hidden; border-radius: 4px; }}
.iniciais {{ width: 100%; height: 100%; background: {estilos['cor_primaria']}; color: white; display: flex; align-items: center; justify-content: center; font-size: 2.2rem; font-weight: bold; position: absolute; z-index: 2; transition: 0.3s; }}
.foto-real {{ width: 100%; height: 100%; object-fit: cover; position: absolute; z-index: 1; }}
.card:hover .iniciais {{ opacity: 0; }}

/* Rodapé */
footer {{ background: {estilos['cor_primaria']}; color: white; padding: 40px 10%; }}
.footer-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }}

@media (max-width: 900px) {{ 
    .grid-equipe {{ grid-template-columns: 1fr; }}
    .card-marcio, .card-maria, .card-rafael, .card-thiago, .card-anna {{ grid-column: span 1; }}
    .footer-grid {{ grid-template-columns: 1fr; }}
}}
"""

    html_cards = ""
    for p in equipe:
        ini = (p['nome'].split()[0][0]+p['nome'].split()[-1][0]).upper()
        html_cards += f"""
        <a href="{p['id']}.html" class="card card-{p['id']}">
            <div class="foto-box">
                <img src="img/{p['img']}" class="foto-real">
                <div class="iniciais">{ini}</div>
            </div>
            <div class="info"><h3>{p['nome']}</h3><p>{p['cargo']}</p></div>
        </a>"""

    html_content = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>M.A. Cazu Advogados</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
</head>
<body>
    <nav>
        <label for="menu-toggle" class="menu-icon">☰</label>
        <input type="checkbox" id="menu-toggle">
        <ul class="nav-links">
            <li><a href="index.html">Início</a></li>
            <li><a href="#">Sobre nós</a></li>
            <li><a href="#">Áreas de Atuação</a></li>
            <li><a href="#profissionais">Profissionais</a></li>
        </ul>
        <div class="nav-logo">
            <img src="img/logo_mac2.png" alt="Logo MAC">
        </div>
    </nav>

    <div class="brand-area">
        <div class="bg-image"></div>
    </div>

    <section class="news-slider">
        <div class="container">
            <h2 style="color:{estilos['cor_primaria']}; margin-bottom:20px;">Atualidades Jurídicas</h2>
            <script type="text/javascript" src="https://feed.mikle.com/js/fw-loader.js" preloader-text="A carregar notícias..." data-fw-widget-id="158732"></script>
        </div>
    </section>

    <div class="container" id="profissionais">
        <h1 style="text-align:center; color:{estilos['cor_primaria']}; margin-bottom:40px;">Nossos Profissionais</h1>
        <div class="grid-equipe">{html_cards}</div>
    </div>

    <footer>
        <div class="footer-grid">
            <div>
                <h3>CONTATO</h3>
                <p>📧 atendimento@marciocazuadvogados.com</p>
                <p>📞 (16) 3371-1299</p>
            </div>
            <div>
                <p>📍 Rua Rui Barbosa, nº 347 - Vila Monteiro | São Carlos/SP</p>
            </div>
        </div>
    </footer>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f: f.write(html_content)
    with open("style.css", "w", encoding="utf-8") as f: f.write(css_content)
    print("Site atualizado: Menu hambúrguer e Slider RSS incluídos!")

if __name__ == "__main__":
    gerar_site_v3_final()