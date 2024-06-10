from fpdf import FPDF
import matplotlib.pyplot as plt
import io

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Laporan Forensik', 0, 1, 'C')

    def judul_bab(self, judul):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, judul, 0, 1, 'L')
        self.ln(10)

    def isi_bab(self, isi):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, isi)
        self.ln()

    def tambahkan_gambar(self, img_data, x=None, y=None, w=0, h=0):
        self.image(img_data, x, y, w, h)

def buat_laporan(data):
    pdf = PDF()
    pdf.add_page()

    pdf.judul_bab('Pesan yang Diekstrak')

    for item in data:
        isi = f"Tanggal: {item['tanggal']}\nDari: {item['alamat']}\nPesan: {item['teks']}\n\n"
        pdf.isi_bab(isi)

    pdf.judul_bab('Linimasa Pesan')

    # Membuat linimasa pesan
    tanggal = [item['tanggal'] for item in data]
    plt.hist(tanggal, bins=20, edgecolor='black')
    plt.title('Linimasa Pesan')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Pesan')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    pdf.tambahkan_gambar(buf, x=10, y=None, w=190)

    pdf.output("laporan_forensik.pdf")
