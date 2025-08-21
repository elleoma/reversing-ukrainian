## Частина 24 – Дебагування булевих змінних

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте знову переглянемо наш код.

<XyZ9PlH0ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520236715844.jpg"/></XyZ9PlH1ZuK8>

Давайте дебагуємо.

<XyZ9PlH2ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520194325794.jpg"/></XyZ9PlH3ZuK8>

Давайте зробимо 4 кроки вперед і розіб'ємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520190876822.jpg"/></div>

Давайте розглянемо, що зараз знаходиться в __r3__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520171350771.jpg"/></div>

Як ми можемо побачити, значення в __isHacked__ є __0__ або __false__, що має сенс на основі нашого джерела коду на C++.

Я знаю, що ці уроки можуть здатися незначними, але Реверс-інжиніринг – це все про розбивку речей на їх найпростіші компоненти. Реверс-інжиніринг – це про терпіння і логічну послідовність. Важливо, щоб ви витратили час і пройшли всі ці приклади на приставці Raspberry Pi, щоб мати належну оцінку того, як цей процес працює насправді.

Наступна неділя ми вийдемо на тему Хакінгу булевих змінних.