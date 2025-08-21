## part 29 - налагодження ASM 3 \ [переміщення даних між пам'яттю та регістрами \]

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте налагоджуємо! &nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520241537282.jpg"/></div>

Зокрема, ми перемістимо значення всередині постійного цілого числа 10 десятків у ECX.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520590508110.jpg"/></div>

Ми відкриваємо GDB в тихому режимі і розбиваємо \ _start і запускаємо, слідуючи за командами вище.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520193652626.jpg"/></div>

Як ми бачимо, коли ми реєструємо інформацію, значення ECX дорівнює 0.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520590507589.jpg"/></div>

Після того, як ми вступаємо двічі, тепер ми бачимо значення ECX як 10 десятків 0xa HEX.

Я з нетерпінням чекаю побачити вас на весь наступний тиждень, коли ми занурюємось у зламу нашої третьої програми Асамблеї!