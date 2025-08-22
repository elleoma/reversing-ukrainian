## Частина 9 - Примітивний тип даних

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/hacking\_c-\_arm64

Сьогодні ми розберемо перший з примітивних типів даних C++. Тип даних _char_ використовується для зберігання однієї літери і повинен бути оточений одинарними кавичками.

Давайте розглянемо нашу базову приклад.

<pre spellcheck="false">#include &lt;iostream&gt;

int main()
{
    char my_char = 'c';

    std::cout &lt;&lt; my_char &lt;&lt; std::endl;

    return 0;
}
</pre>

Дуже просто. Ми створюємо змінну типу char під назвою _my\_char _і присвоюємо їй літеру _c_.

Далі ми друкуємо її в stdout і нічого більше.

Давайте скомпілюємо і зв'яжемо.

<pre spellcheck="false">g++ -o 0x03_asm64_char_primitive_datatype 0x03_asm64_char_primitive_datatype.cpp
</pre>

Давайте запустимо.

<pre spellcheck="false">./0x03_asm64_char_primitive_datatype
</pre>

Дуже просто ми бачимо наступне.

<pre spellcheck="false">c
</pre>

Видалося успішно відбитися _c_ в терміналі stdout. Дуже просто.

Наступного тижня ми відлагодимо цей дуже простий приклад.