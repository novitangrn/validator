from synop_functions import *
import pandas as pd

def input_sandi(parts):
    section1_list = []
    section2_list = []
    section3_list = []
    try:
        index_1 = parts.index('96935')  # Mencari indeks sandi pertama '96935'
        index_2 = parts.index('333')  # Mencari indeks sandi kedua '333'
    except ValueError:
        raise ValueError("Masukkan input sandi synop yang valid")

    section1_list = parts[:index_1+1] 
    section2_list = parts[index_1 + 1:index_2]  
    section3_list = parts[index_2:]  

    return section1_list, section2_list, section3_list

def section_0(functions, parts):
    outputs = []
    function0_left = functions.copy()
    unprocessed_parts = parts[:]

    for part in parts[:3]:
        # Heading sandi
        if any(char in ["S", "M", "I", "D"] for char in list(part)):
          if heading1 in function0_left and part in unprocessed_parts:
            output = heading1(part)
            outputs.insert(functions.index(heading1)+1, output)
            function0_left.remove(heading1)
            #processed_functions.add(heading1)
            unprocessed_parts.remove(part)
        # Location
        if any(char in ["W", "R"] for char in list(part)):
          output = location(part)
          outputs.insert(functions.index(location)+1, output)
          function0_left.remove(location)
          #processed_functions.add(location)
          unprocessed_parts.remove(part)
        # Time
        if part.isdigit() and len(part) == 6:
          output = time(part)
          outputs.insert(functions.index(time)+1, output)
          function0_left.remove(time)
          #processed_functions.add(time)
          unprocessed_parts.remove(part)

    for part in parts[2:]:
        # Mi-Mi-Mj-Mj
        if any(char in ["A", "X"] for char in list(part)):
          output = synop(part)
          outputs.insert(functions.index(synop)+1, output)
          function0_left.remove(synop)
          #processed_functions.add(synop)
          unprocessed_parts.remove(part)
        # Y-Y-G-G-Iw
        if any(char in ["0", "1", "3", "4"] for char in list(part)[-1]) and len(part) == 5:
          output = anemo_time(part)
          outputs.insert(functions.index(anemo_time)+1, output)
          function0_left.remove(anemo_time)
          #processed_functions.add(anemo_time)
          unprocessed_parts.remove(part)
        # I-I-i-i-i
        if any(substring in part for substring in ["96", "69", "93", "35"]):
          output = sandi_stamet(part)
          outputs.insert(functions.index(sandi_stamet)+1, output)
          function0_left.remove(sandi_stamet)
          #processed_functions.add(sandi_stamet)
          unprocessed_parts.remove(part)

    for func in function0_left:
      out = func("")
      output = [out[0], "", "Sandi harus diisi"]
      outputs.insert(functions.index(func), output)

    return outputs

def section_1_00UTC(functions, parts):
    outputs = []
    function1_left = functions.copy()
    required_func = [sandi_hujan, wind, temp, dew_point, qfe, qff, pressure, clouds]
    parts1 = parts.copy()
    unprocessed_parts = []

    function_mapping_seksi1 = {
        '1': temp,
        '2': dew_point,
        '3': qfe,
        '4': qff,
        '5': pressure,
        '6': rain_24,
        '7': weather_con,
        '8': clouds,
        #'9': time_10m
    }

    processed_parts = set()  # Membuat set untuk menyimpan parts yang sudah dijalankan

    if not parts1[2].startswith("00"):
        for i in range(2):
            try:
                output = functions[i](parts1[0])
                outputs.append(output)
                processed_parts.add(parts1[0])  # Tandai parts yang sudah dijalankan
                function1_left.remove(functions[i])  # Hapus fungsi yang sudah dijalankan dari daftar fungsi wajib yang belum dijalankan
                parts1.remove(parts1[0])
            except Exception as e:
                # outputs.append(str(e))
                unprocessed_parts.append(parts1[0])
    else:
        for i in range(3):
            try:
                output = functions[i](parts1[0])
                outputs.append(output)
                processed_parts.add(parts1[0])  # Tandai parts yang sudah dijalankan
                function1_left.remove(functions[i])  # Hapus fungsi yang sudah dijalankan dari daftar fungsi wajib yang belum dijalankan
                parts1.remove(parts1[0])
            except Exception as e:
                # outputs.append(str(e))
                unprocessed_parts.append(parts1[0])

    if parts1[0][0] != '0':
        for part in parts1:
            try:
                if part in processed_parts:  # Periksa apakah part sudah dijalankan sebelumnya
                    outputs.append(f"Part '{part}' sudah dijalankan sebelumnya.")
                else:
                    key = part[0]
                    if key in function_mapping_seksi1:
                        function = function_mapping_seksi1[key]
                        output = function(part)
                        outputs.append(output)
                        processed_parts.add(part)  # Tandai part yang sudah dijalankan
                        function1_left.remove(function)  # Hapus fungsi yang sudah dijalankan dari daftar fungsi wajib yang belum dijalankan
                    else:
                        raise ValueError(f"Tidak ada fungsi yang sesuai untuk karakter pertama '{key}'.")
            except Exception as e:
                # outputs.append(str(e))
                unprocessed_parts.append(part)
    else:
        unprocessed_parts = parts1
        outputs.append("Posisi sandi pada seksi 1 tidak sesuai. Mohon perhatikan karakter pertama sandi sebagai pengenal.")

    # Menambahkan validasi untuk fungsi wajib yang belum dijalankan
    for function in function1_left:
        if function in required_func:
            try:
                output = function("")
                index = required_func.index(function)
                output = [output[0], "", "Sandi harus dituliskan"]
                outputs.insert(index, output)
            except Exception as e:
                outputs.append(str(e))

    return outputs

