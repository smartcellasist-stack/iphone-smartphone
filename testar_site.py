import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

url_base = "https://iphonesmartphone.com.br"
url_com_cache_buster = f"{url_base}?t={int(time.time())}"

print(f"=== INICIANDO VARREDURA CORRIGIDA EM: {url_base} ===")

try:
    resposta = requests.get(url_com_cache_buster, headers={"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"}, timeout=10)
    if resposta.status_code == 200:
        print("[OK] Página inicial acessível!")
        soup = BeautifulSoup(resposta.text, 'html.parser')
        links = soup.find_all(['a', 'link'])
        
        urls_encontradas = set()
        for link in links:
            href = link.get('href')
            if href:
                # Remove âncoras locais como #iphones
                if href.startswith('#'):
                    continue
                # Se começar com /, junta com a URL base
                if href.startswith('/'):
                    url_completa = url_base + href
                else:
                    url_completa = urljoin(url_base, href)
                
                if urlparse(url_completa).netloc == urlparse(url_base).netloc:
                    urls_encontradas.add(url_completa)
        
        print(f"\n[INFO] Encontrados {len(urls_encontradas)} links internos para testar botões.")
        
        print("\n=== TESTANDO LINKS E BOTÕES UM POR UM ===")
        for url in sorted(urls_encontradas):
            try:
                checagem = requests.head(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5, allow_redirects=True)
                status = checagem.status_code
                if status == 200:
                    print(f"[FUNCIONANDO (200)] -> {url}")
                elif status == 404:
                    print(f"[ERRO CRÍTICO (404 Not Found)] Botão quebrado! -> {url}")
                else:
                    print(f"[AVISO (Status {status})] Verifique este link -> {url}")
            except Exception as e:
                print(f"[FALHA DE CONEXÃO] Não foi possível testar -> {url}")
    else:
        print(f"[ERRO] A página inicial retornou status: {resposta.status_code}")
except Exception as e:
    print(f"[ERRO CRÍTICO] Falha ao conectar no site: {e}")

print("\n=== VARREDURA CONCLUÍDA ===")
