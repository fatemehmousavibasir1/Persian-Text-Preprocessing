# -*- coding: utf-8 -*-
import arabic_reshaper
from bidi.algorithm import get_display
import re
text_to_be_reshaped ='''در شکل 2-1 نرخ اطلاعات اصلی سیگنال (یا کنترل) در مراحل مختلف فرایند نیز آمده است. نرخ اطلاعات در متن اولیه و خام پیام، نسبتاً پایین است (حدود bps 50 (بیت بر ثانیه) مترادف با حدود 8 صدای مختلف در ثانیه، در شرایطی که هر صدا تقریباً 50 سمبل مجزا داشته باشد). بعد از تبدیل کد زبان، با اضافه شدن اطلاعات عروضی گفتار، نرخ اطلاعات تا bps 200 بالا می‌رود. در مراحل بعدی، ارائۀ اطلاعات در قالب سیگنال (یا کنترل) با سرعتی حدود bps 2000 به‌منظور کنترل عصبی تمامی اندام‌های درگیر در تولید گفتار و در حدود bps 50,000 – 30,000 در سطح .سیگنال صوتی ادامه پیدا می‌کند.
روند تشخیص گفتار به‌صورت معکوس، الگوی فرایند تولید گفتار است؛ بنابراین، نرخ اطلاعات در غشای پایه در حدود bps 50,000 – 30,000 و در حین مرحلۀ هدایت عصبی در حدود bps 2000 است. بالاترین سطح پردازش در مغز، سیگنال‌های عصبی را به بازنمایی مجزا تبدیل می‌کند که سرانجام پیام با نرخ بیت پایین تولید می‌شود. 
احتراما پیرو هماهنگیهای انجام شده جهت بازدید دانش آموزان پایه نهم دبیرستان از آزمایشگاهها و کارگاههای دانشکده فنی و مهندسی دانشگاه الزهراء(س)، بدینوسیله درخواست خود جهت انجام بازدید دو گروه 20 نفری از دانش آموزان همراه با تعدادی از دبیران در روزهای چهارشنبه مورخ 22/1/97 و 29/1/97 ساعت 9 تا 12 را تقد‌یم می‌‌دارم.
''' 
print(text_to_be_reshaped)
reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
bidi_text = get_display(reshaped_text)
print(bidi_text)
bidi_text=bidi_text.replace('ﺎ', 'ا')
words=re.findall(r'\w+|\?|\,|\!|\.|\"|\(|\)|\:|\\|\/|\؛|\،|\–|\S+', bidi_text)
print(words)



def stems(word):
   word= re.sub(r'اﻬ', '', word)
   word= re.sub(r'ﺕا', '', word)
   word= re.sub(r'ﻥا', '', word) 
   word= re.sub(r'اه', '', word) 
   word= re.sub(r'ﯼاﻬ', '', word) 
   word= re.sub(r'ﯼاﻫ', '', word) 
   word= re.sub(r'ﺀ', '', word) 
   word= re.sub(r'ﮥ', 'ه', word) 
 
   word= re.sub(r'ﻦﯾﺮﺗ', '', word) 
   word= re.sub(r'ﺮﺗ', '', word) 
   word= re.sub(r'ﯽ', ' ', word)
   word= re.sub(r'ﯼ', '', word)
   word= re.sub(r'ا‌س‌ا', '', word)
   word= re.sub(r'ن‌ی‌گ', '', word)
   word= re.sub(r'هﻥﺍ‌', '', word) 
   word= re.sub(r'ک‌ی', '', word) 
   word= re.sub(r'ن‌ا‌د', '', word) 
   word= re.sub(r'ﻥﺍ', '', word)
   return word

words= " ".join([stems(word) for word in words])
print(words)






words = re.sub(r'[!:,()".;\'?؛،/-]', '', words)

words=re.sub(r'\bﺭﺩ\b\s+',"",words)
words=re.sub(r'\b ﻭ\b\s+'," ",words)
words=re.sub(r'\bاﯾ\b\s+',"",words)
words=re.sub(r'\bاﺑ\b\s+',"",words)
words=re.sub(r'\bﺍﺭ\b\s+',"",words)
words=re.sub(r'\bﻪﺑ\b\s+',"",words)
words=re.sub(r'\bﺰﯿﻧ\b\s+',"",words)
words=re.sub(r'\bﺯﺍ\b\s+',"",words)
words=re.sub(r'\bمی\b\s+',"",words)
words=re.sub(r'\b ﻣ\b\s+',"",words)
words=re.sub(r'\bزا\b\s+',"",words)
words=re.sub(r'\bی‌ب\b\s+',"",words)
words=re.sub(r'\bرب\b\s+',"",words)
words=re.sub(r'\bات\b\s+',"",words)
words=re.sub(r'\bرگ‌‌م\b\s+',"",words)
words=re.sub(r'\bزج\b\s+',"",words)
words=re.sub(r'\bﺭا\b\s+',"",words)

words=re.sub(r'\bbps\b\s+'," bit per second",words)
words=re.sub(r'\b$س$\b\s+'," سلام الله علیها ",words)

words=re.sub(r'\b\d+\b', '', words)

words = re.sub(r'\s+', ' ', words)
print(words)


