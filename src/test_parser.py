import parser as p


def test_filter_common():
    data = """
Модуль       Название               Тип драйвера  Дата ссылки           
============ ====================== ============= ======================
1394ohci     1394 OHCI-совместимый  Kernel                              
3ware        3ware                  Kernel        19.05.2015 1:28:03    
ACPI         Драйвер Microsoft ACPI Kernel                    
Dfsc         Драйвер клиента простр File System
AcpiDev      Драйвер устройств с AC Kernel                              
""".split('\n')
    assert p.filter(data) == ['Dfsc         Драйвер клиента простр File System']


def test_filter_name():
    data = """
Модуль       Название               Тип драйвера  Дата ссылки           
============ ====================== ============= ======================
1394ohci     1394 OHCI-совместимый  Kernel                              
fstest       File System            Kernel        19.05.2015 1:28:03                     
    """.split('\n')
    assert p.filter(data) == []


def test_name():
    data = """
Модуль       Название               Тип драйвера  Дата ссылки           
============ ====================== ============= ======================
1394ohci     1394 OHCI-совместимый  File System                         
3ware        3ware                  Kernel        19.05.2015 1:28:03    
ACPI         Драйвер Microsoft ACPI File System               
Dfsc         Драйвер клиента простр File System
AcpiDev      Драйвер устройств с AC Kernel                              
""".split('\n')
    assert p.names(p.filter(data)) == ['1394ohci', 'ACPI', 'Dfsc']