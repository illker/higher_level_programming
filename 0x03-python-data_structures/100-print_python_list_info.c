#include <Python.h>

/**
 * print_python_list_info- prototype function
 * @p: Variable char pointer
 * Return: Void
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	size = PySIZE(p);
	alloc = ((PylistObject *)p)->allocated;

	printf("[*] Size of the Python List = %d", size);
	printf("[*] Allocated = %d", alloc);

	for (i = 0, i < size, i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
