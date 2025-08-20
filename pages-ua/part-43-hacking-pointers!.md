## part 43 - Hacking покажчики!

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Ми в кінці дороги. Це остаточне відео в серії x64. Заключна тема - це покажчики.

Що таке покажчики? Почнемо з прикладу.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567286671465.jpg"/></div>

Покажчик - це не що інше, як адреса пам'яті. Коли ми компілюємо, ми чітко побачимо, де лотерея \ _number живе в відображеній пам’яті (це запущений приклад на відміну від наших прикладів RADARE беззастережних).

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567286745307.jpg"/></div>

Давайте add справжній вказівник на приклад:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567287725406.jpg"/></div>

Ми бачимо те саме значення:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567287787090.jpg"/></div>

Давайте експериментуємо більше:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567288396508.jpg"/></div>

Ми бачимо вказівку вказівника на нову адресу:

hack

Пам'ятайте покажчики - це адреси пам'яті інших змінних. Давайте подивимось на це іншим способом:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567289354121.jpg"/></div>

Давайте складемо:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567289368216.jpg"/></div>

Ми поважаємо, роблячи наступне:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567289646596.jpg"/></div>

Тоді ми складаємо:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567289657671.jpg"/></div>

Ми можемо побачити, що вказівник на повагу дорівнює 777.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567290644015.jpg"/></div>

Ми можемо побачити приклад із масивом:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567290665083.jpg"/></div>

Давайте налагоджуємо:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567290786481.jpg"/></div>

Тоді ми disassemble:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567290800965.jpg"/></div>

Давайте hack!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567292294462.jpg"/></div>

Давайте переглянемо двійкове:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567292311387.jpg"/></div>

Ми бачимо, що ми зламали значення 3 з 6.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567292376880.jpg"/></div>

Ми можемо побачити, що ми зробили успішний hack.

Я сподіваюся, що протягом багатьох років через буквальні сотні x86, ARM and x64 у вас є основні знання про те, як зробити добро, щоб захистити критичні інфраструктури від шкідливих рук, розуміючи, як ворог працює. Іди and Зробіть хорошу роботу!