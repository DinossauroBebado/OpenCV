from treinamento import treina
from reconhece import reconhece

# treinar o reconhecimento de face

treina()
reconhece(img, "caracteristicas.npy", "etiquetas.npy",
          "reconhecimento_de_face_treinado_DINO.yml")
