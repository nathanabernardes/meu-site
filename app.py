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
        <title>Nathana Bernardes | Desenvolvedora</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: #ffffff;
            }

            header {
                padding: 80px 20px;
                text-align: center;
                background: linear-gradient(135deg, #111827, #1e3a8a);
            }

            header h1 {
                font-size: 42px;
                margin-bottom: 20px;
            }

            header p {
                font-size: 20px;
                max-width: 800px;
                margin: 0 auto 30px;
                color: #dbeafe;
            }

            .botao {
                display: inline-block;
                background: #22c55e;
                color: #ffffff;
                padding: 15px 30px;
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
                margin-bottom: 40px;
            }

            .cards {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
                gap: 20px;
            }

            .card {
                background: #1e293b;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            }

            .card h3 {
                color: #93c5fd;
            }

            .sobre, .final {
                text-align: center;
                line-height: 1.7;
                font-size: 18px;
            }

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

            footer {
                text-align: center;
                padding: 25px;
                background: #020617;
                color: #94a3b8;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>Criação de Sites, Aplicações Web e Mobile</h1>
            <p>
                Transformo ideias em soluções digitais modernas, funcionais e responsivas.
                Ajudo profissionais, pequenos negócios e empresas a terem presença digital com
                sites, landing pages, sistemas e aplicações web/mobile.
            </p>
            <a class="botao" href="https://wa.me/5551981686819" target="_blank">
                Solicitar orçamento pelo WhatsApp
            </a>
        </header>

        <section>
            <h2>Serviços</h2>
            <div class="cards">
                <div class="card">
                    <h3>Criação de Sites Profissionais</h3>
                    <p>Sites modernos, rápidos e adaptados para celular, computador e tablet.</p>
                </div>

                <div class="card">
                    <h3>Landing Pages</h3>
                    <p>Páginas estratégicas para divulgação de serviços, captação de clientes e campanhas.</p>
                </div>

                <div class="card">
                    <h3>Aplicações Web</h3>
                    <p>Soluções sob medida para organizar processos, cadastros, informações e rotinas do negócio.</p>
                </div>

                <div class="card">
                    <h3>Desenvolvimento Mobile</h3>
                    <p>Aplicativos funcionais para Android/iOS, conforme a necessidade do projeto.</p>
                </div>
            </div>
        </section>

        <section class="sobre">
            <h2>Sobre mim</h2>
            <p>
                Sou Nathana Bernardes, desenvolvedora apaixonada por tecnologia e criação de soluções digitais.
                Trabalho com desenvolvimento de projetos que ajudam pessoas e empresas a se posicionarem melhor
                na internet.
            </p>
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
            <p>Vamos conversar sobre o seu projeto e encontrar a melhor solução digital para você.</p>
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