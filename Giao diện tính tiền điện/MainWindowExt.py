from PyQt6.QtWidgets import QMessageBox

from MainWindowt import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonSHBT.clicked.connect(self.tinhshbt)
        self.pushButtonKinhDoanh.clicked.connect(self.tinhkinhdoanh)
        self.pushButtonSanXuat.clicked.connect(self.tinhsanxuat)
        self.pushButtonHuong.clicked.connect(self.huongdan)
    def tinhshbt(self):
        a=float(self.lineEditChisocu.text())
        b=float(self.lineEditChisomoi.text())
        c=float(self.lineEditSoho.text())
        d=b-a
        d=round(d)
        if d <= 50 * c:
            pay = d * 1484
        elif d <= 100 * c:
            pay = (50 * c * 1484) + ((d - 50 * c) * 1533)
        elif d <= 200 * c:
            pay = (50 * c * 1484) + (50 * c * 1533) + ((d - 100 * c) * 1786)
        elif d <= 300 * c:
            pay = (50 * c * 1484) + (50 * c * 1533) + (100 * c * 1786) + ((d - 200 * c) * 2242)
        elif d <= 400 * c:
            pay = (50 * c * 1484) + (50 * c * 1533) + (100 * c * 1786) + (100 * c * 2242) + ((d - 300 * c) * 2503)
        else:
            pay = (50 * c * 1484) + (50 * c * 1533) + (100 * c * 1786) + (100 * c * 2242) + (100 * c * 2503) + (
                        (d - 400 * c) * 2587)
        self.lineEditSokWhdung.setText(f"{d}")
        self.labelTienthu.setText(f"Tiền SHBT ={pay}")
    def tinhkinhdoanh(self):
        a = float(self.lineEditChisocu.text())
        b = float(self.lineEditChisomoi.text())
        d = b-a
        d = round(d)
        kinhdoanh=(b - a) * 2320
        self.lineEditSokWhdung.setText(f"{d}")
        self.labelTienthu.setText(f"Tiền kinh doanh ={kinhdoanh}")
    def tinhsanxuat(self):
        a = float(self.lineEditChisocu.text())
        b = float(self.lineEditChisomoi.text())
        d = b - a
        d = round(d)
        sanxuat = (b - a) * 1518
        self.lineEditSokWhdung.setText(f"{d}")
        self.labelTienthu.setText(f"Tiền sản xuất ={sanxuat}")

    def huongdan(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Exit Confirmation")
        dlg.setText("Đây là phần mềm tính tiền điện\nKỹ sư thiết kế: Đặng Ngọc Hoài Phương")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Ok
        )
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        # check the user confirmation
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Ok:
            self.MainWindow.close()
        else:
            pass  # do nothing
    def show(self):
        self.MainWindow.show()
