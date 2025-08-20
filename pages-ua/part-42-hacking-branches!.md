## part 42 - Hacking гілки!

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте подивимось на якусь логіку розгалуження:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729104643.jpg"/></div>

Як ми можемо побачити, що ми ініціюємо int до 1 and, якщо змінна дорівнює 1 Перший, якщо оператор друкує відповідь на стандартний вихід.

Давайте складемо:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729192665.jpg"/></div>

Давайте запустимо:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729212374.jpg"/></div>

Як ми можемо логічно бачити, що перша гілка взята. Давайте візьмемо його в Radare and Огляньте на Асамблею:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729291450.jpg"/></div>

Ми можемо побачити логіку розгалуження з стрілками Aqua Color. На __0x0000114a__ ми бачимо, що наша перша гілка завантажується в __rdi__. Візьміть до відома __0x00001148__ Ми бачимо __jne 0x1158__. На __0x00001158__ ми бачимо, що наша друга гілка завантажується в __rdi__.

__Jne__ означає стрибати, якщо not рівний. Це означає, що якщо те, що порівнюється в __0x00001144__, це not дорівнює 1 (ми бачимо, що __1__ порівнюється з тим, що є в __local \ _4h__, що ми знаємо, що це псевдо-код за те, що насправді є __rbp-0x4__.

Для hack ми просто робимо заяву __jne__ до __je__, що є стрибком, якщо рівне, яке ми знаємо, що __cmp__ or порівняння дорівнює, тому воно тепер буде гілкою на "__a - NOT 1! __".

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729757650.jpg"/></div>

Коли ми exit radare, ми бачимо, що ми успішно зламали двійковий:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729786175.jpg"/></div>

Залишайтеся в курсі!