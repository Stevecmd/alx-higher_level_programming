#include <Python.h>

/**
 * print_python_list - Print information about a Python list object
 * @list_obj: A pointer to a PyObject representing a list object
 */
void print_python_list(PyObject *list_obj)
{
	int num_elements, allocated, i;
	const char *elem_type;
	PyListObject *list = (PyListObject *)list_obj;
	PyVarObject *var = (PyVarObject *)list_obj;

	num_elements = var->ob_size;
	allocated = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", num_elements);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < num_elements; i++)
	{
		elem_type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, elem_type);
		if (strcmp(elem_type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Print information about a Python byte object
 * @byte_obj: A pointer to a PyObject representing a byte object
 */
void print_python_bytes(PyObject *byte_obj)
{
	unsigned char i, size;
	PyBytesObject *bytes = (PyBytesObject *)byte_obj;

	printf("[.] bytes object info\n");
	if (strcmp(byte_obj->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)byte_obj)->ob_size);
	printf("  attempting string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)byte_obj)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)byte_obj)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
