## part 36 - x64 c ++ 3 Hacking \ [частина 3 \]

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте розглянемо наш код:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1564757193950.jpg"/></div>

Компіляція:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1564758303402.jpg"/></div>

Бігати:

nbsp

Згадаймо цей рядок вище, коли ми порівнюємо з нашим зламаним двійковим.

Давайте відкриємо наш двійковий режим запису and просто проаналізуйте двійковий.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1564757311281.jpg"/></div>

Гаразд, тут багато чого відбувається. Давайте розберемо його. Спочатку ми відкриваємо Radare 2 в режимі запису, ввівши '__r2 -w ./1__' and, а потім використовуємо команду '__aaa__' для аналізу двійкового. Потім ми використовуємо '__s sym.main__', щоб прагнути до рутини бінарного main, яка є нашою точкою входу. Потім ми виконуємо команду '__pdf__' для disassemble бінарного.

Ми бачимо, що ми називаємо прологом, де ми push&nbsp;__rbp__&nbsp;. Потім ми переміщуємося, Десяткові байти на стеку, щоб звільнити місце для нашої струни.

Якщо нічого з цього не має сенсу, поверніться до початку серії підручник, щоб переглянути основну збірку and регістрів, як це критично, ви розумієте це, перш ніж ми рухаємось вперед.

Ми можемо чітко побачити QWord '__Hello World \\ n__' на пам'ять Addenthd&nbsp;__0x2005__&nbsp;and, тоді ми бачимо наш C ++ бібліотека call для вихідного потоку, що is&nbsp;__cout__cout__cout__cout__cout__cout__cout__cout__cout__cout__cout__cout__cout__cout__cout__cout__cout__cout__cout__s Наш рядок до терміналу.

Давайте вивчаємо Exype&nbsp;__0x2005__&nbsp;, щоб перевірити, що наша рядок знаходиться в цьому місці:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1564757423920.jpg"/></div>

Тепер час для HACK!

Давайте hack цінність для чогось подібного:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1564757454631.jpg"/></div>

Тепер давайте подивимось, що зараз всередині значення пам'яті @ __0x2005__!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1564757528202.jpg"/></div>

Бум! Як ми бачимо, ми зламали значення and, коли ми кинемо Радаре 2, він напише його and, змінюйте наш двійковий як такий.,

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1564757568026.jpg"/></div>

Як ви бачите, ми зламали двійкову! Це дуже основне, але тепер у вас є елементарний рівень розуміння зворотної інженерії бінарного C ++.

Наступного тижня ми продовжимо нашу подорож до C and покроковою інженерною інженерією.