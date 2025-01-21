from functools import partial

DEFAULT_SPEED = 250

class SlidingStackedWidget(QStackedWidget):

    LEFT2RIGHT, RIGHT2LEFT, TOP2BOTTOM, BOTTOM2TOP, AUTOMATIC = range(5)

    def __init__(self, *args, **kwargs):
        super(SlidingStackedWidget, self).__init__(*args, **kwargs)
        self._pnow = QPoint(0, 0)
        # animation speed
        self._speed = DEFAULT_SPEED
        # current index
        self._now = 0
        # current index in automatic mode
        self._current = 0
        # next index
        self._next = 0
        # Activate now
        self._active = 0
        # animation direction (default is landscape)
        self._orientation = Qt.Horizontal
        # Animation Curve Type
        self._easing = QEasingCurve.Linear
        # initialization animation
        self._initAnimation()

    def setSpeed(self, speed=DEFAULT_SPEED):
        """Set animation speed
        :param speed:       speed value, Default is DEFAULT_SPEED
        :type speed:        int
        """
        self._speed = speed

    @pyqtProperty(int, fset=setSpeed)
    def speed(self):
        return self._speed

    def setOrientation(self, orientation=Qt.Horizontal):
        """Set the direction of the animation(landscape and portrait)
        :param orientation:    direction(Qt.Horizontal or Qt.Vertical)
        :type orientation:     http://doc.qt.io/qt-5/qt.html#Orientation-enum
        """
        self._orientation = orientation

    @pyqtProperty(int, fset=setOrientation)
    def orientation(self):
        return self._orientation

    def setEasing(self, easing=QEasingCurve.OutBack):
        """Set the curve type for animation
        :param easing:    默认为QEasingCurve.OutBack
        :type easing:     http://doc.qt.io/qt-5/qeasingcurve.html#Type-enum
        """
        self._easing = easing

    @pyqtProperty(int, fset=setEasing)
    def easing(self):
        return self._easing

    def slideInNext(self):
        """Swipe to next page"""
        now = self.currentIndex()
        if now < self.count() - 1:
            self.slideInIdx(now + 1)
            self._current = now + 1

    def slideInPrev(self):
        """Swipe to previous page"""
        now = self.currentIndex()
        if now > 0:
            self.slideInIdx(now - 1)
            self._current = now - 1

    def slideInLast(self):
        """Swipe to last page"""
        # now = self.currentIndex()
        # if now < self.count() - 1:
        #     self.slideInIdx(now + 1)
        #     self._current = now + 1
        pos = self.count() - 1
        self.slideInIdx(pos)
        self._current = pos

    def slideInFirst(self):
        """Swipe to first page"""
        pos = 0
        self.slideInIdx(pos)
        self._current = pos

    def slideInIdx(self, idx, direction=4):
        """Slide to the specified serial number
        :param idx:               serial number
        :type idx:                int
        :param direction:         direction,The default is AUTOMATIC=4
        :type direction:          int
        """
        if idx > self.count() - 1:
            direction = self.TOP2BOTTOM if self._orientation == Qt.Vertical else self.RIGHT2LEFT
            idx = idx % self.count()
        elif idx < 0:
            direction = self.BOTTOM2TOP if self._orientation == Qt.Vertical else self.LEFT2RIGHT
            idx = (idx + self.count()) % self.count()
        self.slideInWgt(self.widget(idx), direction)

    def slideInWgt(self, widget, direction):
        """Swipe to the specified widget
        :param widget:        QWidget, QLabel, etc...
        :type widget:         QWidget Base Class
        :param direction:     direction
        :type direction:      int
        """
        if self._active:
            return
        self._active = 1
        _now = self.currentIndex()
        _next = self.indexOf(widget)
        if _now == _next:
            self._active = 0
            return

        w_now = self.widget(_now)
        w_next = self.widget(_next)

        # Automatically determine the direction
        if _now < _next:
            directionhint = self.TOP2BOTTOM if self._orientation == Qt.Vertical else self.RIGHT2LEFT
        else:
            directionhint = self.BOTTOM2TOP if self._orientation == Qt.Vertical else self.LEFT2RIGHT
        if direction == self.AUTOMATIC:
            direction = directionhint

        # Calculate the offset
        offsetX = self.frameRect().width()
        offsetY = self.frameRect().height()
        w_next.setGeometry(0, 0, offsetX, offsetY)

        if direction == self.BOTTOM2TOP:
            offsetX = 0
            offsetY = -offsetY
        elif direction == self.TOP2BOTTOM:
            offsetX = 0
        elif direction == self.RIGHT2LEFT:
            offsetX = -offsetX
            offsetY = 0
        elif direction == self.LEFT2RIGHT:
            offsetY = 0

        # Reposition the next widget outside/next to the display area
        pnext = w_next.pos()
        pnow = w_now.pos()
        self._pnow = pnow

        # Move to the specified location and display
        w_next.move(pnext.x() - offsetX, pnext.y() - offsetY)
        w_next.show()
        w_next.raise_()

        self._animnow.setTargetObject(w_now)
        self._animnow.setDuration(self._speed)
        self._animnow.setEasingCurve(self._easing)
        self._animnow.setStartValue(QPoint(pnow.x(), pnow.y()))
        self._animnow.setEndValue(QPoint(offsetX + pnow.x(), offsetY + pnow.y()))

        self._animnext.setTargetObject(w_next)
        self._animnext.setDuration(self._speed)
        self._animnext.setEasingCurve(self._easing)
        self._animnext.setStartValue(QPoint(-offsetX + pnext.x(), offsetY + pnext.y()))
        self._animnext.setEndValue(QPoint(pnext.x(), pnext.y()))

        self._next = _next
        self._now = _now
        self._active = 1
        self._animgroup.start()

    def _initAnimation(self):
        """Initialize animation variables for current page and next page"""
        # animation of the current page
        self._animnow = QPropertyAnimation(
            self, propertyName=b'pos', duration=self._speed,
            easingCurve=self._easing)
        # Animation on the next page
        self._animnext = QPropertyAnimation(
            self, propertyName=b'pos', duration=self._speed,
            easingCurve=self._easing)
        # Parallel animation group
        self._animgroup = QParallelAnimationGroup(
            self, finished=self.animationDoneSlot)
        self._animgroup.addAnimation(self._animnow)
        self._animgroup.addAnimation(self._animnext)

    def setCurrentIndex(self, index):
        # Override the animation switching implemented by this method
        # super(SlidingStackedWidget, self).setCurrentIndex(index)
        # Resolutely cannot call the above function, otherwise the animation will fail
        self.slideInIdx(index)

    def setCurrentWidget(self, widget):
        # Override the animation switching implemented by this method
        super(SlidingStackedWidget, self).setCurrentWidget(widget)
        # Resolutely cannot call the above function, otherwise the animation will fail
        self.setCurrentIndex(self.indexOf(widget))

    def animationDoneSlot(self):
        """animation end handler"""
        # Since the setCurrentIndex method is overridden, the method of the parent class itself is used here
        #         self.setCurrentIndex(self._next)
        QStackedWidget.setCurrentIndex(self, self._next)
        w = self.widget(self._now)
        w.hide()
        w.move(self._pnow)
        self._active = 0

    def autoStop(self):
        """stop autoplay"""
        if hasattr(self, '_autoTimer'):
            self._autoTimer.stop()

    def autoStart(self, msec=3000):
        """Automatic carousel
        :param time: time, Default 3000, 3 seconds
        """
        if not hasattr(self, '_autoTimer'):
            self._autoTimer = QTimer(self, timeout=self._autoStart)
        self._autoTimer.stop()
        self._autoTimer.start(msec)

    def _autoStart(self):
        if self._current == self.count():
            self._current = 0
        self._current += 1
        self.setCurrentIndex(self._current)

