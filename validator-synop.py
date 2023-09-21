import streamlit as st
import pandas as pd

output_list = []

def heading1(head):
    head = str(head)
    if len(head) == 6:
      if head == "SMID53":
        return ["Heading", head, ""]
      else:
        return ["Heading", head, "Heading sandi tidak sesuai. Masukkan 'SMID53'"]
    else:
      return ["Heading", head, "Masukkan kode 6 karakter"]

def location(loc):
    loc = str(loc)
    if len(loc) == 4:
      if loc == "WARR":
        return ["Sandi Lokasi", loc, ""]
      else:
        return ["Sandi Lokasi", loc, "Sandi lokasi tidak sesuai. Masukkan 'WARR'"]
    else:
      return ["Sandi Lokasi", loc, "Masukkan kode 4 karakter"]

def time(times):
    error_messages = []  # Daftar untuk menyimpan pesan kesalahan

    if len(times) == 6:
        date = int(times[0:2])
        hour = int(times[2:4])
        minute = int(times[4:6])

        if not (0 <= date <= 31):
          error_messages.append(f"Bagian tanggal (date) di luar range 01-31.")
        if not (0 <= hour <= 24):
          error_messages.append(f"Bagian jam (hour) tidak sesuai.")
        if not (0 <= minute < 60):
          error_messages.append(f"Bagian menit (minute) tidak sesuai.")

    if not error_messages:
        if len(times) == 6:
            return ["time", times, ""]
        else:
            error_messages.append("Sandi tidak sesuai.")

    return ["time", times, ", ".join(error_messages)]

def synop(synop_sign):
    synop_sign = str(synop_sign)
    if len(synop_sign) == 4:
      if synop_sign == "AAXX":
        return ["Synop", synop_sign, ""]
      else:
        return ["Synop", synop_sign, "Sandi synop tidak sesuai. Masukkan 'AAXX'"]
    else:
      return ["Synop", synop_sign, "Masukkan kode 4 karakter"]

def anemo_time(an_time):
    error_messages = []  # Daftar untuk menyimpan pesan kesalahan

    if len(str(an_time)) == 5:
        YY = int(an_time[0:2])
        GG = int(an_time[2:4])
        Iw = int(an_time[4])

        if not (0 <= YY <= 31):
            error_messages.append(f"Bagian tanggal (YY) tidak sesuai. (input: {YY})")
        if not (0 <= GG <= 24):
            error_messages.append(f"Bagian jam (GG) tidak sesuai. (input: {GG})")
        if Iw not in [1, 2, 3, 4]:
            error_messages.append(f"Bagian cuaca (Iw) tidak sesuai. (input: {Iw})")
    else:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{an_time}' (Panjang: {len(an_time)}), Panjang sandi harus 5 karakter")

    if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai input
        return ["anemo_time", an_time, ""]

    return ["anemo_time", an_time, ", ".join(error_messages)]  # Kembalikan list output dengan pesan kesalahan dalam satu kolom

def sandi_stamet(IIiii):
    IIiii = str(IIiii)
    error_messages = []  # Daftar untuk menyimpan pesan kesalahan
    correct_sandi = '96935'

    if len(IIiii) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{IIiii}' (Panjang: {len(IIiii)}), Panjang sandi harus 5 karakter")

    if IIiii == correct_sandi:
        return ["sandi_stamet", IIiii, ""]
    else:
        mismatch_indices = [i for i, (char_input, char_correct) in enumerate(zip(IIiii, correct_sandi)) if char_input != char_correct]

        if mismatch_indices:
            error_msg = "Sandi Juanda yang benar adalah: "
            for i, char in enumerate(correct_sandi):
                if i in mismatch_indices:
                    error_msg += f"[{char}]"
                else:
                    error_msg += char
            error_msg += f". (input: {IIiii})"
            error_messages.append(error_msg)
        else:
            error_messages.append("Sandi Juanda yang benar adalah: 96935")

    if error_messages:
        return ["sandi_stamet", IIiii, ", ".join(error_messages)]

    return ["sandi_stamet", IIiii, "Sandi stamet tidak sesuai."]


