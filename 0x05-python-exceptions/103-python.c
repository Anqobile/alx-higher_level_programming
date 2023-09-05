#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints info about the Python lists.
 * @p: A list object PyObject.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, h;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (h = 0; h < size; h++)
	{
		type = list->ob_item[h]->ob_type->tp_name;
		printf("Element %ld: %s\n", h, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[h]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[h]);
	}
}

/**
 * print_python_bytes - Prints info about the Python byte objects.
 * @p: A byte object PyObject.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, h;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", size);
	for (h = 0; h < size; h++)
	{
		printf("%02hhx", bytes->ob_sval[h]);
		if (h == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints info about the Python float objects.
 * @p: A float object PyObject.
 */
void print_python_float(PyObject *p)
{
	char *buffer = NULL;

	PyFloatObject *float_objt = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(float_objt->ob_fval, 't', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	PyMem_Free(buffer);
}


