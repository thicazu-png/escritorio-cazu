import os

def gerar_site_definitivo():
    diretorio_atual = os.getcwd()
    
    estilos = {
        "cor_primaria": "#003366",
        "fonte_titulos": "'Montserrat', sans-serif",
        "fonte_corpo": "'Open Sans', sans-serif"
    }

    # Dados detalhados
    equipe = [
        {"id": "marcio", "nome": "Marcio Antonio Cazu", "cargo": "Sócio Fundador", "img": "marcio.jpg", "email": "marciocazu@marciocazuadvogados.com", "historico": "Especialista em Direito Civil..."},
        {"id": "maria", "nome": "Maria Lucia Madalena", "cargo": "Sócia", "img": "maria.jpg", "email": "marialucia@marciocazuadvogados.com", "historico": "Especialista em Direito Tributário..."},
        {"id": "rafael", "nome": "Rafael Valério Morillas", "cargo": "Associado", "img": "rafael.jpg", "email": "rafael@marciocazuadvogados.com", "historico": "Especialista em Direito do Trabalho..."},
        {"id": "thiago", "nome": "Thiago Gialorenço Cazu", "cargo": "Associado", "img": "thiago.jpg", "email": "thiago@marciocazuadvogados.com", "historico": "Especialista em Direito Digital..."},
        {"id": "anna", "nome": "Anna Julia Madalena", "cargo": "Associada", "img": "anna.jpg", "email": "annajulia@marciocazuadvogados.com", "historico": "Especialista em Família..."}
    ]

    atuacao = [
        {"titulo": "Direito Cível", "desc": "Consultoria em contratos e responsabilidade civil."},
        {"titulo": "Direito Trabalhista", "desc": "Defesa de interesses corporativos e prevenção."},
        {"titulo": "Direito Tributário", "desc": "Planejamento fiscal e recuperação de créditos."},
        {"titulo": "Direito Digital", "desc": "Adequação à LGPD e conformidade tecnológica."},
        {"titulo": "Família e Sucessões", "desc": "Inventários, divórcios e mediação familiar."}
    ]

    # --- CSS COM GRID MATEMÁTICO ---
    css_content = f"""
* {{ box-sizing: border-box; }}
body {{ font-family: {estilos['fonte_corpo']}; margin: 0; color: #333; line-height: 1.6; }}

/* Menu Justificado */
nav {{ background: {estilos['cor_primaria']}; padding: 15px 10%; position: sticky; top: 0; z-index: 1000; }}
.nav-links {{ display: flex; justify-content: space-between; list-style: none; margin: 0; padding: 0; width: 100%; }}
.nav-links a {{ text-decoration: none; color: white; font-weight: 600; font-size: 0.85rem; text-transform: uppercase; }}

/* Hero Area (Logo + Fundo Escritório) */
.brand-area {{ position: relative; text-align: center; padding: 80px 0; overflow: hidden; display: flex; align-items: center; justify-content: center; min-height: 400px; }}
.bg-image {{ position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-image: url('img/frete_escritorio.png'); background-size: cover; background-position: center; filter: blur(6px); transform: scale(1.05); z-index: 1; }}
.brand-area::after {{ content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(255, 255, 255, 0.2); z-index: 2; }}
.brand-area img {{ position: relative; max-width: 450px; width: 85%; z-index: 3; }}

.container {{ max-width: 1200px; margin: 0 auto; padding: 40px 20px; }}
.section-title {{ text-align: center; color: {estilos['cor_primaria']}; font-family: {estilos['fonte_titulos']}; margin-bottom: 50px; font-size: 2rem; position: relative; }}

/* GRID CONFIGURADO PARA 2 EM CIMA E 3 EMBAIXO */
.grid-equipe {{ 
    display: grid;
    grid-template-columns: repeat(6, 1fr); 
    gap: 25px;
}}

/* Card Estilo Base */
.card {{ 
    background: #fff; border: 1px solid #eee; display: flex; align-items: center; 
    padding: 20px; text-decoration: none; color: inherit; transition: 0.3s; border-radius: 4px;
}}
.card:hover {{ border-color: #c5a059; box-shadow: 0 10px 20px rgba(0,0,0,0.05); }}

/* Marcio e Maria (Ocupam 3 colunas cada = 2 cards na linha) */
.card-marcio, .card-maria {{ grid-column: span 3; }}

/* Rafael, Thiago e Anna (Ocupam 2 colunas cada = 3 cards na linha) */
.card-rafael, .card-thiago, .card-anna {{ grid-column: span 2; }}

.foto-box {{ width: 130px; height: 130px; position: relative; margin-right: 25px; flex-shrink: 0; overflow: hidden; border-radius: 4px; }}
.iniciais {{ width: 100%; height: 100%; background: {estilos['cor_primaria']}; color: white; display: flex; align-items: center; justify-content: center; font-size: 2.2rem; font-weight: bold; position: absolute; z-index: 2; transition: 0.3s; }}
.foto-real {{ width: 100%; height: 100%; object-fit: cover; position: absolute; z-index: 1; }}
.card:hover .iniciais {{ opacity: 0; }}

/* Áreas de Atuação */
.atuacao-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; }}
.atuacao-item {{ padding: 25px; border: 1px solid #eee; text-align: center; transition: 0.3s; background: #fff; }}
.atuacao-item:hover {{ background: {estilos['cor_primaria']}; color: white; }}

/* Rodapé */
footer {{ background: {estilos['cor_primaria']}; color: white; padding: 60px 10% 20px; }}
.footer-grid {{ display: grid; grid-template-columns: 1.5fr 1fr; gap: 50px; }}
.footer-info-group a {{ color: white; text-decoration: none; font-weight: 600; }}
.map-container {{ width: 100%; height: 250px; border: none; border-radius: 4px; }}

/* Perfil Individual */
.perfil-container {{ max-width: 1000px; margin: 60px auto; display: grid; grid-template-columns: 350px 1fr; gap: 50px; padding: 0 20px; }}
.perfil-foto img {{ width: 100%; border-radius: 4px; }}

@media (max-width: 900px) {{ 
    .grid-equipe {{ grid-template-columns: 1fr; }}
    .card-marcio, .card-maria, .card-rafael, .card-thiago, .card-anna {{ grid-column: span 1; }}
    .footer-grid, .perfil-container {{ grid-template-columns: 1fr; }}
}}
"""

    def layout_base(conteudo, titulo_pagina, eh_home=False):
        map_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3699.23126756627!2d-47.89679192383838!3d-22.021028704403866!2m3!1f0!2f0!3f0!3m2!1i1024!2i1024!3f106.1!3m2!1i1024!2i1024!4f13.1!3m3!1m2!1s0x94b87739564c7d01%3A0x77c22502660d00f7!2sRua%20Rui%20Barbosa%2C%20347%20-%20Vila%20Monteiro%2C%20S%C3%A3o%20Carlos%20-%20SP!5e0!3m2!1spt-BR!2sbr!4v1700000000000"
        
        logo_path = "img/logo_mac2.png" # Caminho para a sua logo transparente
        
        header_brand = f"""<div class="brand-area"><div class="bg-image"></div><a href="index.html"><img src="{logo_path}" alt="Logo MAC"></a></div>""" if eh_home else f"""<div class="brand-area" style="min-height: auto; padding: 30px 0; background: #fff; border-bottom: 1px solid #eee;"><a href="index.html"><img src="{logo_path}" alt="Logo MAC" style="max-width: 280px;"></a></div>"""

        return f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo_pagina} | M.A. Cazu Advogados</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav><ul class="nav-links"><li><a href="index.html">Início</a></li><li><a href="#">Sobre nós</a></li><li><a href="#atuacao">Áreas de Atuação</a></li><li><a href="#profissionais">Profissionais</a></li></ul></nav>
    {header_brand}
    {conteudo}
    <footer>
        <div class="footer-grid">
            <div class="footer-info-group">
                <h3>CONTATO</h3>
                <p>📧 <a href="mailto:atendimento@marciocazuadvogados.com">atendimento@marciocazuadvogados.com</a></p>
                <p>📞 <a href="tel:1633711299">(16) 3371-1299</a></p>
                <a href="https://wa.me/551633711299" target="_blank" style="align-self:flex-start; background:#25d366; color:white; padding:10px 20px; border-radius:5px; text-decoration:none; font-weight:bold;">WHATSAPP BUSINESS</a>
                <p>📍 Rua Rui Barbosa, nº 347 - Vila Monteiro | São Carlos/SP</p>
            </div>
            <iframe class="map-container" src="{map_url}" allowfullscreen="" loading="lazy"></iframe>
        </div>
        <div class="copyright">© 2026 Marcio Antonio Cazu Advogados | Todos os direitos reservados.</div>
    </footer>
