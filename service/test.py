from pycorrector import Corrector

#pwd_path = os.path.abspath(os.path.dirname(__file__))
#lm_path = os.path.join(pwd_path, './people_chars_lm.klm')
model = Corrector(language_model_path="/Users/huan/Documents/zh_giga.no_cna_cmn.prune01244.klm")

corrected_sent, detail = model.correct('少先队员因该为老人让坐')
print(corrected_sent)