def section_3_00UTC(functions, parts):
    # section 3 with 1 digit key
    function_mapping_seksi3 = {
        '3': seksi_3,
        '1': max_temp,
        '2': min_temp,
        '5': evaporation,
        '6': rain_3hours,
        #'8': cloud_1
    }
    # section 3 with 2 digit key
    additional_function_mapping = {
        '55': sun_radiation,
        '56': cloud_direction,
        '57': convective_clouds,
        '58': pressure_changes,
        '80': convective_1
    }

    required_func = [seksi_3, min_temp, evaporation, sun_radiation, cloud_direction, pressure_changes]

    processed_functions = set()
    unprocessed_parts = parts[:]  # Menyimpan semua bagian yang belum diproses
    outputs = []

    output_mapping = {}  # Menyimpan output fungsi sesuai dengan urutan section_3
    for section in parts:
        output_mapping[section] = None

    # Fungsi-fungsi dari function_mapping_seksi3
    for part in unprocessed_parts[:]:
        try:
            if part[0] in function_mapping_seksi3:
                function = function_mapping_seksi3[part[0]]
                if function not in processed_functions:
                    output = function(part)
                    output_mapping[part] = output
                    processed_functions.add(function)
                    unprocessed_parts.remove(part)
        except Exception as e:
            outputs.append(str(e))
            unprocessed_parts.remove(part)

    # Fungsi-fungsi dari additional_function_mapping
    for part in unprocessed_parts[:]:
        try:
            if part[:2] in additional_function_mapping:
                function = additional_function_mapping[part[:2]]
                if function not in processed_functions:
                    output = function(part)
                    output_mapping[part] = output
                    processed_functions.add(function)
                    unprocessed_parts.remove(part)
        except Exception as e:
            outputs.append(str(e))
            unprocessed_parts.remove(part)

    # Menambahkan output fungsi ke outputs sesuai dengan urutan section_3
    for section in parts:
        outputs.append(output_mapping[section])

    i = 0
    if unprocessed_parts:
        cs3 = cloud_section3(unprocessed_parts)
        if cs3 is not None:
            for i, val in enumerate(reversed(cs3)):
                outputs.insert(-(i+2), val)
    else:
        cs3 = None
    if cs3 is None:
        pass

    # Menambahkan validasi untuk fungsi wajib yang belum dijalankan
    for function in required_func:
        if function not in processed_functions:
            try:
                output = function("")
                index = required_func.index(function)
                output = [output[0], "", "Sandi harus dituliskan"]
                outputs.insert(index, output)
            except Exception as e:
                outputs.append(str(e))

    outputs = list(filter(lambda x: x is not None, outputs))
    return outputs

def create_dataframe(output):
    pd.set_option('display.max_colwidth', None)
    df = pd.DataFrame(output, columns=['Nama Fungsi', 'Input', 'Output'])
    return df

def main_00UTC(synop_code):

    # prepare functions
    functions = [heading1, location, time, synop, anemo_time, sandi_stamet,
                sandi_hujan, wind, temp, dew_point, qfe, qff, pressure, rain_24, weather_con, clouds,
                seksi_3, max_temp, min_temp, evaporation, sun_radiation, cloud_direction, convective_clouds,
                pressure_changes, rain_3hours, cloud_1, cloud_2, cloud_3, convective_1, isobar]


    function_seksi_0 = [heading1, location, time, synop, anemo_time, sandi_stamet]
    function_seksi_1 = [sandi_hujan, wind, wind_2, temp, dew_point, qfe, qff, isobar, pressure, rain_24, weather_con, clouds]
    function_seksi_3 = [seksi_3, max_temp, min_temp, evaporation, sun_radiation, cloud_direction, convective_clouds,
                        pressure_changes, rain_3hours, cloud_1, cloud_2, cloud_3, convective_1]


    # prepare input sandi
    synop_code = str(synop_code)
    parts = synop_code.split()
    first_list, second_list, third_list = input_sandi(parts)

    # process functions
    processed_functions = set()
    unprocessed_parts = parts[:]
    results_seksi_0 = section_0(function_seksi_0, first_list)
    results_seksi_1 = section_1_00UTC(function_seksi_1, second_list)
    results_seksi_3 = section_3_00UTC(function_seksi_3, third_list)

    # create dataframe
    #df = pd.concat([create_dataframe(results_seksi_0),
                    #create_dataframe(results_seksi_1),
                    #create_dataframe(results_seksi_3)], ignore_index=True)

    # create data frames
    df_seksi_0 = create_dataframe(results_seksi_0)
    df_seksi_1 = create_dataframe(results_seksi_1)
    df_seksi_3 = create_dataframe(results_seksi_3)

    return df_seksi_0, df_seksi_1, df_seksi_3
