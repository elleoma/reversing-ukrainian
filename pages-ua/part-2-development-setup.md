## PART 2 - Налаштування розвитку

Для повного змісту всіх уроків, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює. https://github.com/mytechnotalent/hacking\_c-\_arm64

Сьогодні ми збираємося створити своє середовище розвитку. Нам знадобиться наступне:

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

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1606060809296.jpg"/></div>

__Raspberry Pi 4__

https://www.adafruit.com/product/4292

__64 Гб microSD chard__

https://www.sparkfun.com/products/16498

__Micro SD -зчитувач карт/письменник__

https://www.walmart.com/ip/Iogear-GFR204SD-SD-MicroSD-MMC-Card-Reader-and-Writer/15522266

__Download 64-бітний Kali Linux ARM Image__

Kali Linux RaspberryPi 2 (v1.2), 3 and 4 (64-біт) (img.xz) __ __

https://www.offensive-security.com/kali-linux-arm-images

__Load Balenaetcher__

https://www.balena.io/etcher

__Flash kali ARM image__

__Optional: Video \ [Завантажити kali rpi 4 \] __

<a href="https://youtu.be/Jquf9BDm4iU" rel="nofollow noopener" target="_blank">https://youtu.be/Jquf9BDm4iU</a>

__ Як встановити vim__

https://www.simplified.guide/ubuntu/install-vim 

Отримавши всі необхідні пристрої and Програмне забезпечення, перегляньте відео про те, як налаштувати своє середовище, оскільки Null Byte зробив дивовижну роботу з покроковою підручник, яка отримає вас налаштування за лічені хвилини.

Наступним кроком є те, що клон and побудувати програмне забезпечення Radare2, оскільки це ми хочемо, щоб остання версія, оскільки стандартна версія, вбудована в Kali, буде not достатньою для наших потреб.

__Git клон &amp; побудувати Radare2 програмне забезпечення__ __

https://github.com/radareorg/radare2

<pre spellcheck="false">cd Documents
git clone https://github.com/radareorg/radare2.git
sys/install.sh
</pre>

Нарешті ми будемо використовувати текстовий редактор для створення нашого коду. У Kali вбудовано обидва редактори тексту Vim and. Ми будемо використовувати vim, але ви free, щоб використовувати будь -який вам зручний.

На нашому наступному уроці ми напишемо нашу першу програму C ++, яка буде "Hello World!".