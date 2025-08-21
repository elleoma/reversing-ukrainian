## PART 26 - налагодження ASM 2 \ [Переміщення даних між регістрами \]

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте налагоджуємо другу програму нижче:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520143823093.jpg"/></div>

Давайте стріляємо GDB і розірвемося на \ _start, запускаємо двійкові та диски:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520559684472.jpg"/></div>

Тепер давайте __si__ двічі та __i r__:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520203219432.jpg"/></div>

Як ми бачимо, значення __0x16__ або __222 Decimal успішно переходив у EDX. Тепер давайте знову __SI__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520144473531.jpg"/></div>

Як ви бачите, ми успішно перенесли EDX в EAX.

Я з нетерпінням чекаю зустрічі з вами на наступному тижні, коли ми занурюємось у зламу нашої другої програми Асамблеї!