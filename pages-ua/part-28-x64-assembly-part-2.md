## part 28 - x64 Асамблея \ [Частина 2 \]

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте продовжимо інший приклад:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1550829629337.jpg"/></div>

Як ми бачимо, ми переміщаємо __0x10__ в __rax__ and, додаючи __0x05__ в __rax__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1550829671542.jpg"/></div>

Ми складаємо and давайте disassemble.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1550829696687.jpg"/></div>

Як ви бачите, як очікувалося, ми бачимо наш код у налагодженні.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1550829787663.jpg"/></div>

Ми стукаємо двічі and тоді ...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1550829821644.jpg"/></div>

Ми бачимо __0x15 __ або __21__ десятковий показник перейшов у __rax__. Знайдіть час, щоб уважно спробувати ці дуже прості приклади, коли ми йдемо вперед.