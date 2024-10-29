from APP.config.dotenvfile import GetEnv

# from APP.config.util import Get_time_now

from APP.config.utility.util import Get_time_now


def LogProses(data: str, forcePrint=False):
    try:
        current_time = Get_time_now("%H:%M:%S.%f")
        LogName = Get_time_now("%Y-%m-%d")
        content_data = f"{current_time}: {data}\n"

        # print log ke console
        if GetEnv("Log_print", "False").str() == "True" or forcePrint:
            print(content_data)

        try:
            with open(f"log/{LogName}.log", mode="a") as file:
                file.write(content_data)

        except Exception as e:
            print(f"gagal menyimpan Log. isi LOG:\n{data}")

    except Exception as e:
        print(f"Error writing to log: {e}")
