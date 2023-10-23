import random
import time

def cikartma():
  cikartma_log = """
    0. seviye = num0 - num1 = ?
    1. seviye = num10 - num11 = ?
    2. seviye = num0 - num1 + num2 = ?
    3. seviye = num10 - num11 + num12 = ?
    out = çıkış
  """
  print(cikartma_log)

  key_while_cikartma = 0
  while key_while_cikartma == 0:
    level_cikartma_select = input("seviye seçiniz: ")

    if level_cikartma_select == "0":
      level_loop_count = int(input("kaç soru çözeceğinizi seçin: "))
      level_loop = 0
      correct_answer = 0
      wrong_answer = 0
      total_time = 0

      while level_loop < level_loop_count:
        num0 = random.randint(0, 9)
        num1 = random.randint(0, 9)
        start_time = time.time() # süreyi başlat
        user_answer = int(input(f"{num0} - {num1} = "))
        end_time = time.time() # süreyi durdur
        pc_answer = num0 - num1

        if user_answer == pc_answer:
          correct_answer += 1
        else:
          wrong_answer += 1
        
        # Sorunun çözümüne harcanan süreyi hesapla ve toplam süreye ekle
        question_time = end_time - start_time
        total_time += question_time


        level_loop += 1
      # Ortalamayı hesapla
      total_questions = correct_answer + wrong_answer
      if total_questions > 0:
          success_rate = (correct_answer / total_questions) * 100
          average_time = total_time / total_questions
          print(f"Doğru Cevaplar: {correct_answer}, Yanlış Cevaplar: {wrong_answer}, Başarı Oranı: {success_rate:.2f}%")
          print(f"Ortalama Soru Çözme Süresi: {average_time:.2f} saniye")
          print(f"kullanılan toplam süre: {int(total_time)} saniye")
      else:
          print("Hiç soru çözülmedi.")

    elif level_cikartma_select == "1":
      level_loop_count = int(input("kaç soru çözeceğinizi seçin: "))
      level_loop = 0
      correct_answer = 0
      wrong_answer = 0
      total_time = 0

      while level_loop < level_loop_count:
        num0 = random.randint(0, 99)
        num1 = random.randint(0, 99)
        start_time = time.time() # süreyi başlat
        user_answer = int(input(f"{num0} - {num1} = "))
        end_time = time.time() # süreyi durdur
        pc_answer = num0 - num1

        if user_answer == pc_answer:
          correct_answer += 1
        else:
          wrong_answer += 1
        
        # Sorunun çözümüne harcanan süreyi hesapla ve toplam süreye ekle
        question_time = end_time - start_time
        total_time += question_time


        level_loop += 1
      # Ortalamayı hesapla
      total_questions = correct_answer + wrong_answer
      if total_questions > 0:
          success_rate = (correct_answer / total_questions) * 100
          average_time = total_time / total_questions
          print(f"Doğru Cevaplar: {correct_answer}, Yanlış Cevaplar: {wrong_answer}, Başarı Oranı: {success_rate:.2f}%")
          print(f"Ortalama Soru Çözme Süresi: {average_time:.2f} saniye")
          print(f"kullanılan toplam süre: {int(total_time)} saniye")
      else:
          print("Hiç soru çözülmedi.")

    elif level_cikartma_select == "2":
      level_loop_count = int(input("kaç soru çözeceğinizi seçin: "))
      level_loop = 0
      correct_answer = 0
      wrong_answer = 0
      total_time = 0

      while level_loop < level_loop_count:
        num0 = random.randint(0, 9)
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        start_time = time.time() # süreyi başlat
        user_answer = int(input(f"{num0} - {num1} + {num2} = "))
        end_time = time.time() # süreyi durdur
        pc_answer = num0 - num1 + num2

        if user_answer == pc_answer:
          correct_answer += 1
        else:
          wrong_answer += 1
        
        # Sorunun çözümüne harcanan süreyi hesapla ve toplam süreye ekle
        question_time = end_time - start_time
        total_time += question_time


        level_loop += 1
      # Ortalamayı hesapla
      total_questions = correct_answer + wrong_answer
      if total_questions > 0:
          success_rate = (correct_answer / total_questions) * 100
          average_time = total_time / total_questions
          print(f"Doğru Cevaplar: {correct_answer}, Yanlış Cevaplar: {wrong_answer}, Başarı Oranı: {success_rate:.2f}%")
          print(f"Ortalama Soru Çözme Süresi: {average_time:.2f} saniye")
          print(f"kullanılan toplam süre: {int(total_time)} saniye")
      else:
          print("Hiç soru çözülmedi.")

    elif level_cikartma_select == "3":
      level_loop_count = int(input("kaç soru çözeceğinizi seçin: "))
      level_loop = 0
      correct_answer = 0
      wrong_answer = 0
      total_time = 0

      while level_loop < level_loop_count:
        num0 = random.randint(0, 99)
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 99)
        start_time = time.time() # süreyi başlat
        user_answer = int(input(f"{num0} - {num1} + {num2} = "))
        end_time = time.time() # süreyi durdur
        pc_answer = num0 - num1 + num2

        if user_answer == pc_answer:
          correct_answer += 1
        else:
          wrong_answer += 1
        
        # Sorunun çözümüne harcanan süreyi hesapla ve toplam süreye ekle
        question_time = end_time - start_time
        total_time += question_time


        level_loop += 1
      # Ortalamayı hesapla
      total_questions = correct_answer + wrong_answer
      if total_questions > 0:
          success_rate = (correct_answer / total_questions) * 100
          average_time = total_time / total_questions
          print(f"Doğru Cevaplar: {correct_answer}, Yanlış Cevaplar: {wrong_answer}, Başarı Oranı: {success_rate:.2f}%")
          print(f"Ortalama Soru Çözme Süresi: {average_time:.2f} saniye")
          print(f"kullanılan toplam süre: {int(total_time)} saniye")
      else:
          print("Hiç soru çözülmedi.")

    elif level_cikartma_select == "out":
      key_while_cikartma = 1