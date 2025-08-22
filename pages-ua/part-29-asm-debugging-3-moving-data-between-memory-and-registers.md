## Частина 29 - Дебагування ASM 3 \[Moving Дані між пам'яттю та регістрами\]

Для повного змісту змісту всіх уроків, будь ласка, натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте дебагуємо!&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520241537282.jpg"/></div>

У конкретному випадку ми перемістимо значення 10 десятичне в константу ціле ECX.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520590508110.jpg"/></div>

Ми відкриваємо GDB у тихому режимі та зупиняємося на \_start та виконуємо команди вище.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520193652626.jpg"/></div>

Як ми бачимо, коли ми виводимо інформацію про регістри, значення ECX становить 0.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520590507589.jpg"/></div>

Після того, як ми ввійшли двічі, тепер ми бачимо значення ECX як 10 десятичне 0xa в шістнадцятковому вигляді.

Я чекаю на побачення з вами наступної тижня, коли ми підемо до хакінгу нашого третього програми збірки!