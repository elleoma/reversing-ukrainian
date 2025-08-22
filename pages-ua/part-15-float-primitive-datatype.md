## Частина 15 - Примітивний тип даних Float

Для повного змісту змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/hacking\_c-\_arm64

Сьогодні ми розберемося з примітивним типом даних C++ _float_, який зберігає значення з плаваючою комою.

<pre spellcheck="false">#include &lt;iostream&gt;

int main()
{
&nbsp; &nbsp; float my_float = 10.1;

&nbsp; &nbsp; std::cout &lt;&lt; my_float &lt;&lt; std::endl;

&nbsp; &nbsp; return 0;
}
</pre>

Дуже просто ми створюємо змінну типу float і присвоюємо їй просте значення, а потім друкуємо її.

Хай компілюємо і зв'яжемо.

<pre spellcheck="false">g++ -o 0x05_float_primitive_datatype 0x05_float_primitive_datatype.cpp
</pre>

Хай запустимо.

<pre spellcheck="false">./0x05_float_primitive_datatype
</pre>

Ми просто бачимо наступне.

<pre spellcheck="false">10.1
</pre>

Видалося успішно виведено _10.1_ у термінальний вивід stdout. Дуже просто.

Наступного тижня ми відлагодимо цю дуже просту приклад.

Примітка: XMDX - це лише спеціальні символи, які не мають ніякого значення в українському тексті.