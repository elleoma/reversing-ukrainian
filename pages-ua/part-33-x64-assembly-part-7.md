## Частина 33 - x64 Збірка \[Part 7\]

Для повного змісту змісту всіх уроків, будь ласка, натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть обговорені.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте знову переглянемо наш код джерела.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853169947.jpg"/></div>

Давайте скомпілюємо...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853185424.jpg"/></div>

Як ми вже бачили раніше, він створює нашу стрічку.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853213341.jpg"/></div>

Ми відлагоджуємо і бачимо, як стрічка переміщується в __0x6000d8__ і потім в __RSI__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853259407.jpg"/></div>

Щоб підтвердити, можна побачити стрічку на згаданій адресі. АТУТУ ДЛЯ НЕКОТОРИЙ ВІДВІДКУ :)...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853296959.jpg"/></XyZ9PlH10ZuK8>

У цьому місці ми демонструємо, що маємо можливість просто хакнути і переозначити стрічку в пам'яті. Ми просто встановлюємо довжину байта char і встановлюємо нову стрічку.

<XyZ9PlH11ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853373225.jpg"/></XyZ9PlH12ZuK8>

Як ми бачимо, ми успішно змінили стрічку в пам'яті.

<XyZ9PlH13ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853413835.jpg"/></XyZ9PlH14ZuK8>

Ми продовжуємо і проходимо через бінарний файл і бачимо, що наш хак продовжується через __RSI__.

<XyZ9PlH15ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853461475.jpg"/></XyZ9PlH16ZuK8>

Нарешті ми бачимо, коли ми запускаємо бінарний файл, ми успішно хакнули його роботу. Це дуже простий приклад, однак він демонструє силу справжньої розуміння збірки на цьому рівні. Інструменти відлагоджувачі GUI також надасть цю функціональність, однак мені подобається використовувати командні інструменти, щоб вони можна було використовувати в кожному середовищі.

Мета цих інструментів — ПОНЯТИ, як це робиться, і що шукати, коли ви професійно відлагоджуєте в реальному часі. Вам потрібно зрозуміти, як атакувальник може змінювати пам'ять і інструкції and/or. Нам потрібні більше професійних RE's, щоб допомогти захистити інфраструктури по всьому світу і надіямо, що ці уроки мотивують вас до кар'єри в такій галузі.