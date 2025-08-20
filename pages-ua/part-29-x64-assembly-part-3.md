## part 29 - x64 Асамблея \ [Частина 3 \]

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Сьогодні ми продовжуємо наш підручник з простим прикладом віднімання. Давайте вивчимо вихідний код:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1551437589689.jpg"/></div>

Давайте складемо and запустити налагоджувач:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1551437628625.jpg"/></div>

Давайте запустимо and disassemble:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1551437662831.jpg"/></div>

Як ми бачимо, дуже ми завантажуємо __16__ or __0x10__ hex в __eax__ and, а потім відняти __5__ з нього в наступній інструкції.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1551437723578.jpg"/></div>

Ми стукаємо двічі and, а потім подивимось на отримане значення в __rax__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1551437759416.jpg"/></div>

Як ми бачимо, результат 0xb hex or 11 десятковий, як очікувалося. Важливо, щоб ви спробували ці прості приклади, щоб зрозуміти, що відбувається, коли ми починаємо налагодити код C ++ у майбутніх підручниках.