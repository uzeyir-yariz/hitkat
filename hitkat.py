import topla
import cikartma
import carpma

first_log = """
  1) +
  2) -
  3) *
  4) /

  out = çıkış
"""

key_while_base = 0


def coculler(key_select):
  if key_select == "+":
    topla.toplama()
  elif key_select == "-":
    cikartma.cikartma()
  elif key_select == "*":
    carpma.carpma()
  elif key_select == "/":
    print("Bölme işlemi")

# Anahtar seçici
def key_selected():
  print(first_log)
  global key_while_base  # global değişken olarak eklenmeli
  key_select = input("Lütfen bir işlem seçin: ")

  if key_select in ["+", "-", "*", "/"]:
    print("Geçerli bir işlem seçtiniz.")
    coculler(key_select)  # coculler fonksiyonunu key_select ile çağırın
  elif key_select == "out":
    key_while_base = 1
    print("Anahtar seçme programından çıkılıyor.")
  else:
    print("Lütfen geçerli bir işlem seçin: +, -, *, / veya 'out'.")

while key_while_base == 0:
  key_selected()
