from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QFileDialog,
    QVBoxLayout, QWidget
)
from PySide6.QtGui import (
    QPixmap, QPainter, QPen, QBrush, QMouseEvent, QPolygon, QColor, QRegion
)
from PySide6.QtCore import Qt, QPoint, QRect
import sys, math

HANDLE_SIZE = 10  # size of square handles

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer with Move & Resize Tool")
        self.setGeometry(200, 200, 800, 600)

        # State
        self.points = []
        self.drawing_enabled = False
        self.image_loaded = False
        self.polygon_closed = False

        self.edit_enabled = False   # move+resize mode
        self.dragging = False
        self.resizing = False
        self.current_handle = None

        # For move
        self.move_origin = QPoint()
        self.cutout_pos = QPoint()

        # For resize
        self.resize_origin = QPoint()
        self.initial_rect = QRect()
        self.initial_pixmap = None

        # Widgets
        self.image_label = QLabel("No Image Loaded")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMouseTracking(True)
        self.image_label.setFocusPolicy(Qt.StrongFocus)
        self.image_label.mousePressEvent   = self.image_mouse_press
        self.image_label.mouseMoveEvent    = self.image_mouse_move
        self.image_label.mouseReleaseEvent = self.image_mouse_release

        self.open_button = QPushButton("Open Image")
        self.open_button.clicked.connect(self.open_image)

        self.pen_button = QPushButton("Pen Tool")
        self.pen_button.clicked.connect(self.enable_pen)

        self.move_button = QPushButton("Move/Resize Tool")
        self.move_button.clicked.connect(self.enable_edit)

        layout = QVBoxLayout()
        layout.addWidget(self.open_button)
        layout.addWidget(self.pen_button)
        layout.addWidget(self.move_button)
        layout.addWidget(self.image_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.bmp)")
        if not path:
            return
        self.original = QPixmap(path)
        self.working = self.original.copy()
        self.image_loaded = True
        # reset state
        self.points.clear()
        self.polygon_closed = False
        self.edit_enabled = False
        self.cutout = None
        self.image_label.setPixmap(self.working.scaled(
            self.image_label.size(), Qt.KeepAspectRatio))

    def enable_pen(self):
        if not self.image_loaded: return
        self.drawing_enabled = True
        self.edit_enabled = False
        self.polygon_closed = False
        self.points.clear()
        self.cutout = None
        self.working = self.original.copy()
        self.image_label.setPixmap(self.working.scaled(
            self.image_label.size(), Qt.KeepAspectRatio))

    def enable_edit(self):
        if not self.polygon_closed or self.cutout is None:
            return
        self.drawing_enabled = False
        self.edit_enabled = True

    def image_mouse_press(self, ev: QMouseEvent):
        if not self.image_loaded:
            return

        # map label coords → pixmap coords (same as before)
        x, y = self.map_to_pixmap(ev.position())
        pt = QPoint(x, y)

        # drawing polygon
        if self.drawing_enabled and not self.polygon_closed:
            if len(self.points) > 2 and self.dist(self.points[0], pt) < HANDLE_SIZE + 5:
                # close
                self.points.append(self.points[0])
                self.polygon_closed = True
                self.create_cutout()
            else:
                self.points.append(pt)
                self.draw_polygon()
            return

        # edit mode: check handles first
        if self.edit_enabled and self.cutout:
            br = self.cutout.rect().translated(self.cutout_pos)
            handle = self.hit_handle(pt, br)
            if handle:
                # start resizing
                self.resizing = True
                self.current_handle = handle
                self.resize_origin = pt
                self.initial_rect = br
                self.initial_pixmap = self.cutout.copy()
                return
            # else check move inside
            if br.contains(pt):
                self.dragging = True
                self.move_origin = pt

    def image_mouse_move(self, ev: QMouseEvent):
        if not self.image_loaded or not self.edit_enabled:
            return
        x, y = self.map_to_pixmap(ev.position())
        pt = QPoint(x, y)

        if self.dragging:
            delta = pt - self.move_origin
            self.move_origin = pt
            self.cutout_pos += delta
            self.redraw()
        elif self.resizing:
            self.resize_cutout(pt)

    def image_mouse_release(self, ev: QMouseEvent):
        self.dragging = self.resizing = False
        self.current_handle = None

    def dist(self, a, b):
        return math.hypot(b.x()-a.x(), b.y()-a.y())

    def map_to_pixmap(self, pos):
        lbl = self.image_label
        pm  = self.working
        lw, lh = lbl.width(), lbl.height()
        pw, ph = pm.width(), pm.height()
        scale = min(lw/pw, lh/ph)
        xo = (lw - pw*scale)/2;  yo = (lh - ph*scale)/2
        x = int((pos.x()-xo)/scale);  y = int((pos.y()-yo)/scale)
        return x, y

    def draw_polygon(self):
        self.working = self.original.copy()
        p = QPainter(self.working)
        pen = QPen(Qt.red, 2)
        p.setPen(pen)
        for i in range(1, len(self.points)):
            p.drawLine(self.points[i-1], self.points[i])
        # draw vertices
        for i,pt in enumerate(self.points):
            p.setBrush(QBrush(Qt.yellow if i==0 else Qt.green))
            p.drawEllipse(pt, HANDLE_SIZE//2, HANDLE_SIZE//2)
        p.end()
        self.image_label.setPixmap(self.working.scaled(
            self.image_label.size(), Qt.KeepAspectRatio))

    def create_cutout(self):
        # mask & extract
        poly = QPolygon(self.points)
        region = QRegion(poly)
        self.cutout = QPixmap(self.original.size())
        self.cutout.fill(Qt.transparent)
        p = QPainter(self.cutout)
        p.setClipRegion(region)
        p.drawPixmap(0,0,self.original)
        p.end()
        # erase original
        self.working = self.original.copy()
        p = QPainter(self.working)
        p.setClipRegion(region)
        p.fillRect(region.boundingRect(), QColor(0,0,0,0))
        p.end()
        # init cutout position at polygon's bbox top-left
        self.cutout_pos = region.boundingRect().topLeft()
        self.redraw()

    def redraw(self):
        tmp = self.working.copy()
        p = QPainter(tmp)
        p.drawPixmap(self.cutout_pos, self.cutout)
        # draw handles if editing
        if self.edit_enabled:
            br = self.cutout.rect().translated(self.cutout_pos)
            pen = QPen(Qt.blue, 1, Qt.DashLine)
            p.setPen(pen)
            p.drawRect(br)
            # corner handles
            for corner in [(br.left(),br.top()), (br.right(),br.top()),
                           (br.left(),br.bottom()),(br.right(),br.bottom())]:
                p.fillRect(corner[0]-HANDLE_SIZE//2, corner[1]-HANDLE_SIZE//2,
                           HANDLE_SIZE, HANDLE_SIZE, Qt.white)
                p.setPen(QPen(Qt.black,1))
                p.drawRect(corner[0]-HANDLE_SIZE//2, corner[1]-HANDLE_SIZE//2,
                           HANDLE_SIZE, HANDLE_SIZE)
        p.end()
        self.image_label.setPixmap(tmp.scaled(
            self.image_label.size(), Qt.KeepAspectRatio))

    def hit_handle(self, pt, br: QRect):
        # returns which corner: 'tl','tr','bl','br'
        corners = {
            'tl': QPoint(br.left(), br.top()),
            'tr': QPoint(br.right(), br.top()),
            'bl': QPoint(br.left(), br.bottom()),
            'br': QPoint(br.right(), br.bottom()),
        }
        for name, cpt in corners.items():
            if abs(pt.x()-cpt.x())<=HANDLE_SIZE and abs(pt.y()-cpt.y())<=HANDLE_SIZE:
                return name
        return None

    def resize_cutout(self, pt: QPoint):
        # compute new rect by dragging current_handle
        r = QRect(self.initial_rect)
        if self.current_handle == 'tl':
            r.setTopLeft(pt)
        elif self.current_handle == 'tr':
            r.setTopRight(pt)
        elif self.current_handle == 'bl':
            r.setBottomLeft(pt)
        elif self.current_handle == 'br':
            r.setBottomRight(pt)

        # avoid zero/negative
        if r.width()<10 or r.height()<10:
            return

        # scale original cutout pixmap to new size
        self.cutout = self.initial_pixmap.scaled(r.size())
        # update position
        self.cutout_pos = r.topLeft()
        self.redraw()

    def keyPressEvent(self, ev):
        if (ev.modifiers()==Qt.ControlModifier and ev.key()==Qt.Key_Z
            and self.drawing_enabled and not self.polygon_closed
            and self.points):
            self.points.pop()
            self.draw_polygon()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ImageViewer()
    w.show()
    sys.exit(app.exec())
