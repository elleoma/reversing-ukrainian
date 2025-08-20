## part 33 - x64 Асамблея \ [Частина 7 \]

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте знову розглянемо наш вихідний код.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853169947.jpg"/></div>

Давайте складемо ...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853185424.jpg"/></div>

Як ми бачили до того, як він створює нашу струну.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853213341.jpg"/></div>

Ми налагоджуємо and, дивіться рядок, що переміщується в __0x6000d8__ and, а потім __rsi__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853259407.jpg"/></div>

Тільки для перевірки ми можемо побачити рядок за вищезгаданою адресою. Тепер для трохи задоволення :) ...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853296959.jpg"/></div>

Тут ми демонструємо, що ми маємо силу просто hack and переосмислити рядок у пам'яті. Ми просто встановлюємо довжину байта char and встановивши новий рядок.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853373225.jpg"/></div>

Як ми бачимо, ми успішно змінили рядок у пам'яті.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853413835.jpg"/></div>

Ми продовжуємо and пробігти через двійковий and, див. Наш hack триває через __rsi__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853461475.jpg"/></div>

Нарешті ми бачимо, коли запускаємо двійкове, ми успішно зламали його операцію. Однак це дуже простий приклад показує силу справді розуміння складання на цьому рівні. GUI налагоджувач Інструменти також забезпечать цю функціональність, однак мені подобається використовувати інструменти командного рядка, щоб вони могли бути використані в кожному середовищі.

Мета цих інструментів-зрозуміти, як це робиться and, на що слід шукати, коли ви професійно повертаєте в режимі реального часу. Вам потрібно зрозуміти, як зловмисник може змінити пам'ять and/or інструкції. Нам потрібно більше професійних РЕ, щоб допомогти захищати інфраструктури у всьому світі and, сподіваємось, ці підручники мотивують вас до кар’єри в такому.