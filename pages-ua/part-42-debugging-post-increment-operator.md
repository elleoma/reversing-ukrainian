---
{}
---

## Part 42 – налагодження Post-Increment Operator

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює. & NBSP; __ Ploadholder_14__

Давайте переглянемо наш код.

__Placeholder_0 __#включає & lt; iostream & gt;

int main(void) {
& nbsp; & nbsp; & nbsp; __ ploadholder_18__ mynumber = 16;
& nbsp; & nbsp; & nbsp; __ ploadholder_19__ mynewnumber = ++ mynumber;

& nbsp; & nbsp; & nbsp; std :: cout & lt; & lt; mynewnumber & lt; & lt; std :: endl;

& nbsp; & nbsp; & nbsp; повернення 0;
}
__Placeholder_1__

We create a змінна __myNumber = 16__ to which we create another змінна __myNewNumber__ which post-increments the value of __myNumber__.&nbsp;We see that when we execute our code it shows __16__ as the value of __myNewNumber__ and __17__ as the value of __myNumber__ as __myNewNumber__ does __Placeholder_24__ збільшується, оскільки лише __mynumber__ збільшується, оскільки це пост -оператор.

Коли ми після запровадження значення змінної збільшується після призначення її іншій змінній. & NBSP; наприклад, __Mynumber__ є __16__, тому вона збільшується після призначення до __mynewnumbum__, тому ми отримуємо __17__.

Давайте налагоджуємо.

__Placeholder_2____placeholder_3____placeholder_4__

Давайте розірвемося на __ \*main+28 __ і продовжуємо.

__Placeholder_5____Placeholder_6____Placeholder_7__

Як ми бачимо значення в __r3 __ен 16 __placeholder_21__ значення в __r2 __is 17. Ми можемо бачити, що, як вони завантажуються з пам'яті в регістри в __ \*main+12__ безпосередньо за допомогою __ -mov__ інструкції __placeholder_22__ __ \*main+24__ ми __ __plicholder_16______ ________ ____ ____ ____ ____ ____ __ ____ ____ ____ ____ ____ ____ __ ____ ____ ____ ____ ____ __ ________ ____ __ __ __t __ значення в __R2__.

__Placeholder_8____Placeholder_9____Placeholder_10__

По мірі продовження ми можемо побачити функцію __cout __c ++ під назвою, яка переливає значення до терміналу (стандартний вихід), як очікувалося.

__Placeholder_11____Placeholder_12____Placeholder_13__________________

Next week we will dive into Hacking Post-Increment Operator.