def sandi_hujan(pengenal_hujan):
    pengenal_hujan = str(pengenal_hujan)
    error_messages = []

    if len(pengenal_hujan) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{pengenal_hujan}' (Panjang: {len(pengenal_hujan)}), Panjang sandi harus 5 karakter")

    if len(pengenal_hujan) == 5:
        Ir = int(pengenal_hujan[0])  # data curah hujan
        Ix = int(pengenal_hujan[1])  # macam operasi stasiun
        h = pengenal_hujan[2]  # tinggi dasar awan terendah
        VV = int(pengenal_hujan[3:])  # pengelihatan mendatar

        # Cek kesesuaian karakter
        if not Ir in [0, 1, 2, 3, 4]:
            error_messages.append(f"Pengenal hujan (IR) tidak sesuai. Masukkan nilai 0-4. Input: '{Ir}'")
        if not Ix in [1, 2, 3, 4, 5, 6]:
            error_messages.append(f"Pengenal operasi stasiun (IX) tidak sesuai. Masukkan nilai antara 1-6. Input: '{Ix}'")
        if not h in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/']:
            error_messages.append(f"Tinggi dasar awan terendah (h) tidak sesuai. Masukkan nilai antara 0-9 atau '/'. Input: '{h}'")
        if not (0 <= VV <= 99) and not (51 <= VV <= 55):
            error_messages.append(f"Pengelihatan mendatar (VV) tidak sesuai. Masukkan nilai antara 00-99. Input: '{VV}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai integer
            return ["Pengenal Hujan", int(pengenal_hujan), ""]

    if error_messages:
        return ["Pengenal Hujan", pengenal_hujan, ", ".join(error_messages)]

    return ["Pengenal Hujan", pengenal_hujan, "Pengenal hujan tidak sesuai."]

def wind(wind_code):
    wind_code = str(wind_code)
    error_messages = []

    if len(wind_code) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{wind_code}' (Panjang: {len(wind_code)}), Panjang sandi harus 5 karakter")

    if len(wind_code) == 5:
        N = wind_code[0]  # data tutupan awan
        dd = int(wind_code[1:3])  # arah angin
        ff = int(wind_code[3:])  # kecepatan angin

        # Cek kesesuaian karakter
        if not N in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/']:
            error_messages.append(f"Tinggi dasar awan terendah (h) tidak sesuai. Masukkan nilai antara 0-9 atau '/'. Input: '{N}'")
        if not (0 <= dd <= 36):
            error_messages.append(f"Arah angin (dd) tidak sesuai. Masukkan nilai antara 00-36. Input: '{dd}'")
        if not (0 <= ff <= 99):
            error_messages.append(f"Kecepatan angin (ff) tidak sesuai. Masukkan nilai antara 00-99. Input: '{ff}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai yang sesuai
            return ["Pengenal Angin Seksi 1", wind_code, ""]

    if error_messages:
        return ["Pengenal Angin Seksi 1", wind_code, ", ".join(error_messages)]

    return ["Pengenal Angin Seksi 1", wind_code, "Pengenal angin seksi 1 tidak sesuai."]

def wind_2(wind_code):
    wind_code = str(wind_code)
    error_messages = []

    if len(wind_code) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{wind_code}' (Panjang: {len(wind_code)}), Panjang sandi harus 5 karakter")

    if len(wind_code) == 5:
        wind_coder = wind_code[:2]  # kode angin >99 knot
        ff = int(wind_code[2:])  # kecepatan angin

        # Cek kesesuaian karakter
        if wind_coder != "00":
            error_messages.append(f"Kode angin >99 knot tidak sesuai. Masukkan nilai '00'. Input: '{wind_coder}'")
        if not ff > 99:
            error_messages.append(f"Kecepatan angin (ff) tidak sesuai. Masukkan nilai di atas 099. Input: '{ff}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai yang sesuai
            return ["Pengenal Angin Tambahan Seksi 1", wind_code, ""]

    if error_messages:
        return ["Pengenal Angin Tambahan Seksi 1", wind_code, ", ".join(error_messages)]

    return ["Pengenal Angin Tambahan Seksi 1", wind_code, "Pengenal angin tambahan seksi 1 tidak sesuai."]

# 1SnTTT
def temp(temp_val):
    temp_val = str(temp_val)
    error_messages = []

    if len(temp_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{temp_val}' (Panjang: {len(temp_val)}), Panjang sandi harus 5 karakter")

    if len(temp_val) == 5:
        temp_code = int(temp_val[0])  # data curah hujan
        Sn = int(temp_val[1])  # macam operasi stasiun
        TTT = int(temp_val[2:])  # tinggi dasar awan terendah

        # Cek kesesuaian karakter
        if not temp_code == 1:
            error_messages.append(f"Pengenal sandi suhu tidak sesuai. Masukkan nilai 1. Input: '{temp_code}'")
        if not Sn in [0, 1]:
            error_messages.append(f"Pengenal Sn tidak sesuai. Masukkan nilai 0 atau 1. Input: '{Sn}'")
        if not (0 <= TTT <= 999):
            error_messages.append(f"Nilai suhu udara tidak valid. Masukkan nilai antara 000-999. Input: '{TTT}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai integer
            return ["Sandi Suhu", int(temp_val), ""]

    if error_messages:
        return ["Sandi Suhu", temp_val, ", ".join(error_messages)]

    return ["Sandi Suhu", temp_val, "Pengenal hujan tidak sesuai."]

# 2SnTTT or 29UUU

def dew_point(dp_val):
    dp_val = str(dp_val)
    error_messages = []

    if len(dp_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{dp_val}' (Panjang: {len(dp_val)}), Panjang sandi harus 5 karakter")

    if len(dp_val) == 5:
      if dp_val[1] != "9":
        dp_code = int(dp_val[0])
        Sn = int(dp_val[1])
        Td = int(dp_val[2:])

        # Cek kesesuaian karakter
        if not dp_code == 2:
            error_messages.append(f"Pengenal sandi titik embun tidak sesuai. Masukkan nilai 2. Input: '{dp_code}'")
        if not Sn in [0, 1]:
            error_messages.append(f"Pengenal Sn tidak sesuai. Masukkan nilai 0 atau 1. Input: '{Sn}'")
        if not (000 <= Td <= 700): # threshold dew point
            error_messages.append(f"Nilai titik embun tidak valid. Masukkan nilai antara 000-999. Input: '{Td}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai dalam bentuk list
            return ["Sandi Titik Embun", int(dp_val), ""]

      else:
        rh_code = int(dp_val[:2])
        U = int(dp_val[2:])

        # Cek kesesuaian karakter
        if not rh_code == 29:
            error_messages.append(f"Pengenal sandi kelembaban nisbi tidak sesuai. Masukkan nilai 29. Input: '{rh_code}'")
        if not (000 <= U <= 100): # threshold RH
            error_messages.append(f"Nilai kelembaban nisbi tidak valid. Masukkan nilai antara 000-100. Input: '{U}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai dalam bentuk list
            return ["Sandi Kelembaban Nisbi", int(dp_val), ""]

    if error_messages:
        return ["Sandi Titik Embun/Kelembaban Nisbi", dp_val, ", ".join(error_messages)]

    return ["Sandi Titik Embun", dp_val, "Sandi titik embun tidak sesuai."]

# 3P0P0P0P0

def qfe(qfe_val):
    qfe_val = str(qfe_val)
    error_messages = []

    if len(qfe_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{qfe_val}' (Panjang: {len(qfe_val)}), Panjang sandi harus 5 karakter")

    if len(qfe_val) == 5:
        qfe_code = int(qfe_val[0])  # sandi pengenal QFE
        P0 = int(qfe_val[1:])  # besar tekanan dalam persepuluhan milibar

        # Cek kesesuaian karakter
        if not qfe_code == 3:
            error_messages.append(f"Pengenal sandi QFE tidak sesuai. Masukkan nilai 3. Input: '{qfe_code}'")
        if not (0000 <= P0 <= 9999):  # threshold dew point
            error_messages.append(f"Nilai QFE tidak valid. Masukkan nilai antara 0000-9999. Input: '{P0}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai dalam bentuk list
            return ["Sandi QFE", int(qfe_val), ""]

    if error_messages:
        return ["Sandi QFE", qfe_val, ", ".join(error_messages)]

    return ["Sandi QFE", qfe_val, "Sandi QFE tidak sesuai."]

# 4PPPP

def qff(qff_val):
    qff_val = str(qff_val)
    error_messages = []

    if len(qff_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{qff_val}' (Panjang: {len(qff_val)}), Panjang sandi harus 5 karakter")

    if len(qff_val) == 5:
      if qff_val[1] not in ["1", "8", "7", "5"]:
        qff_code = int(qff_val[0])  # sandi pengenal QFE
        P = int(qff_val[1:])  # besar tekanan dalam persepuluhan milibar

        # Cek kesesuaian karakter
        if not qff_code == 4:
            error_messages.append(f"Pengenal sandi QFE tidak sesuai. Masukkan nilai 4. Input: '{qff_code}'")
        if not (0000 <= P <= 9999):  # threshold dew point
            error_messages.append(f"Nilai QFE tidak valid. Masukkan nilai antara 0000-9999. Input: '{P}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai dalam bentuk list
            return ["Sandi QFF", int(qff_val), ""]

      else:
        height_code = int(qff_val[0])  # sandi pengenal tinggi permukaan bumi
        a3 = qff_val[1]  # indikator permukaan isobarik
        h = int(qff_val[2:])

        # Cek kesesuaian karakter
        if not height_code == 4:
            error_messages.append(f"Pengenal sandi tinggi permukaan bumi tidak sesuai. Masukkan nilai 4. Input: '{height_code}'")
        if a3 not in ["1", "8", "7", "5"]:  # threshold dew point
            error_messages.append(f"Nilai a3 tidak valid. Masukkan nilai antara 1, 8, 7, atau 5. Input: '{a3}'")
        if not (000 <= h <= 999):  # threshold height
            error_messages.append(f"Nilai tinggi tidak valid. Masukkan nilai antara 0000-9999. Input: '{P}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai dalam bentuk list
            return ["Sandi QFF", int(qff_val), ""]

    if error_messages:
        return ["sandi Tinggi Permukaan Bumi", qff_val, ", ".join(error_messages)]

    return ["Sandi QFF/sandi Tinggi Permukaan Bumi", qff_val, "Sandi QFF/sandi Tinggi Permukaan Bumi tidak sesuai."]

# 4a3hhh

def isobar(isobar_var):
    isobar_val = str(isobar_var)
    error_messages = []

    if len(isobar_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{isobar_val}' (Panjang: {len(isobar_val)}), Panjang sandi harus 5 karakter")

    if len(isobar_val) == 5:
        isobar_code = int(isobar_val[0])  # sandi pengenal QFF
        hhh = int(isobar_val[1:])  # besar tekanan dalam persepuluhan milibar

        # Cek kesesuaian karakter
        if not isobar_code == 4:
            error_messages.append(f"Pengenal sandi isobar tidak sesuai. Masukkan nilai 4. Input: '{isobar_code}'")
        if not (0000 <= hhh <= 9999):  # threshold dew point
            error_messages.append(f"Nilai QFF tidak valid. Masukkan nilai antara 0000-9999. Input: '{hhh}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai dalam bentuk list
            return ["Sandi Isobar", int(isobar_val), ""]

    if error_messages:
        return ["Sandi Isobar", isobar_val, ", ".join(error_messages)]

    return ["Sandi Isobar", isobar_val, "Sandi Isobar tidak sesuai."]

def pressure(pres_val):
    pres_val = str(pres_val)
    error_messages = []

    if len(pres_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{pres_val}' (Panjang: {len(pres_val)}), Panjang sandi harus 5 karakter")

    if len(pres_val) == 5:
        pres_code = int(pres_val[0])  # sandi pengenal tekanan
        a = int(pres_val[1])
        p = int(pres_val[2:])  # besar perubahan tekanan dari 3 jam yang lalu

        # Cek kesesuaian karakter
        if not pres_code == 5:
            error_messages.append(f"Pengenal sandi tekanan tidak sesuai. Masukkan nilai 5. Input: '{pres_code}'")
        if not (0 <= a <= 8):  # sifat perubahan tekanan cuaca
            error_messages.append(f"Nilai pengenal perubahan tekanan udara tidak valid. Masukkan nilai antara 0-8. Input: '{a}'")
        if not (0 <= p <= 999):  # jumlah perubahan tekanna udar
            error_messages.append(f"Nilai QFE tidak valid. Masukkan nilai antara 000-999. Input: '{p}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai dalam bentuk list
            return ["Sandi Perubahan Tekanan Udara", pres_val, ""]

    if error_messages:
        return ["Sandi Perubahan Tekanan Udara", pres_val, ", ".join(error_messages)]

    return ["Sandi Perubahan Tekanan Udara", pres_val, "Sandi Perubahan Tekanan Udara tidak sesuai."]

# 6RRRtR

def rain_24(rain_val):
    rain_val = str(rain_val)
    error_messages = []

    if len(rain_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{rain_val}' (Panjang: {len(rain_val)}), Panjang sandi harus 6 karakter")

    if len(rain_val) == 5:
        rain_code = int(rain_val[0])  # sandi pengenal tekanan
        RRR = int(rain_val[1:4])  # jumlah curah hujan dalam 24 jam
        tR = int(rain_val[4])  # tipe curah hujan

        # Cek kesesuaian karakter
        if not rain_code == 6:
            error_messages.append(f"Pengenal sandi curah hujan tidak sesuai. Masukkan nilai 6. Input: '{rain_code}'")
        if not (000 <= RRR <= 999):  # jumlah curah hujan dalam 24 jam
            error_messages.append(f"Nilai curah hujan dalam 24 jam tidak valid. Masukkan nilai antara 000-999. Input: '{RRR}'")
        if not (0 <= tR <= 9):  # selang waktu
            error_messages.append(f"Nilai selang waktu tidak valid. Masukkan nilai antara 0-9. Input: '{tR}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai dalam bentuk list
            return ["Sandi Curah Hujan 24 Jam", int(rain_val), ""]

    if error_messages:
        return ["Sandi Curah Hujan 24 Jam", rain_val, ", ".join(error_messages)]

    return ["Sandi Curah Hujan 24 Jam", rain_val, "Sandi Curah Hujan 24 Jam tidak sesuai."]

#7-w-w-W1-W2

def weather_con(weathercon_val):
    weathercon_val = str(weathercon_val)
    error_messages = []

    if len(weathercon_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{weathercon_val}' (Panjang: {len(weathercon_val)}), Panjang sandi harus 14 karakter")

    if len(weathercon_val) == 5:
        weather_code = weathercon_val[0]  # sandi pengenal cuaca
        ww = int(weathercon_val[1:3])  # keadaan cuaca pada waktu pengamatan 1
        W1 = int(weathercon_val[3])  # keadaan cuaca yang lalu 1
        W2 = int(weathercon_val[4])  # keadaan cuaca yang lalu 2

        # Cek kesesuaian karakter
        if not weather_code == "7":
            error_messages.append(f"Sandi pengenal cuaca tidak sesuai. Masukkan nilai '7'. Input: '{weather_code}'")
        if not (00 <= ww <= 99):
            error_messages.append(f"Sandi keadaan cuaca tidak valid. Masukkan nilai antara 00-99. Input: '{ww}'")
        if not (0 <= W1 <= 9):
            error_messages.append(f"Sandi W1 tidak valid. Masukkan nilai antara 0-9. Input: '{W1}'")
        if not (0 <= W2 <= 9) and not (W2 >= W1):
            error_messages.append(f"Sandi W2 tidak valid. Masukkan nilai antara 0-9. Input: '{W2}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai dalam bentuk list
            return ["Sandi Pengenal Cuaca", weathercon_val, ""]

    if error_messages:
        return ["Sandi Pengenal Cuaca", weathercon_val, ", ".join(error_messages)]

    return ["Sandi Pengenal Cuaca", weathercon_val, "Sandi Pengenal Cuaca tidak sesuai."]

#8-Nh-CL-CM-CH

def clouds(clouds_val):
    clouds_val = str(clouds_val)
    error_messages = []

    if len(clouds_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{clouds_val}' (Panjang: {len(clouds_val)}), Panjang sandi harus 14 karakter")

    if len(clouds_val) == 5:
        cloud_code = clouds_val[0]  # sandi pengenal awan
        Nh = clouds_val[1]  # besar tutupan awan
        CL = clouds_val[2]  # jenis awan CL
        CM = clouds_val[3]  # jenis awan CM
        CH = clouds_val[4]  # jens awan CH

        # Cek kesesuaian karakter
        if not cloud_code == "8":
            error_messages.append(f"Pengenal sandi awan tidak sesuai. Masukkan nilai '8'. Input: '{cloud_code}'")
        if not (Nh in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/']):
            error_messages.append(f"Besar tutupan awan tidak valid. Masukkan nilai antara 0-9. Input: '{Nh}'")
        if not (CL in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/']):
            error_messages.append(f"Kode awan jenis CL tidak valid. Masukkan nilai antara 0-9. Input: '{CL}'")
        if not (CM in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/']):
            error_messages.append(f"Kode awan jenis CM tidak valid. Masukkan nilai antara 0-9. Input: '{CM}'")
        if not (CH in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/']):
            error_messages.append(f"Kode awan jenis CH tidak valid. Masukkan nilai antara 0-9. Input: '{CH}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai dalam bentuk list
            return ["Sandi Awan", clouds_val, ""]

    if error_messages:
        return ["Sandi Awan", clouds_val, ", ".join(error_messages)]

    return ["Sandi Awan", clouds_val, "Sandi Awan tidak sesuai."]


def seksi_3(sec_val):
    expected_value = '333'
    error_messages = []  # Daftar untuk menyimpan pesan kesalahan

    if sec_val == expected_value:
        return ["Section 3", sec_val, ""]

    else:
        # Cek panjang string
        if len(sec_val) != len(expected_value):
            error_messages.append(f"Panjang string tidak sesuai. Input: '{sec_val}' (Panjang: {len(sec_val)}), Harusnya: '{expected_value}' (Panjang: {len(expected_value)})")
        else:
            # Cek kesalahan penulisan karakter
            differences = [f"Posisi {i+1}: '{sec_val[i]}' -> '{expected_value[i]}'" for i in range(len(sec_val)) if sec_val[i] != expected_value[i]]
            if differences:
                error_messages.append(f"Kesalahan penulisan karakter: {', '.join(differences)}")
            else:
                error_messages.append(f"Kode pengenal sandi tidak sesuai. Input: '{sec_val}', Harusnya: '{expected_value}'")

        if error_messages:
            return ["Section 3", sec_val, ", ".join(error_messages)]  # Menggabungkan pesan kesalahan menjadi satu string

        return None

# 00 UTC (2-Sn-Tn-Tn-Tn)

def min_temp(mintemp_val):
    mintemp_val = str(mintemp_val)
    error_messages = []  # Daftar untuk menyimpan pesan kesalahan

    if len(mintemp_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{mintemp_val}' (Panjang: {len(mintemp_val)}), Panjang sandi harus 5 karakter")

    if len(mintemp_val) == 5:
        min_temp_code = mintemp_val[0]
        Sn = mintemp_val[1]
        Tn = int(mintemp_val[2:])

        # Cek apakah karakter pertama adalah "2"
        if min_temp_code != "2":
            error_messages.append(f"Karakter pertama tidak sesuai. Input: '{min_temp_code}', Sandi pengenal: '2'")

        if Sn != "0":
            error_messages.append(f"Karakter kedua mungkin tidak sesuai. Input: '{Sn}', Harusnya: '0'")

        if not (0 <= Tn <= 499):  # Koreksi batasan angka suhu
            error_messages.append(f"Angka suhu mungkin tidak sesuai. Input: '{Tn}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai integer
            return ["Min Temp", mintemp_val, ""]

    if error_messages:
        return ["Min Temp", mintemp_val, ", ".join(error_messages)]  # Menggabungkan pesan kesalahan menjadi satu string

    return ["Min Temp", mintemp_val, "Suhu minimum tidak sesuai."]

# Only for 12.00 (1-Sn-Tx-Tx-Tx)

def max_temp(maxtemp_val):
    maxtemp_val = str(maxtemp_val)
    error_messages = []  # Daftar untuk menyimpan pesan kesalahan

    if len(maxtemp_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{maxtemp_val}' (Panjang: {len(maxtemp_val)}), Panjang sandi harus 5 karakter")

    if len(maxtemp_val) == 5:
        max_temp_code = maxtemp_val[0]
        Sn = maxtemp_val[1]
        Tx = int(maxtemp_val[2:])

        # Cek apakah karakter pertama adalah "1"
        if max_temp_code != "1":
            error_messages.append(f"Karakter pertama tidak sesuai. Input: '{max_temp_code}', Sandi pengenal: '1'")

        if Sn != "0":
            error_messages.append(f"Karakter kedua mungkin tidak sesuai. Input: '{Sn}', Harusnya: '0'")

        if not (0 <= Tx <= 499):  # Koreksi batasan angka suhu
            error_messages.append(f"Angka suhu mungkin tidak sesuai. Input: '{Tx}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai integer
            return ["Suhu maksimum", maxtemp_val, ""]

    if error_messages:
        return ["Suhu maksimum", maxtemp_val, ", ".join(error_messages)]  # Kembalikan daftar pesan kesalahan

    return "Suhu maksimum tidak sesuai."

# Only for 00.00

def evaporation(vapor_val):
    vapor_val = str(vapor_val)
    error_messages = []  # Daftar untuk menyimpan pesan kesalahan

    if len(vapor_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{vapor_val}' (Panjang: {len(vapor_val)}), Panjang sandi harus 5 karakter")

    if len(vapor_val) == 5:
        vapor_val_code = vapor_val[0]
        E = int(vapor_val[1:-1])
        Ie = vapor_val[-1]

        # Cek kesesuaian karakter
        if vapor_val_code != "5":
            error_messages.append(f"Karakter pertama tidak sesuai. Input: '{vapor_val_code}', Sandi pengenal: '5'")

        if not (0 <= E <= 999):  # Koreksi batasan angka suhu
            error_messages.append(f"Angka suhu mungkin tidak sesuai. Input: '{E}'")

        if Ie not in ["0", "1"]:
            error_messages.append(f"Pengenal panci penguapan mungkin tidak sesuai. Input: '{Ie}', Harusnya: '0' atau '1'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai integer
            return ["Evaporasi", vapor_val, ""]

    if error_messages:
        return ["Evaporasi", vapor_val, ", ".join(error_messages)]  # Kembalikan daftar pesan kesalahan

    return "Sandi evaporasi tidak sesuai."

# Only 00.00 UTC

def sun_radiation(sunrad_val):
    sunrad_val = str(sunrad_val)
    error_messages = []  # Daftar untuk menyimpan pesan kesalahan

    if len(sunrad_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{sunrad_val}' (Panjang: {len(sunrad_val)}), Panjang sandi harus 5 karakter")

    if len(sunrad_val) == 5:
        sunrad_val_code = sunrad_val[0:2]
        SSS = int(sunrad_val[2:])

        # Cek kesesuaian karakter
        if sunrad_val_code != "55":
            error_messages.append(f"Karakter pertama tidak sesuai. Input: '{sunrad_val_code}', Sandi pengenal: '55'")

        if not (0 <= SSS < 240):  # Koreksi batasan angka suhu
            error_messages.append(f"Angka suhu mungkin tidak sesuai, melebihi 24 jam. Input: '{SSS}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai integer
            return ["Radiasi Matahari", sunrad_val, ""]

    if error_messages:
        return ["Radiasi Matahari", sunrad_val, ", ". join(error_messages)]  # Kembalikan daftar pesan kesalahan

    return "Sandi radiasi matahari tidak sesuai."

def cloud_direction(cloud_direction_val):
    cloud_direction_val = str(cloud_direction_val)
    error_messages = []  # Daftar untuk menyimpan pesan kesalahan

    if len(cloud_direction_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{cloud_direction_val}' (Panjang: {len(cloud_direction_val)}), Panjang sandi harus 5 karakter")

    if len(cloud_direction_val) == 5:
        cloud_val_code = cloud_direction_val[0:2]
        Dl = int(cloud_direction_val[2])
        Dm = int(cloud_direction_val[3])
        Dh = int(cloud_direction_val[4])

        # Cek kesesuaian karakter
        if cloud_val_code != "56":
            error_messages.append(f"Karakter pertama tidak sesuai. Input: '{cloud_val_code}', Sandi pengenal: '56'")

        if not (0 <= Dl <= 8):
            error_messages.append(f"Sandi arah awan rendah mungkin tidak sesuai. Masukkan nilai antara 0-8. Input: '{Dl}'")
        if not (0 <= Dm <= 8):
            error_messages.append(f"Sandi arah awan menengah mungkin tidak sesuai. Masukkan nilai antara 0-8. Input: '{Dm}'")
        if not (0 <= Dh <= 8):
            error_messages.append(f"Sandi arah awan tinggi mungkin tidak sesuai. Masukkan nilai antara 0-8. Input: '{Dh}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai integer
            return ["Arah awan", cloud_direction_val, ""]

    if error_messages:
        return ["Arah awan", cloud_direction_val, ", ".join(error_messages)]  # Kembalikan daftar pesan kesalahan

    return "Sandi arah awan tidak sesuai."

# Grup ini dilaporkan hanya saat terdapat awan konvektif saja seperti Cumulus congestu atau towering Cumulus (sandi 2 atau 8), cumulunimbus (sandi 3 atau 9).
# 57-C-D-e

def convective_clouds(convective_clouds_val):
    convective_clouds_val = str(convective_clouds_val)
    error_messages = []  # Daftar untuk menyimpan pesan kesalahan

    if len(convective_clouds_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{convective_clouds_val}' (Panjang: {len(convective_clouds_val)}), Panjang sandi harus 5 karakter")

    if len(convective_clouds_val) == 5:
        cloud_val_code = convective_clouds_val[0:2]
        C = int(convective_clouds_val[2]) # Jenis awan
        Da = int(convective_clouds_val[3]) # Arah awan
        ec = int(convective_clouds_val[4]) # Sudut elevasi

        # Cek kesesuaian karakter
        if cloud_val_code != "57":
            error_messages.append(f"Karakter pertama tidak sesuai. Input: '{cloud_val_code}', Sandi pengenal: '56'")

        if not C in [8, 9]:
            error_messages.append(f"Sandi awan tidak sesuai. Masukkan nilai 8 atau 9. Input: '{C}'")
        if not (0 <= Da <= 8):
            error_messages.append(f"Sandi arah awan konvektif tidak sesuai. Masukkan nilai antara 0-8. Input: '{Da}'")
        if not (0 <= ec <= 9):
            error_messages.append(f"Sandi sudut awan konvektif mungkin tidak sesuai. Masukkan nilai antara 0-9. Input: '{ec}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai integer
            return ["Awan konvektif.", convective_clouds_val, ""]

    if error_messages:
        return ["Awan konvektif.", convective_clouds_val, ", ".join(error_messages)]  # Kembalikan daftar pesan kesalahan

    return "Sandi awan konvektif tidak sesuai."

# 58PPP / 59PPP
def pressure_changes(pressure_changes_val):
    pressure_changes_val = str(pressure_changes_val)
    error_messages = []  # Daftar untuk menyimpan pesan kesalahan

    if len(pressure_changes_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{pressure_changes_val}' (Panjang: {len(pressure_changes_val)}), Panjang sandi harus 5 karakter")

    if len(pressure_changes_val) == 5:
        pressure_changes_code = pressure_changes_val[0:2]
        P = int(pressure_changes_val[2:])

        # Cek kesesuaian karakter
        if not pressure_changes_code in ["58", "59"]:
            error_messages.append(f"Sandi perbedaan tekanan tidak sesuai. Masukkan nilai 58 atau 59. Input: '{pressure_changes_code}'")
        if not (0 <= P <= P):
            error_messages.append(f"Sandi arah awan konvektif tidak sesuai. Masukkan nilai antara 0-8. Input: '{P}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai integer
            return ["Perubahan Tekanan.", pressure_changes_val, ""]

    if error_messages:
        return ["Perubahan Tekanan.", pressure_changes_val, ", ".join(error_messages)]  # Kembalikan daftar pesan kesalahan

    return "Sandi perubahan tekanan tidak sesuai."

def rain_3hours(rain_3hours_val):
    rain_3hours_val = str(rain_3hours_val)
    error_messages = []  # Daftar untuk menyimpan pesan kesalahan

    if len(rain_3hours_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{rain_3hours_val}' (Panjang: {len(rain_3hours_val)}), Panjang sandi harus 5 karakter")

    if len(rain_3hours_val) == 5:
        rain_3hours_code = rain_3hours_val[0]
        R = int(rain_3hours_val[1:4])
        Tr = rain_3hours_val[-1]

        # Cek kesesuaian karakter
        if rain_3hours_code != "6":
            error_messages.append(f"Sandi pengenal tidak sesuai. Input: '{rain_3hours_code}', Sandi pengenal seharusnya: '6'")
        if not (0 <= R <= 999):
            error_messages.append(f"Nilai hujan 3 jam mungkin tidak sesuai. Masukkan nilai antara 0-999. Input: '{R}'")
        if not (Tr == "7"):
            error_messages.append(f"Nilai Tr tidak sesuai. Input: '{Tr}'. Nilai Tr seharusnya: '7'.")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai integer
            return ["Hujan 3 jam", rain_3hours_val, ""]

    if error_messages:
        return ["Hujan 3 jam", rain_3hours_val, ", ".join(error_messages)]   # Kembalikan daftar pesan kesalahan

    return "Nilai hujan 3 jam tidak sesuai."

def cloud_1(cloud_1_val):
    cloud_1_val = str(cloud_1_val)
    error_messages = []  # Daftar untuk menyimpan pesan kesalahan

    if len(cloud_1_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{cloud_1_val}' (Panjang: {len(cloud_1_val)}), Panjang sandi harus 5 karakter")

    if len(cloud_1_val) == 5:
      cloud_1_code = cloud_1_val[0] # Kode pengenal kode awan sandi awan 1
      Ns = cloud_1_val[1]  # Ns: bagian langit yang tertutup oleh jenis awan tertentu
      C = int(cloud_1_val[2])   # C: Jenis Awan (sandi: 0-9)
      hs = int(cloud_1_val[3:]) # hs: Tinggi awan

      # Cek kesesuaian karakter
      if cloud_1_val[0] != '8':
          error_messages.append(f"Pengenal sandi awan tidak sesuai. Input: '{cloud_1_val[0]}', Harusnya: '8'")
      if not (Ns in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '/']):
          error_messages.append(f"Jumlah oktas Ns tidak sesuai. Masukkan nilai antara 0-8, 9, atau /. Input: '{Ns}'")
      if not (0 <= C <= 9):
          error_messages.append(f"Kode jenis awan (C) tidak sesuai. Masukkan nilai antara 0-9. Input: '{C}'")
      if not (0 <= hs <= 99):
          error_messages.append(f"Nilai tinggi awan (hs) tidak sesuai. Input: '{hs}'")

      if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai integer
          return ["Awan Lapisan Pertama.", cloud_1_val, ""]

    if error_messages:
        return ["Awan Lapisan Pertama.", cloud_1_val, ", ".join(error_messages)]  # Kembalikan daftar pesan kesalahan

    return "Sandi awan pertama tidak sesuai."

def cloud_2(cloud_2_val):
    cloud_2_val = str(cloud_2_val)
    error_messages = []  # Daftar untuk menyimpan pesan kesalahan

    if len(cloud_2_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{cloud_2_val}' (Panjang: {len(cloud_2_val)}), Panjang sandi harus 5 karakter")

    if len(cloud_2_val) == 5:
      cloud_2_code = cloud_2_val[0] # Kode pengenal kode awan sandi awan 2
      Ns = cloud_2_val[1]  # Ns: bagian langit yang tertutup oleh jenis awan tertentu
      C = int(cloud_2_val[2])   # C: Jenis Awan (sandi: 0-9)
      hs = int(cloud_2_val[3:]) # hs: Tinggi awan

      # Cek kesesuaian karakter
      if cloud_2_val[0] != '8':
          error_messages.append(f"Pengenal sandi awan tidak sesuai. Input: '{cloud_2_val[0]}', Harusnya: '8'")
      if not (Ns in ['3', '4', '5', '6', '7', '8', '9', '/']):
          error_messages.append(f"Jumlah oktas Ns lapisan kedua tidak sesuai. Masukkan nilai antara 3-8, 9, atau /. Input: '{Ns}'")
      if not (0 <= C <= 9):
          error_messages.append(f"Kode jenis awan (C) tidak sesuai. Masukkan nilai antara 0-9. Input: '{C}'")
      if not (0 <= hs <= 99):
          error_messages.append(f"Nilai tinggi awan (hs) tidak sesuai. Input: '{hs}'")

      if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai integer
          return ["Awan Lapisan Kedua", cloud_2_val, ""]

    if error_messages:
        return ["Awan Lapisan Kedua", cloud_2_val, ", ".join(error_messages)]  # Kembalikan daftar pesan kesalahan

    return "Sandi awan kedua tidak sesuai."

def cloud_3(cloud_3_val):
    cloud_3_val = str(cloud_3_val)
    error_messages = []  # Daftar untuk menyimpan pesan kesalahan

    if len(cloud_3_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{cloud_3_val}' (Panjang: {len(cloud_3_val)}), Panjang sandi harus 5 karakter")

    if len(cloud_3_val) == 5:
      cloud_3_code = cloud_3_val[0] # Kode pengenal kode awan sandi awan 3
      Ns = cloud_3_val[1]  # Ns: bagian langit yang tertutup oleh jenis awan tertentu
      C = int(cloud_3_val[2])   # C: Jenis Awan (sandi: 0-9)
      hs = int(cloud_3_val[3:]) # hs: Tinggi awan

      # Cek kesesuaian karakter
      if cloud_3_val[0] != '8':
          error_messages.append(f"Pengenal sandi awan tidak sesuai. Input: '{cloud_3_val[0]}', Harusnya: '8'")
      if not (Ns in ['5', '6', '7', '8', '9', '/']):
          error_messages.append(f"Jumlah oktas Ns lapisan ketiga tidak sesuai. Masukkan nilai antara 5-8, 9, atau /. Input: '{Ns}'")
      if not (0 <= C <= 9):
          error_messages.append(f"Kode jenis awan (C) tidak sesuai. Masukkan nilai antara 0-9. Input: '{C}'")
      if not (0 <= hs <= 99):
          error_messages.append(f"Nilai tinggi awan (hs) tidak sesuai. Input: '{hs}'")

      if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan nilai integer
          return ["Awan Lapisan Ketiga.", cloud_3_val, ""]

    if error_messages:
        return ["Awan Lapisan Ketiga.", cloud_3_val, ", ".join(error_messages)]  # Kembalikan daftar pesan kesalahan

    return "Sandi awan ketiga tidak sesuai."

# 8-N-C-h-h

def cloud_section3(values):
    cloud_list = []
    for value in values:
        if value[0] == ('8') and value[1] != '0':
          cloud_list.append(value)
    if len(cloud_list) == 4:
        return cloud_1(cloud_list[0]), cloud_1(cloud_list[1]), cloud_2(cloud_list[2]), cloud_3(cloud_list[3])
    elif len(cloud_list) == 3:
        return cloud_1(cloud_list[0]), cloud_2(cloud_list[1]), cloud_3(cloud_list[2])
    elif len(cloud_list) == 2:
        return cloud_1(cloud_list[0]), cloud_2(cloud_list[1])
    elif len(cloud_list) == 1:
        return [cloud_1(cloud_list[0])]

def convective_1(convective_3_val):
    convective_3_val = str(convective_3_val)
    error_messages = []  # Daftar untuk menyimpan pesan kesalahan

    if len(convective_3_val) != 5:
        error_messages.append(f"Panjang string tidak sesuai. Input: '{convective_3_val}' (Panjang: {len(convective_3_val)}), Panjang sandi harus 5 karakter")

    if len(convective_3_val) == 5:
        convective_3_code = convective_3_val[0:2]  # Kode pengenal sandi awan konvektif seksi 3
        C = int(convective_3_val[2])  # C: Jenis Awan (sandi: 0-9)
        hs = int(convective_3_val[3:])  # hs: Tinggi awan

        # Cek kesesuaian karakter
        if not (convective_3_code == "80"):
            error_messages.append("Awan konvektif harus jenis Cumulus (8) atau Cumulonimbus (9).")
        if not (C in ['8', '9']):
            error_messages.append(f"Kode jenis awan (C) tidak sesuai. Masukkan nilai antara 8-9. Input: '{C}'")
        if not (0 <= hs <= 99):
            error_messages.append(f"Nilai tinggi awan (hs) tidak sesuai. Input: '{hs}'")

        if not error_messages:  # Jika tidak ada pesan kesalahan, kembalikan sandi awan
            return ["Konvektif Seksi 3", convective_3_val, ""]

    if error_messages:
        return ["Konvektif Seksi 3", convective_3_val, ", ".join(error_messages)]  # Kembalikan daftar pesan kesalahan

    return "Sandi awan konvektif seksi 3 tidak sesuai."


# Daftar fungsi
functions = [heading1, location, time, synop, anemo_time, sandi_stamet,
             sandi_hujan, wind, temp, dew_point, qfe, qff, pressure, rain_24, weather_con, clouds,
             seksi_3, max_temp, min_temp, evaporation, sun_radiation, cloud_direction, convective_clouds,
             pressure_changes, rain_3hours, cloud_1, cloud_2, cloud_3, convective_1, isobar]


function_seksi_0 = [heading1, location, time, synop, anemo_time, sandi_stamet]
function_seksi_1 = [sandi_hujan, wind, wind_2, temp, dew_point, qfe, qff, isobar, pressure, rain_24, weather_con, clouds]
function_seksi_3 = [seksi_3, max_temp, min_temp, evaporation, sun_radiation, cloud_direction, convective_clouds,
                    pressure_changes, rain_3hours, cloud_1, cloud_2, cloud_3, convective_1]

def input_sandi(parts):
    section1_list = []
    section2_list = []
    section3_list = []
    index_1 = parts.index('96935') # Mencari indeks sandi pertama '96935'
    index_2 = parts.index('333') # Mencari indeks sandi kedua '333'
    section1_list = parts[:index_1+1] # Memasukkan bagian pertama ke first_list
    section2_list = parts[index_1 + 1:index_2] # Memasukkan bagian kedua ke second_list
    section3_list = parts[index_2:] # Memasukkan bagian ketiga ke third_list

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

    cs3 = cloud_section3(unprocessed_parts)
    for i, val in enumerate(cs3):
        outputs.insert(-(i+2), val)

    outputs = list(filter(lambda x: x is not None, outputs))

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

    cs3 = cloud_section3(unprocessed_parts)
    for i, val in enumerate(reversed(cs3)):
        outputs.insert(-(i+2), val)

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

import pandas as pd

def create_dataframe(output):
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

def main():
    st.title("Validator Synop Sederhana")
    #st.image('login2.png',use_column_width=True)
    
    # Dropdown untuk memilih jam
    selected_hour = st.selectbox("Pilih Jam", ["--Pilih Jam--", "00.00", "01.00", "02.00"])  # Tambahkan jam-jam lain yang diinginkan

    # Input teks dari pengguna
    synop_code = st.text_input("Masukkan sandi synop", max_chars=100, max_width=500)

    # Tombol untuk memproses data
    if st.button("Proses"):
        # Menjalankan fungsi sesuai pilihan jam
        if selected_hour == "00.00":
            df_seksi_0, df_seksi_1, df_seksi_3 = main_00UTC(synop_code)
        #elif selected_hour == "01.00":
            #df = main_01UTC(synop_code)
        #elif selected_hour == "02.00":
            #df = main_02UTC(synop_code)
        else:
            st.error("Jam yang dipilih tidak valid")

            # Menampilkan DataFrame jika ada
        #if 'df' in locals():
            #st.dataframe(df, height=1100, width=2000)

        # Menampilkan DataFrame jika ada
        if 'df_seksi_0' in locals():
            st.markdown("<h2>Seksi 0</h2>", unsafe_allow_html=True)
            st.dataframe(highlight_df(df_seksi_0), height=300, width=700)
        if 'df_seksi_1' in locals():
            st.markdown("<h2>Seksi 1</h2>", unsafe_allow_html=True)
            st.dataframe(highlight_df(df_seksi_1), height=450, width=700)
        if 'df_seksi_3' in locals():
            st.markdown("<h2>Seksi 3</h2>", unsafe_allow_html=True)
            st.dataframe(highlight_df(df_seksi_3), height=500, width=700)

def highlight_df(df):
    def highlight(row):
        # Menggunakan warna kuning untuk baris dengan nilai pada kolom output
        # Ganti 'output_column_name' dengan nama kolom output yang relevan
        if row['Output'] != "":
            return ['background-color: yellow'] * len(row)
        return [''] * len(row)

    return df.style.apply(highlight, axis=1)

if __name__ == '__main__':
    main()
