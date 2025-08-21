## PART 22 - Змінні символи хакерства

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте розглянемо наш код.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520232430320.jpg"/></div>

Давайте хакемо!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520194771044.jpg"/></div>

Ми знову бачимо, що пряме значення __0x6e__ перемістилося в __r3__ на __main+12__, що є нашим "__n__".

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520195499705.jpg"/></div>

Після вступу в 4 рази і перевірте значення в __R3__, яке ми чітко бачимо як "__n__".

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520233196032.jpg"/></div>

Давайте зламаємо значення в __R3__ до "__Y__", а потім перегляньте значення в __R3 __. &nbsp;WE тепер чітко бачимо, що він був змінений на "__Y__".

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520232999022.jpg"/></div>

Коли ми продовжуємо, ми успішно бачимо, як наш хак працював! &nbsp; Ми бачимо значення друку "__Y__" до стандартного виходу.

Наступного тижня ми зануримося в булеві змінні.