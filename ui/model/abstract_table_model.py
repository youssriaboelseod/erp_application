from abc import abstractmethod

from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt


class AbstractTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(AbstractTableModel, self).__init__(parent)

    def rowCount(self, parent):
        return len(self.data)

    def columnCount(self, parent):
        return len(self.data[0])

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.header[col])
        return QVariant()

    @abstractmethod
    def data(self, index, role):
        raise NotImplementedError("Subclass must implement abstract method")
