## part 15 - налагодження ADD

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте розглянемо наш приклад ADD нижче:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520244359354.jpg"/></div>

Знову ми бачимо, що ми переміщуємо десятку __67__ на __r1__ and десятковий __53__ __r2__. Тоді ми __add r1 __ та __r2__ and поставили результат у __r0__.

Давайте складемо:

__AS -O add.O add.S__

__ld -o add add.o__

Давайте введемо в GDB для налагодження:

__gdb -q add__

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520594706178.jpg"/></div>

Ми можемо бачити, що коли ми b__ \ _start__, розірвайтеся на старті and __r__, запустіть ми бачимо disassembly. Якщо ви робите __i r__, ми бачимо регістри інформації, де ми помічаємо, що наш __cpsr__ є __0x10__.

Коли ми знову крокуємо and інформаційних реєстраторів:

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520213487826.jpg"/></div>

Ми помічаємо __0x43__ hex or __67__ десятковий у __r1__. Ми також помічаємо, що прапори незмінні (__cpsr 0x10__).

Давайте знову стекти and інформаційних реєстрів:

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520594706126.jpg"/></div>

Ми можемо побачити __r0 __now тримає __0x78__ hex or __120__ десятковий. Ми успішно побачили інструкцію add на місці and Ми знову помічаємо, що реєстр прапорів (__CPSR__) залишається незмінним цією операцією.

Наступного тижня ми зануримось у Hacking ADD.