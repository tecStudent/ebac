from sys import argv

from extracao import Extracao
from visualizacao import Vizualizacao


try:
  Extracao()
except Exception as exc:
  print("Erro, na extração")
else:
  print("Extração concluida!")
  try:
    Vizualizacao(argv[1])
  except Exception as exc:
    print("Erro, na geração de imagem")
  else:
    print("Grafico gerado!" )