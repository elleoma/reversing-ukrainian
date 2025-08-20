## PART 30 - ASM Hacking 3 \ [Переміщення даних між пам'яттю And Регістри \]

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте hack! &nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520588657073.jpg"/></div>

Зокрема, ми перемістимо значення всередині постійного цілого числа 10 -десяткових у ECX, як і раніше.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520171419386.jpg"/></div>

Ми відкриваємо GDB у тихому режимі and break on \ _start and запустити, дотримуючись команд вище.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520145740732.jpg"/></div>

Як ми бачимо, коли ми реєструємо значення значення ECX дорівнює 0.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520198737146.jpg"/></div>

Як ви бачите, значення ECX становить 10 десятків or 0xa hex, як це було на попередньому уроці, тепер дозволяє hack, що цінує щось інше.

Давайте __SET $ ecx = 1337 __ і зробимо i r.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520588657130.jpg"/></div>

Як ви чітко бачите, ми зламали значення ECX до 0x539 HEX or 1337 DECIMAL.

Як я вже говорив у цій серії. Кожен з цих уроків є дуже прикладами розміру укусу, щоб ви отримали важку м’язову пам’ять про те, як hack через різні ситуації, щоб ви в кінцевому рахунку мали повне оволодіння контролем процесора.

Я з нетерпінням чекаю побачити вас на весь наступний тиждень, коли ми занурюємось у створення нашої четвертої програми Асамблеї!