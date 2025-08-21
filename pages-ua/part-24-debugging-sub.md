## part 24 - налагодження SUB

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Як було сказано, віднімання в ARM має чотири інструкції, які є SUB, SBC, RSB та RSC. Ми розпочнемо сьогодні з SUB.

Будь ласка, майте на увазі, коли ви додасте суфікс S на кінці кожного, наприклад, Subs, SBC, RSB, RSC, це вплине на прапори. На попередніх уроках ми витратили достатньо часу на прапори, щоб ви зараз мали на увазі це.

Давайте переглянемо наш приклад SUB:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520242319262.jpg"/></div>

Ми просто приймаємо __67 Decimal__ і переходимо до __R1__ та __53 Decimal__ і переходимо до __R2__ і віднімають R1 - r2 і ставимо результат __r0__.

Давайте налагоджуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520211071860.jpg"/></div>

Як ми бачимо, регістри зрозумілі. Давайте перейдемо і подивимось, якою є значення __R0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520241790816.jpg"/></div>

Як ви бачите вище __R0__ тепер __Decimal__ __14__, який працює як очікувалося.

Наступного тижня ми занурюємось у хакерство SUB.