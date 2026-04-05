#risiti ya mauzo kwa bidhaa zaidi ya moja
# jumla_kuu = 0
# jumla_kodi =  0 
# bidhaa_zote = []
# from datetime import datetime
# while True:
#     try:
#         control = int(input("1 kuingiza bidhaa  0 kumaliza"))
#         if control == 0:
#             break
#         bidhaa = input("ingiza jina la bidhaa  ")
#         bei = float(input("ingiza bei ya bidhaa  "))
#         idadi = int(input("ingiza idadi ya bidhaa "))
#         kiasi = bei * idadi
#         kodi = 0.18 * kiasi
#         jumla = kiasi + kodi
#         jumla_kuu += jumla
#         jumla_kodi += kodi 
#         bidhaa_zote.append((bidhaa,bei,idadi,jumla))
#     except:
#         print("Tafadhali ingiza namba")
#         exit()
# print("=" * 40)
# tarehe = datetime.now()
# tarehe_m = tarehe.strftime("%d-%m-%Y")
# muda = tarehe.strftime("%H:%M:%S")
# print(f"{'SELEMANI MIX SHOP':^40}")
# print(f"{'SIMU:  0623017380':^40}")
# print("=" * 40)           
# print(f"Tarehe:  {tarehe_m}")  
# print(f"Muda:   {muda}")
# print("-" * 40)
# print(f"{'Bidhaa':<15}{'bei':>7}{'idadi':>8}{'jumla':>10}") 
# for b in bidhaa_zote:
#     print(f"{b[0]:<15}{b[1]:>7}{b[2]:>8}{b[3]:>10}")
# print("-" * 40)
# print(f"VAT(18%):  {jumla_kodi}" )
# print("=" * 40)
# print(f"JUMLA KUU:  {jumla_kuu}")
# print(f"{'ASANTE KWA KUNUNUA':^40}")    
# print("=" * 40) 



# #building a travel whether planner       
# distance_mi = 0.5
# is_raining = True
# has_bike = True
# has_car = False
# has_ride_share_app = False

# if not distance_mi:
#     print(False)
# elif distance_mi <= 1 and not is_raining:
#     print(True)
# elif distance_mi <= is_raining:
#     print(False) 
# elif (distance_mi  > 1 and distance_mi <= 6 ) and (is_raining and not has_bike):
#     print(False)
          
# elif (distance_mi > 1 and distance_mi <= 6 ) and (has_bike and not is_raining):
#     print(True) 
# elif distance_mi > 6 and (has_car or has_ride_share_app):
#     print(True)
# else:
#     print(False)                   




# ##building an apply Discount Function
# def apply_discount(price, discount):
#     if not isinstance(price, (int, float)):
#         return 'The price should be a number'
#     elif not isinstance(discount, (int, float)):  
#         return 'The discount should be a number'
#     elif price <= 0:
#         return 'The price should be greater than 0'
#     elif discount < 0 or discount > 100: 
#         return 'The discount should be between 0 and 100'
#     else:
#         final_price = price - (discount/100 * price)
#         print(final_price)
# apply_discount(50,0)   




#building a caesar cipher
def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)            
           
           
           
           
###In this lab you will practice the basics of Python by building a small app that creates a character for an RPG adventure
           