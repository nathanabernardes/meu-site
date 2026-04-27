from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Nathana Bernardes | Desenvolvedora Web</title>

        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: #ffffff;
            }

            header {
                padding: 65px 20px;
                text-align: center;
                background: linear-gradient(135deg, #111827, #1e3a8a);
            }

            .logo {
                width: 85px;
                opacity: 0.4;
                margin-bottom: 15px;
            }

            header h1 {
                font-size: 28px;
                line-height: 1.3;
                margin-bottom: 20px;
                font-weight: 700;
            }

            .botao {
                display: inline-block;
                background: #22c55e;
                color: #ffffff;
                padding: 14px 28px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: bold;
            }

            section {
                padding: 60px 20px;
                max-width: 1100px;
                margin: auto;
            }

            h2 {
                text-align: center;
                font-size: 32px;
                margin-bottom: 10px;
            }

            /* SERVIÇOS */
            .servicos {
                text-align: center;
            }

            .servicos-subtitulo {
                color: #cbd5e1;
                font-size: 16px;
                margin-bottom: 30px;
            }

            .servicos-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
                gap: 20px;
            }

            .servico-card {
                background: linear-gradient(180deg, #1e293b, #111827);
                border: 1px solid rgba(147, 197, 253, 0.15);
                border-radius: 16px;
                padding: 25px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.30);
                transition: all 0.3s ease;
            }

            .servico-card:hover {
                transform: translateY(-5px);
                border: 1px solid rgba(34, 197, 94, 0.4);
            }

            .servico-card h3 {
                color: #93c5fd;
                font-size: 18px;
                margin-bottom: 10px;
            }

            .servico-card p {
                color: #e2e8f0;
                font-size: 14px;
                line-height: 1.6;
            }

            /* PORTFÓLIO */
            .portfolio {
                text-align: center;
            }

            .portfolio-subtitulo {
                color: #cbd5e1;
                font-size: 16px;
                margin-bottom: 35px;
            }

            .carousel {
                width: 100%;
                overflow: hidden;
            }

            .carousel-track {
                display: flex;
                gap: 16px;
                width: max-content;
                animation: scroll 25s linear infinite;
            }

            .carousel-card {
                flex: 0 0 auto;
                width: 180px;
                background: #1e293b;
                border-radius: 14px;
                overflow: hidden;
                box-shadow: 0 8px 20px rgba(0,0,0,0.30);
                transition: transform 0.3s ease;
            }

            .carousel-card:hover {
                transform: translateY(-6px);
            }

            .carousel-card img {
                width: 100%;
                height: 120px;
                object-fit: cover;
            }

            .carousel-card h3 {
                text-align: center;
                padding: 10px;
                color: #93c5fd;
                font-size: 14px;
            }

            @keyframes scroll {
                0% {
                    transform: translateX(0);
                }

                100% {
                    transform: translateX(-50%);
                }
            }

            /* DIFERENCIAIS */
            .diferenciais {
                text-align: center;
            }

            .diferenciais span {
                display: inline-block;
                background: #1e40af;
                padding: 12px 18px;
                margin: 8px;
                border-radius: 20px;
            }

            /* CHAMADA FINAL */
            .final {
                text-align: center;
                line-height: 1.7;
                font-size: 18px;
            }

            footer {
                text-align: center;
                padding: 25px;
                background: #020617;
                color: #94a3b8;
            }

            @media (max-width: 768px) {
                header h1 {
                    font-size: 24px;
                }

                .carousel-card {
                    width: 150px;
                }

                .carousel-card img {
                    height: 100px;
                }
            }
        </style>
    </head>

    <body>

        <header>
            <img src="/static/logo.png" alt="Logo Nathana Bernardes" class="logo">

            <h1>
                Criação de Sites Profissionais <br>
                e Desenvolvimento Web
            </h1>

            <a class="botao" href="https://wa.me/5551981686819" target="_blank">
                Solicitar orçamento pelo WhatsApp
            </a>
        </header>

        <section class="servicos">
            <h2>Serviços</h2>

            <p class="servicos-subtitulo">
                Soluções digitais para fortalecer sua presença online e atrair mais clientes.
            </p>

            <div class="servicos-grid">
                <div class="servico-card">
                    <h3>Sites Profissionais</h3>
                    <p>Criação de sites modernos, responsivos e pensados para transmitir confiança ao seu público.</p>
                </div>

                <div class="servico-card">
                    <h3>Landing Pages</h3>
                    <p>Páginas estratégicas para divulgar serviços, campanhas e aumentar solicitações de orçamento.</p>
                </div>

                <div class="servico-card">
                    <h3>Aplicações Web</h3>
                    <p>Soluções personalizadas para organizar informações, processos e rotinas do negócio.</p>
                </div>

                <div class="servico-card">
                    <h3>Mobile</h3>
                    <p>Interfaces e aplicações adaptadas para uma experiência prática em dispositivos móveis.</p>
                </div>
            </div>
        </section>

        <section class="portfolio">
            <h2>Portfólio</h2>

            <p class="portfolio-subtitulo">
                Catálogo de modelos de sites, lojas, plataformas e aplicativos.
            </p>

            <div class="carousel">
                <div class="carousel-track">

                    <div class="carousel-card">
                        <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=600&q=80" alt="Site profissional">
                        <h3>Sites</h3>
                    </div>

                    <div class="carousel-card">
                        <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=600&q=80" alt="Loja virtual">
                        <h3>Lojas</h3>
                    </div>

                    <div class="carousel-card">
                        <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=80" alt="Plataforma web">
                        <h3>Plataformas</h3>
                    </div>

                    <div class="carousel-card">
                        <img src="https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&w=600&q=80" alt="Aplicativo mobile">
                        <h3>Apps</h3>
                    </div>

                    <div class="carousel-card">
                        <img src="https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=600&q=80" alt="Sistema web">
                        <h3>Sistemas</h3>
                    </div>

                    <div class="carousel-card">
                        <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=600&q=80" alt="Site profissional">
                        <h3>Sites</h3>
                    </div>

                    <div class="carousel-card">
                        <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=600&q=80" alt="Loja virtual">
                        <h3>Lojas</h3>
                    </div>

                    <div class="carousel-card">
                        <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=80" alt="Plataforma web">
                        <h3>Plataformas</h3>
                    </div>

                </div>
            </div>
        </section>

        <section class="diferenciais">
            <h2>Diferenciais</h2>

            <span>Design responsivo</span>
            <span>Atendimento personalizado</span>
            <span>Sites com foco em conversão</span>
            <span>Entrega organizada</span>
            <span>Comunicação clara</span>
        </section>

        <section class="final">
            <h2>Quer tirar sua ideia do papel?</h2>

            <p>
                Vamos conversar sobre o seu projeto e encontrar a melhor solução digital para você.
            </p>

            <a class="botao" href="https://wa.me/5551981686819" target="_blank">
                Quero meu site ou aplicação
            </a>
        </section>

        <footer>
            <p>© 2026 Nathana Bernardes | Desenvolvedora Web e Mobile</p>
        </footer>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)