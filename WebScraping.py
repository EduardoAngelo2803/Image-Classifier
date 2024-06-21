import torch

print("Versão do PyTorch:", torch.__version__)
print("Versão do CUDA disponível no PyTorch:", torch.version.cuda)
print("Quantas GPUs estão disponíveis:", torch.cuda.device_count())
print("Nome da GPU (se disponível):", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "Nenhuma GPU encontrada")




##from bing_image_downloader import downloader

## ownloader.download("Camisas do Nautico", limit=100, output_dir='imagens/testscrapping/nautico', force_replace=False, timeout=2,verbose=True)