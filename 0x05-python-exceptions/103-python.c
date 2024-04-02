#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p) {
    Py_ssize_t p_size = 0;
    int i = 0;

    fflush(stdout);
    printf("[*] Python list info\n");

    if (!PyList_CheckExact(p)) {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    p_size = PyList_GET_SIZE(p);
    printf("[*] Size of the Python List = %zd\n", p_size);
    printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < p_size; i++) {
        PyObject *item = PyList_GET_ITEM(p, i);
        printf("Element %d: %s\n", i, item->ob_type->tp_name);

        if (PyBytes_CheckExact(item))
            print_python_bytes(item);
        else if (PyFloat_CheckExact(item))
            print_python_float(item);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t p_size = 0;
    char *string = NULL;
    int i = 0;

    fflush(stdout);
    printf("[.] bytes object info\n");

    if (!PyBytes_CheckExact(p)) {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    p_size = PyBytes_Size(p);
    printf("  size: %zd\n", p_size);

    string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
    printf("  trying string: %s\n", string);

    printf("  first %zd bytes:", p_size < 10 ? p_size + 1 : 10);
    for (i = 0; i < p_size + 1 && i < 10; i++) {
        printf(" %02hhx", string[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    double value = 0;

    fflush(stdout);
    printf("[.] float object info\n");

    if (!PyFloat_CheckExact(p)) {
        printf("[ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);
    printf("  value: %f\n", value);
}
