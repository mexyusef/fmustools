

        i = __LOOP_INDEX__
        # tiap list item punya 2 komponen: button dan content
        # item = button
        item = QListWidgetItem(self)		
        fold_button = FoldButton(item, '__FOLD_TITLE__', self, objectName='testBtn') # set parent dari button = item			
        self.setItemWidget(item, fold_button) # item, button = parent, child
        # item2 = content
        item2 = QListWidgetItem(self)
        anak = __WIDGET_ANAK_NAME__(item2, self) # set parent dari widgetanak = item2
        self.setItemWidget(item2, anak) # item, anak = parent, child
        # buka yg pertama saja...
        if i != 0:
            item2.setHidden(True)
            fold_button.setChecked(True)
        fold_button.toggled.connect(item2.setHidden) # last, sambungkan button di item ke toggle item2