</body>
</html>"""

    # Gerar Home
    html_cards = ""
    for p in equipe:
        iniciais = (p['nome'].split()[0][0]+p['nome'].split()[-1][0]).upper()
        html_cards += f"""
        <a href="{p['id']}.html" target="_blank" class="card card-{p['id']}">
            <div class="foto-box">
                <img src="img/{p['img']}" class="foto-real">
                <div class="iniciais">{iniciais}</div>
            </div>
            <div class="info">
                <h3>{p['nome']}</h3><p>{p['cargo']}</p>
                <div style="color:{estilos['cor_primaria']}; font-weight:bold; font-size:0.7rem; margin-top:10px;">VER PERFIL COMPLETO</div>
            </div>
        </a>"""

    html_atuacao = "".join([f"""<div class="atuacao-item"><h3>{a['titulo']}</h3><p>{a['desc']}</p></div>""" for a in atuacao])

    conteudo_home = f"""
    <div class="container" id="profissionais"><h1 class="section-title">Nossos Profissionais</h1><div class="grid-equipe">{html_cards}</div></div>
    <div class="container" id="atuacao" style="background:#f9f9f9; max-width:100%;"><div style="max-width:1200px; margin:0 auto; padding:40px 20px;"><h1 class="section-title">Áreas de Atuação</h1><div class="atuacao-grid">{html_atuacao}</div></div></div>"""

    # Geração Final
    with open("index.html", "w", encoding="utf-8") as f: f.write(layout_base(conteudo_home, "Início", True))
    with open("style.css", "w", encoding="utf-8") as f: f.write(css_content)
    for p in equipe:
        with open(f"{p['id']}.html", "w", encoding="utf-8") as f: f.write(layout_base(f"<div class='perfil-container'><div class='perfil-foto'><img src='img/{p['img']}'></div><div class='perfil-info'><h1>{p['nome']}</h1><p><strong>{p['cargo']}</strong></p><h2>Histórico Profissional</h2><p>{p['historico']}</p><h2>Formação Acadêmica</h2><ul><li>Informação em breve...</li></ul></div></div>", p['nome']))

    print("Site atualizado! Execute o commit no GitHub e aguarde 1 minuto.")

if __name__ == "__main__":
    gerar_site_definitivo()