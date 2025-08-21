## part 42 - хакерські гілки!

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте подивимось на якусь логіку розгалуження:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729104643.jpg"/></div>

Як ми, очевидно, бачимо, що ми ініціюємо int до 1, і якщо змінна дорівнює 1 першому, якщо оператор друкує відповідь на стандартний вихід.

Давайте складемо:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729192665.jpg"/></div>

Давайте запустимо:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729212374.jpg"/></div>

Як ми можемо логічно бачити, що перша гілка взята. Давайте візьмемо його в Радаре і оглянемося на збірку:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729291450.jpg"/></div>

Ми можемо побачити логіку розгалуження з стрілками Aqua Color. На __0x0000114a__ ми бачимо, що наша перша гілка завантажується в __rdi__. Візьміть до відома __0x00001148__ Ми бачимо __jne 0x1158__. На __0x00001158__ ми бачимо, що наша друга гілка завантажується в __rdi__.

__Jne__ означає стрибок, якщо не рівний. Це означає, що те, що порівнюється в __0x00001144__, не дорівнює 1 (ми бачимо, що __1__ порівнюється з тим, що є в __LOCAL \ _4H__, який ми знаємо, що це псевдо-код для того, що насправді є в __RBP-0x4__.

Щоб зламати, ми просто робимо заяву __jne__ до __je__, що є стрибком, якщо рівним, який ми знаємо, __cmp__ або порівняння рівне, тому воно тепер буде розгалуженим на "__a не 1! __".

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729757650.jpg"/></div>

Коли ми виходимо з радаре, ми бачимо, що ми успішно зламали двійковий:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729786175.jpg"/></div>

Залишайтеся в курсі!