## Частина 28 - Програма ASM 3 \[Moving Дані між пам'яттю та регістрами\]

Для повного змісту змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

У нашій третьій програмі ми продемонструємо, як можна перемістити дані між пам'яттю та регістрами. <XyZ9PlH2ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520175192505.jpg"/></XyZ9PlH3ZuK8>

У конкретному випадку ми перемістимо значення внутрішнього цілого числа 10 десятичне в ECX.

Увага! Для збірки ми пишемо:

__as –32 -o moving\_data\_between\_memory\_and\_registers.o moving\_data\_between\_memory\_and\_registers.s__

Для зв'язування об'єкта file ми пишемо:

__ld -m elf\_i386 -o moving\_data\_between\_memory\_and\_registers moving\_data\_between\_memory\_and\_registers.o __

Чекаю на всіх наступної тижня, коли ми вийдемо на етап відлагодження нашої третьої програми збірки!

Дякую за увагу!