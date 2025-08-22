## Частина 28 - Програма ASM 3 \[Moving Дані між пам'яттю та регістрами\]

Для повного змісту змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

У нашій третьій програмі ми продемонструємо, як можна перемістити дані між пам'яттю та регістрами.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520175192505.jpg"/></div>

У конкретно ми перемістимо значення внутрішнього константного цілого числа 10 десятичне в ECX.

Увага! Аби збудувати, ми пишемо:

__as –32 -o moving\_data\_between\_memory\_and\_registers.o moving\_data\_between\_memory\_and\_registers.s__

Аби зв'язати об'єкт file ми пишемо:

__ld -m elfMDXX\_i386XMDX -o moving\_data\_between\_memory\_and\_registers moving\_data\_between\_memory\_and\_registers.o __

Я чекаю на всіх вас наступної тижня, коли ми зануримося в відлагодження нашої третьої програми збірки!

Мовчання!