## Частина 26 - Дебагування ASM 2 \[Moving Дані між регістрів\]

Для повного змісту змісту всіх уроків, будь ласка, натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте дебагуватимемо другий програмний код нижче:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520143823093.jpg"/></div>

Давайте запустимо GDB і зупинимося на \_start, виконанні бінарного файлу та розбору:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520559684472.jpg"/></div>

Тепер давайте __si__ двічі та __i r__:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520203219432.jpg"/></div>

Як бачимо, значення __0x16__ або __22__ у десятковій системі числення успішно потрапило в EDX. Тепер давайте __si__ знову.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520144473531.jpg"/></div>

Як бачимо, ми успішно перемістили EDX в EAX.

Я чекаю на побачення з вами наступної тижня, коли ми розпочнемо хакінг нашого другого програми збірки!

Дякую за увагу!