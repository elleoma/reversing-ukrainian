## Частина 26 - Дебагування ASM 2 \[Moving Дані між регістрів\]

Для повного змісту змісту всіх уроків, будь ласка, натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте дебагуватимемо другий програмний код нижче:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520143823093.jpg"/></div>

Давайте запустимо GDB і зупинимося на \_start, виконати бінарний і розібратися:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520559684472.jpg"/></div>

Тепер давайте __si__ двічі і __i r__:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520203219432.jpg"/></div>

Як ми бачимо, значення __0x16__ або __22__ десяткове перемістився в EDX успішно. Тепер давайте __si__ знову.

<XyZ9PlH10ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520144473531.jpg"/></XyZ9PlH11ZuK8>

Як ви бачите, ми успішно перемістили EDX в EAX.

Я чекаю побачити вас усіх наступної тижня, коли ми вийдемо на хакінг нашої другої програми збірки!

Дякую за увагу!