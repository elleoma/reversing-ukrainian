## Частина 28 - x64 Збірка \[Part 2\]

Для повного змісту змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Продовжимо з ще одним прикладом:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1550829629337.jpg"/></div>

Як ми бачимо, ми переміщаємо __0x10__ в __RAX__ і додаємо __0x05__ в __RAX__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1550829671542.jpg"/></div>

Компілюємо і дозволімо розібратися.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1550829696687.jpg"/></div>

Як бачите, як очікували, ми бачимо наш код в режимі відладки.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1550829787663.jpg"/></div>

Шагаємо двічі, а потім...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1550829821644.jpg"/></XyZ9PlH10ZuK8>

Бачимо __0x15 __або __21__ десяткове число переміщене в __RAX__. Вдірайтесь до цих дуже простих прикладів, коли ми рухаємося далі.