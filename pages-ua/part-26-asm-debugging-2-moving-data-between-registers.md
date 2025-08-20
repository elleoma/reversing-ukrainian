## part 26 - налагодження ASM 2 \ [переміщення даних між регістрами \]

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте налагоджуємо другу програму нижче:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520143823093.jpg"/></div>

Давайте стріляємо GDB and Break on \ _start, запустіть двійкові and диски:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520559684472.jpg"/></div>

Тепер давайте __si__ двічі and __i r__:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520203219432.jpg"/></div>

Як ми бачимо значення __0x16__ or __222, десятковий показник успішно перейшов у EDX. Тепер давайте знову __SI__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520144473531.jpg"/></div>

Як ви бачите, ми успішно перенесли EDX в EAX.

Я з нетерпінням чекаю побачити вас на весь наступний тиждень, коли ми занурюємось у hacking нашу другу програму Асамблеї!