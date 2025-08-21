## Частина 29 - Дебагування ASM 3 \[Moving Дані між пам'яттю та регістрами\]

Для повного змісту змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть обговорені.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте дебагуватимемо!&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520241537282.jpg"/></div>

У конкретному випадку ми перемістимо значення  у константу ціле число 10 десятичне в ECX.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520590508110.jpg"/></div>

Ми відкриваємо GDB у тихому режимі та зупиняємося на \_start та виконуємо за допомогою команд вище.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520193652626.jpg"/></div>

Як ми бачимо, коли ми виводимо інформацію про регістр, значення ECX становить 0.

<XyZ9PlH10ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520590507589.jpg"/></XyZ9PlH11ZuK8>

Після того, як ми ввійшли двічі, тепер ми бачимо значення ECX як 10 десятичне значення 0xa у вигляді шістнадцятирічного числа.

Я чекаю на побачення з вами наступної тижня, коли ми підемо до хакінгу нашого третього програми збірки!

Очікуйте мене наступної тижня, коли ми підемо до хакінгу нашої третього програми збірки!