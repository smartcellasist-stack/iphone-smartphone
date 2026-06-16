from bs4 import BeautifulSoup
import os

print("=== INICIANDO VARREDURA LOCAL DIRETO NO ARQUIVO ===")

if not os.path.exists('index.html'):
    print("[ERRO] Arquivo index.html não foi encontrado nesta pasta!")
else:
    with open('index.html', 'r', encoding='utf-8') as f:
        html_local = f.read()
    
    soup = BeautifulSoup(html_local, 'html.parser')
    links = soup.find_all(['a', 'link'])
    
    urls_encontradas = set()
    for link in links:
        href = link.get('href')
        if href:
            if href.startswith('#') or href == '/':
                continue
            urls_encontradas.add(href)
            
    print(f"\n[INFO] Encontrados {len(urls_encontradas)} links/botões no arquivo local.")
    
    print("\n=== LISTA DE LINKS IDENTIFICADOS NO SEU HTML ===")
    for url in sorted(urls_encontradas):
        print(f"-> {url}")

print("\n=== VARREDURA LOCAL CONCLUÍDA ===")
