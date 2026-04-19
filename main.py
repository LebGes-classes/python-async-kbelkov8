import asyncio
import time
from asinc import(
    Excel_read,
)


async def run(name1, name2, name3, name4, name5, name6, name7, name8, name9, name10):
    """Функция запуска программы.

    Args:
        names: названия файлов.
    """

    try:
        file_1 = Excel_read(name1)
        file_2 = Excel_read(name2)
        file_3 = Excel_read(name3)
        file_4 = Excel_read(name4)
        file_5 = Excel_read(name5)
        file_6 = Excel_read(name6)
        file_7 = Excel_read(name7)
        file_8 = Excel_read(name8)
        file_9 = Excel_read(name9)
        file_10 = Excel_read(name10)
    except FileNotFoundError:
        print('Данный файл не найден\n')
    else:
        await asyncio.gather(
            file_1.new_master_table(),
            file_2.new_master_table(),
            file_3.new_master_table(),
            file_4.new_master_table(),
            file_5.new_master_table(),
            file_6.new_master_table(),
            file_7.new_master_table(),
            file_8.new_master_table(),
            file_9.new_master_table(),
            file_10.new_master_table()
        )
        print(
            f'файл 1\n {file_1.calibration_report()}\n'
            f'файл 2\n {file_2.calibration_report()}\n'
            f'файл 3\n {file_3.calibration_report()}\n'
            f'файл 4\n {file_4.calibration_report()}\n'
            f'файл 5\n {file_5.calibration_report()}\n'
            f'файл 6\n {file_6.calibration_report()}\n'
            f'файл 7\n {file_7.calibration_report()}\n'
            f'файл 8\n {file_8.calibration_report()}\n'
            f'файл 9\n {file_9.calibration_report()}\n'
            f'файл 10\n {file_10.calibration_report()}\n'
            )

file_name1 = "medical_diagnostic_devices_1"
file_name2 = "medical_diagnostic_devices_2"
file_name3 = "medical_diagnostic_devices_3"
file_name4 = "medical_diagnostic_devices_4"
file_name5 = "medical_diagnostic_devices_5"
file_name6 = "medical_diagnostic_devices_6"
file_name7 = "medical_diagnostic_devices_7"
file_name8 = "medical_diagnostic_devices_8"
file_name9 = "medical_diagnostic_devices_9"
file_name10 = "medical_diagnostic_devices_10"


start_time = time.perf_counter()    # время начала программы

asyncio.run(run(
    file_name1,
    file_name2,
    file_name3,
    file_name4,
    file_name5,
    file_name6,
    file_name7,
    file_name8,
    file_name9,
    file_name10
))

end_time = time.perf_counter()    # время конца программы

print(f'Время работы программы: {(end_time - start_time):.4f}')