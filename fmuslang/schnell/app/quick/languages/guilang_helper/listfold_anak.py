
class __WIDGET_ANAK_NAME__(QWidget):
    def __init__(self, item, *args, **kwargs):
        super(__WIDGET_ANAK_NAME__, self).__init__(*args, **kwargs)
        self.item = item # jk gak handle resize, gak keliatan


__TEMPLATE_CONTENT__


    def resizeEvent(self, event):
        super(__WIDGET_ANAK_NAME__, self).resizeEvent(event)
        self.item.setSizeHint(QSize(self.minimumWidth(), 300))
