## Частина 33 - x64 Збірка \[Part 7\]

Для повного змісту змісту всіх уроків, будь ласка, натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте знову переглянемо наш код джерела.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853169947.jpg"/></div>

Давайте скомпілюємо...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853185424.jpg"/></div>

Як ми вже бачили раніше, це створює нашу стрічку.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853213341.jpg"/></div>

Ми відлагоджували і бачили, як стрічка переміщується в __0x6000d8__ і потім в __RSI__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853259407.jpg"/></div>

Щоб підтвердити, ми можемо побачити стрічку на згаданій адресі. АТТЕНЦІЯ ДЛЯ КРАСНОГО!:)...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853296959.jpg"/></div>

У цьому місці ми демонструємо, що маємо можливість просто хакнути і переозначити стрічку в пам'яті. Ми просто встановлюємо довжину байта char і встановлюємо нову стрічку.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853373225.jpg"/></div>

Як ми бачимо, ми успішно змінили стрічку в пам'яті.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853413835.jpg"/></div>

Ми продовжили і пройшли через бінарний файл і побачили, що наш хак продовжується через __RSI__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853461475.jpg"/></div>

Нарешті, коли ми запустили бінарний файл, ми побачили, що успішно хакнули його роботу. Це дуже простий приклад, але він показує силу справжнього розуміння збірки на цьому рівні. Інструменти GUI-відладчика також забезпечуватимуть цю функціональність, але я люблю використовувати командні інструменти, щоб вони можна було використовувати в кожному середовищі.

Мета цих інструментів - зрозуміти, як це робиться, і що шукати, коли ви професійно відтворюєте в реальному часі. Вам потрібно зрозуміти, як атакувальник може змінювати пам'ять і інструкції. Нам потрібні більше професійних RE's, щоб допомогти захистити інфраструктури по всьому світу, і надіяється, що ці уроки мотивують вас до кар'єри в такому напрямку.