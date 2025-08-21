## Частина 29 - x64 Збірка \[Part 3\]

Для повного змісту змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Сьогодні ми продовжимо нашу навчальну програму з простим прикладом віднімання. Давайте розглянемо джерельний код:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1551437589689.jpg"/></div>

Давайте скомпілюємо та запустимо відлагоджувач:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1551437628625.jpg"/></div>

Давайте запустимо та розіб'ємо:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1551437662831.jpg"/></div>

Як ми бачимо дуже добре, ми завантажуємо __16__ або __0x10__ в __EAX__ і потім віднімаємо __5__ від нього в наступному інструкції.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1551437723578.jpg"/></div>

Ми крокуємо двічі, а потім дивимося на отриманий результат в __RAX__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1551437759416.jpg"/></XyZ9PlH10ZuK8>

Як ми бачимо, результатом є 0xb або 11 десятичний, як очікувалося. Важливо, щоб ви спробували ці прості приклади, щоб отримати уявлення про те, що відбувається, коли ми починаємо відлагоджувати C++ код у майбутніх навчальних матеріалах.