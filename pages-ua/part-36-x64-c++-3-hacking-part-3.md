## part 36 - x64 c ++ 3 хакерство \ [частина 3 \]

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте розглянемо наш код:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1564757193950.jpg"/></div>

Компіляція:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1564758303402.jpg"/></div>

Бігати:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1564757239511.jpg"/></div>

Згадаймо цей рядок вище, коли ми порівнюємо з нашим зламаним двійковим.

Давайте відкриємо наш двійковий режим запису і просто проаналізуємо двійковий.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1564757311281.jpg"/></div>

Гаразд, тут багато чого відбувається. Давайте розберемо його. Спочатку ми відкриваємо Radare 2 в режимі запису, ввівши '__r2 -w ./1__', а потім використовуємо команду '__aaa__' для аналізу двійкового. Потім ми використовуємо '__s sym.main__', щоб прагнути до основного рутини бінарного, який є нашою точкою входу. Тоді ми виконуємо команду '__pdf__', щоб розібрати двійкову.

Ми бачимо, що ми називаємо прологом, де ми push&nbsp;__rbp__&nbsp; stack базовий вказівник на стек. Потім ми переміщуємокси9plh30zuk8__rsp__&nbsp;into&nbsp;__rbp__&nbsp; для безпечного зберігання, а потім ми заповідниках9plh34zuk8__x10__&nbsp;Hex або 16 Decimal

Якщо нічого з цього не має сенсу, поверніться до початку підручника, щоб переглянути основні збори та регістри, як це критично, ви розумієте це, перш ніж ми рухаємось вперед.

Ми можемо чітко побачити QWord '__Hello World \\ n__' на пам'яті адреса&nbsp;__0x2005__&nbsp; і тоді ми бачимо наш C ++ бібліотека call для вихідного потоку, який is&nbsp;__cout__&nbsp;topeance toeartal

Давайте вивчаємо Excie&nbsp;__0x2005__&nbsp;, щоб перевірити, що наша рядок знаходиться в цьому місці:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1564757423920.jpg"/></div>

Тепер час на хак!

Давайте зламаємо цінність для чогось подібного:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1564757454631.jpg"/></div>

Тепер давайте подивимось, що зараз всередині значення пам'яті @ __0x2005__!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1564757528202.jpg"/></div>

Бум! Як ми бачимо, ми зламали значення, і коли ми кинемо Радаре 2, він напише його і змінює наш двійковий як такий.,

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1564757568026.jpg"/></div>

Як ви бачите, ми зламали двійкову! Це дуже основне, але тепер у вас є елементарний рівень розуміння зворотної інженерії бінарного C ++.

Наступного тижня ми продовжимо нашу подорож у C та покрокову інженерну інженерію.