from bing_image_downloader import downloader

downloader.download("Camisas do Nautico", limit=100, output_dir='imagens/scrapping/nautico', force_replace=False, timeout=2,verbose=True)

downloader.download("Camisas do Sport", limit=100, output_dir='imagens/scrapping/sport', force_replace=False, timeout=2,verbose=True)