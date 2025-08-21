## part 33 - x64 Асамблея \ [Частина 7 \]

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте знову розглянемо наш вихідний код.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853169947.jpg"/></div>

Давайте складемо ...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853185424.jpg"/></div>

Як ми бачили до того, як він створює нашу струну.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853213341.jpg"/></div>

Ми налагоджуємо і бачимо, як рядок переміщується в __0x6000d8__, а потім __rsi__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853259407.jpg"/></div>

Тільки для перевірки ми можемо побачити рядок за вищезгаданою адресою. Тепер для трохи задоволення :) ...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853296959.jpg"/></div>

Тут ми демонструємо, що маємо силу просто зламати та переосмислити рядок у пам'яті. Ми просто встановлюємо довжину байтів Char і встановлюємо новий рядок.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853373225.jpg"/></div>

Як ми бачимо, ми успішно змінили рядок у пам'яті.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853413835.jpg"/></div>

Ми продовжуємо і біжимо через двійкову та бачимо, що наш хак продовжується через __rsi__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853461475.jpg"/></div>

Нарешті ми бачимо, коли запускаємо двійкове, ми успішно зламали його операцію. Однак це дуже простий приклад показує силу справді розуміння складання на цьому рівні. Інструменти налагодження GUI також забезпечать цю функціональність, однак мені подобається використовувати інструменти командного рядка, щоб вони могли бути використані в кожному середовищі.

Мета цих інструментів-зрозуміти, як це робиться і на що звернутися, коли ви професійно повертаєте в режимі реального часу. Вам потрібно зрозуміти, як зловмисник може змінити пам'ять та/або інструкції. Нам потрібно більше професійних РЕ, щоб допомогти захистити інфраструктуру у всьому світі, і, сподіваємось, ці навчальні посібники мотивують вас до кар’єри в такому.