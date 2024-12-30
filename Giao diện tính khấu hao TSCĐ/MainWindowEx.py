from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox
from MainWindow import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton.clicked.connect(self.tinhkhauhao)
        self.pushButton_2.clicked.connect(self.xemkhauhao)

    def tinhkhauhao(self):
        # Lấy dữ liệu từ các ô nhập liệu
        self.giamua = float(self.lineEditGiamuamoi.text())
        self.phivanchuyen = float(self.lineEditphivanchuyen.text())
        self.philapdat = float(self.lineEditphilapdat.text())
        self.sonam = int(self.lineEditsonamsudungdukien.text())

        # Tính toán
        self.nguyengia = self.giamua + self.phivanchuyen + self.philapdat
        self.khauhaonam = self.nguyengia / self.sonam
        self.khauhaothang = self.khauhaonam / 12
        self.accumulated_depreciation = 0
        self.nguyengia=round(self.nguyengia)
        self.khauhaonam=round(self.khauhaonam)
        self.khauhaothang=round(self.khauhaothang)
        self.lineEditnguyengiaTSCD.setText(f"{self.nguyengia}")
        self.lineEditkhauhaonam.setText(f"{self.khauhaonam}")
        self.lineEditkhauhaothang.setText(f"{self.khauhaothang}")

    def xemkhauhao(self):
        self.depreciation_details = []
        # Kiểm tra nếu `tinhkhauhao` chưa được gọi
        if not hasattr(self, 'sonam'):
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng bấm 'Tính Khấu Hao' trước!")
            return

        # Xử lý từng năm khấu hao
        for year in range(0, self.sonam ):
            # Khấu hao năm cuối sẽ là 0
            if year == self.sonam:
                depreciation = 0
            else:
                depreciation = self.khauhaonam

            self.accumulated_depreciation += depreciation
            final_depreciation_rate = self.nguyengia - self.accumulated_depreciation
            # Thêm chi tiết khấu hao tháng
            self.depreciation_details.append(
                f"<span style='color: white;'>Năm {year+1}, Sau khấu hao còn => {final_depreciation_rate:} VNĐ</span>")

        # Hiển thị thông tin khấu hao với HTML
        depreciation_text = "<br>".join(self.depreciation_details)
        self.labelxemchitietkhauhao.setText(depreciation_text)
        self.labelxemchitietkhauhao.setTextFormat(Qt.TextFormat.RichText)

    def show(self):
        self.MainWindow.show()