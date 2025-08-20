## part 24 - налагодження булевих змінних

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте переглянемо наш код.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520236715844.jpg"/></div>

Давайте налагоджуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520194325794.jpg"/></div>

Давайте кроком 4 рази and disassemble.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520190876822.jpg"/></div>

Давайте вивчимо, що зараз у __R3__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520171350771.jpg"/></div>

Як ми чітко бачимо, що значення в __ishacked__ є __0__ or __false__, що має сенс на основі нашого вихідного коду C ++.

I know these уроки may seem trivial however зворотна інженерія is all about breaking things down in their most basic components.&nbsp;зворотна інженерія is about patience and logical flow.&nbsp;It is critical that you take the time and work through all of these examples with a Raspberry Pi device so that you can have a proper appreciation for how the процес насправді працює.

Наступного тижня ми зануримось у Boolean змінні Hacking.