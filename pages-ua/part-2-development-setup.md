Частина 2 - Налаштування середовища розробки

Для повного змісту змісту всіх уроків, будь ласка, натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/hacking\_c-\_arm64

Сьогодні ми встановлюємо своє середовище розробки. Нам потрібні наступні речі:

<pre spellcheck="false">Raspberry Pi 4
64GB MicroSD Card
Micro SD Card Reader/Writer
Download 64-bit Kali Linux ARM Image
Download balenaEtcher
Flash Kali Linux ARM Image
OPTIONAL: Video [Load Kali RPI 4]
How To Install VIM
Git Clone &amp; Build Radare2 Software
</pre>

<XyZ9PlH10ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1606060809296.jpg"/></XyZ9PlH11ZuK8>

__Распberry Pi 4__

https://www.adafruit.com/product/4292

__64ГБ MicroSD картка__

https://www.sparkfun.com/products/16498

__Мікро SD картка читач__

r/Writer__

https://www.walmart.com/ip/Iogear-GFR204SD-SD-MicroSD-MMC-Card-Reader-and-Writer/15522266

__Завантажте 64-бітну Kali Linux ARM образ__

Kali Linux RaspberryPi 2 (v1.2), 3 і 4 (64-Біт) (img.xz)__ __

https://www.offensive-security.com/kali-linux-arm-images

__Завантажте balenaEtcher__

https://www.balena.io/etcher

__Схопіть Kali ARM образ__

__ОПЦІОНАЛЬ: Відео \[Load Kali RPI 4\]__

<a href="https://youtu.be/Jquf9BDm4iU" rel="nofollow noopener" target="_blank">https://youtu.be/Jquf9BDm4iU</a>

__Як встановити VIM__

https://www.simplified.guide/ubuntu/install-vim 

Після отримання всіх необхідних пристроїв та програмного забезпечення, будь ласка, перегляньте відео щодо встановлення середовища, оскільки Null Byte зробив чудову роботу зі створення крокової інструкції, яка допоможе вам встановити середовище за кілька хвилин.

Наступний крок - git clone та побудувати Radare2 програмне забезпечення, оскільки цього потрібно для отримання останньої версії, оскільки стандартна версія, інтегрована в Kali, не буде достатньо для наших потреб.

__Git Clone &amp; Build Radare2 Програмне забезпечення__

https://github.com/radareorg/radare2

<pre spellcheck="false">cd Documents
git clone https://github.com/radareorg/radare2.git
sys/install.XyZ9PlH12ZuK8
</pre>

Останнім кроком буде використання текстового редактора для створення нашого коду. Kali має обидва текстові редактори VIM та Nano, інтегровані в нього. Ми використовуватимемо VIM, але ви вільні використовувати будь-який, який вам зручно.

У наступному урокі ми напишемо свій перший програму на C++, яка буде "Hello World!".