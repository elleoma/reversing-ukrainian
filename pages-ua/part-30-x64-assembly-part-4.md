## part 30 - x64 Асамблея \ [Частина 4 \]

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Сьогодні ми кодуємо нашу просту програму "Hello World" у складі x64.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1552041593157.jpg"/></div>

Ми просто створюємо рядок у __.data __Section і додаємо символ повернення в кінці оператора. Потім ми виконуємо простий запис call, який використовує векторну таблицю переривання ОС, щоб виплюнути наш рядок у стандартному виході або терміналі.

Ми будемо складати та працювати нижче:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1552041719716.jpg"/></div>

Як ми бачимо "__Hello World__!" було відгукано до терміналу. Наступного тижня ми налагоджуємо цю просту програму в GDB.