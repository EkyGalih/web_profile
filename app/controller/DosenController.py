from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa

from app import response, app, db
from flask import request

## cara simple
def index():
    try:
        dosen = Dosen.query.all()
        data = [
            {
                'id' : d.id,
                'nidn' : d.nidn,
                'nama' : d.nama,
                'phone' : d.phone,
                'alamat' : d.alamat
            } for d in dosen
        ]
        return response.success(data, "success")
    except Exception as e:
        print(e)
        return response.badRequest(str(e), "Failed")

## get single data
def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_dua == id))

        if not dosen:
            return response.badRequest([], "Tidak ada dosen ditemukan")
        
        dataMahasiswa = [
            {
                'id' : m.id,
                'nim' : m.nim,
                'nama' : m.nama,
                'phone' : m.phone,
                'alamat' : m.alamat
            } for m in mahasiswa
        ]
        data = SingleDetailMahasiswa(dosen, dataMahasiswa)
        return response.success(data, "success")
    except Exception as e:
        print(e)
        return response.badRequest(str(e), "Failed")
    
## save new record
def save():
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        dosens = Dosen(nidn=nidn, nama=nama, phone=phone, alamat=alamat)
        db.session.add(dosens)
        db.session.commit()
        
        return response.success('', 'Data Dosen Ditambahkan')
    except Exception as e:
        print(e)
        return response.badRequest(str(e), "error")

## update data
def ubah(id):
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        input = [
            {
                'nidn': nidn,
                'nama': nama,
                'phone': phone,
                'alamat': alamat
            }
        ]
        
        dosen = Dosen.query.filter_by(id=id).first()
        
        dosen.nidn = nidn
        dosen.nama = nama
        dosen.phone = phone
        dosen.alamat = alamat
        
        db.session.commit()
        
        return response.success('', "Data dosen berhasil diupdate")
    except Exception as e:
        print(e)
        return response.badRequest(str(e), "Failed")
    
## hapus data
def hapus(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        if not dosen:
            return response.badRequest([], "Data dosen tidak ditemukan")

        db.session.delete(dosen)
        db.session.commit()

        return response.success("", "Data dosen berhasil dihapus")
    except Exception as e:
        print(e)
        return response.badRequest(str(e), "Terjadi kesalahan saat hapus data dosen")

## fungsi tambahan untuk format data
def SingleDetailMahasiswa(dosen, mahasiswa):
    data = {
        'id' : dosen.id,
        'nidn' : dosen.nidn,
        'nama': dosen.nama,
        'phone': dosen.phone,
        'mahasiswa' : mahasiswa
    }
    return data

## pakai cara ribet dan lama ##

# def index():
#     try:
#         dosen = Dosen.query.all()
#         data = formatArray(dosen)
#         return response.success(data, "success")
#     except Exception as e:
#         print(e)
               
# def formatArray(datas):
#     array = []
    
#     for i in datas:
#         array.append(singleObject(i))
    
#     return array
        
# def singleObject(data):
#     data = {
#         'id' : data.id,
#         'nidn' : data.nidn,
#         'nama' : data.nama,
#         'phone' : data.phone,
#         'alamat' : data.alamat
#     }
    
#     return data