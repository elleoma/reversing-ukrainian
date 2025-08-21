## Частина 32 - x64 Збірка \[Part 6\]

Для повного змісту змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте переглянемо наш код.

<XyZ9PlH1ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553248751760.jpg"/></XyZ9PlH2ZuK8>

Компілюємо...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553248766003.jpg"/></div>

Дебагуємо...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553248783477.jpg"/></div>

Давайте оцінюємо вміст адреси пам'яті 0x6000d8.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553248844375.jpg"/></div>

Як ми бачимо, "__Hello World__" з поверненням символу буде потім переміщено в наш __RSI__ регістр.

Наступна неділя ми розглянемо це трохи ближче.