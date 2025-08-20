## part 24 - налагодження SUB

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Як було сказано, віднімання в ARM має чотири інструкції, які є SUB, sbc, rsb and rsc. Ми розпочнемо сьогодні з SUB.

Будь ласка, майте на увазі, коли ви add s суфікс s на кінці кожного, наприклад, підводки, sbcs, rsbs, rscs, це вплине на прапори. На попередніх уроках ми витратили достатньо часу на прапори, щоб ви зараз мали на увазі це.

Давайте переглянемо наш приклад SUB:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520242319262.jpg"/></div>

Ми просто приймаємо __67 Decimal__ and переміщено в __r1__ and __53 decimal__ and в __r2__ and r1 - nbsp and pute juclh23zuk8 and pute juct

Давайте налагоджуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520211071860.jpg"/></div>

Як ми бачимо, регістри зрозумілі. Давайте перейдемо через and, подивимось, якою є значення __r0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520241790816.jpg"/></div>

Як ви бачите вище __R0__ тепер __Decimal__ __14__, який працює як очікувалося.

Наступного тижня ми зануримось у SUB hacking.