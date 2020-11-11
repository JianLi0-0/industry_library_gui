import sys
from ui_mainwindow import Ui_MainWindow
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import *
from PySide2.QtGui import *
import redis_img_receiver
import redis
import threading
import json
import time
import operator
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont

bouding_box_color = []
for i in range(15):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)    
    bouding_box_color.append((r,g,b))

camera_width = 640
camera_height = 360

class MainWindow(QMainWindow, Ui_MainWindow):
    video_signal = Signal(QPixmap)
    video_signal_2 = Signal(QPixmap)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.self_defined_ui_variables()
        self.pool = redis.ConnectionPool(host='localhost',port=6379)
        self.r = redis.Redis(connection_pool=self.pool)
        self.button = ''
        self.start_process_picking()
        self.start_process_polishing()
        
    def self_defined_ui_variables(self):
        self.video_signal.connect(self.video_slot_func)
        self.video_signal_2.connect(self.video_slot_func_2)
    
    def start_process_polishing(self):
        self.selected_pts = []
        #self.video_label_2.mousePressEvent = self.get_image_pos_2
        #self.set_path_button.clicked.connect(self.click_set_path_button)
        #self.confirm_path_button.clicked.connect(self.click_confirm_path_button)
        #self.send_path_button.clicked.connect(self.click_send_path_button)
        self.emergency_stop_button_2.setStyleSheet("background-color: red")
        
        t3 = threading.Thread(target=self.update_video_2)
        t3.start()  
        
    def start_process_picking(self):
        self.object_list = []
        #self.video_label.mousePressEvent = self.get_image_pos
        #self.select_object_Button.clicked.connect(self.click_select_object_Button)
        #self.select_place_pt_Button.clicked.connect(self.click_select_place_pt_Button)
        
        self.move2home_button.clicked.connect(self.click_move2home_button)
        self.grasp_button.clicked.connect(self.click_grasp_button)
        self.place_button.clicked.connect(self.click_place_button)
        self.emergency_stop_button.clicked.connect(self.click_emergency_stop_button)
        self.emergency_stop_button.setStyleSheet("background-color: red")
        self.object_comboBox.currentIndexChanged.connect(self.object_comboBox_selection_change)
                #self.object_info_TextEdit.setPlainText("haha\nclick_move2home_button")
        t1 = threading.Thread(target=self.update_combobox)
        t1.start()
        t2 = threading.Thread(target=self.update_video)
        t2.start()
        
    def click_select_object_Button(self):
        self.button = 'select_object'
        self.select_object_Button.setStyleSheet("background-color: green")
       
    def click_select_place_pt_Button(self):
        self.button = 'select_place_pt'
        self.select_place_pt_Button.setStyleSheet("background-color: green")
        
    def object_comboBox_selection_change(self):
        self.object_info_TextEdit.setPlainText("样品名称:  "+ self.object_comboBox.currentText() + "\n")

    def click_move2home_button(self):
        print("click_move2home_button")    
    
    def click_grasp_button(self):
        object = self.object_comboBox.currentText()
        print("click_grasp_button")
        print("grasp object: " + object)
        
    def click_place_button(self):
        #place_point = self.place_pt_plainTextEdit.toPlainText()
        #place_point = place_point[1:-1].split(',')
        #place_point = self.from_widget_to_camera([int(place_point[0]), int(place_point[1])])
        place_pt = self.place_pt_comboBox.currentText()
        print("click_place_button")
        print("place point: " + place_pt)
        
    def click_emergency_stop_button(self):
        print("click_emergency_stop_button")    
    
        
    def click_set_path_button(self):
        self.button = 'set_path'
        self.set_path_button.setStyleSheet("background-color: green")    
        
    def click_confirm_path_button(self):
        self.button = ''
        self.set_path_button.setStyleSheet("background-color: white")
        print(self.selected_pts)
        
    def click_send_path_button(self):
        print("Send path to robot")
        self.selected_pts.clear()
        
    def update_combobox(self):
        while True:
            object_list = self.r.hget('object_list', 'one')
            object_list = str(object_list, encoding='utf-8')
            object_list = json.loads(object_list)
            if operator.eq(object_list, self.object_list) is False:
                self.object_comboBox.clear()
                #self.object_comboBox.addItem("--Select--")
                self.object_comboBox.addItems(list(object_list.keys()))
                self.object_list = object_list
                #print("change combobox")
            time.sleep(1)
            
    def update_video(self):
        while True:
            object_list = self.r.hget('object_list', 'one')
            object_list = str(object_list, encoding='utf-8')
            object_list = json.loads(object_list)      
            
            raw_img = redis_img_receiver.fromRedis(self.r,'image')
            #img = cv2.resize(img, (camera_width, camera_height))
            img = Image.fromarray(raw_img, 'RGB')
            
            #print(img.shape)
            for object_name in object_list:
                # 画矩形框
                [x1, y1, x2, y2] = object_list[object_name]['bounding_box'][0:4]
                index = list(object_list.keys()).index(object_name)
                draw = ImageDraw.Draw(img)
                draw.rectangle([x1,y1, x2,y2],outline=bouding_box_color[index])            
                # 标注文本
                font = ImageFont.truetype("HyFMoonlight-2.ttf", 15)
                #cv2.putText(img, text, (x1, y1-7), font, 2, bouding_box_color[index], 1)
                text_origin = np.array([x1, y1-16])
                draw.text(text_origin, object_name, fill=(0, 0, 0), font=font)
                del draw
            raw_img = np.asarray(img)
            img = QImage(raw_img.data, raw_img.shape[1], raw_img.shape[0], QImage.Format_BGR888)
            self.video_signal.emit(QPixmap.fromImage(img))
            time.sleep(0.03)
            
    def update_video_2(self):
        while True:
            img = redis_img_receiver.fromRedis(self.r,'image')
            points = self.selected_pts
            #if len(points) > 0:
                #for pt in points:
                    #cv2.circle(img, (pt[0],pt[1]), 8, (255,0,0), 3)
                    ##draw circle
                    ##circle(img, center, radius, color, thickness=None, lineType=None, shift=None)
                #if len(points) > 1:
                    #for i in range(len(points)-1):
                        #cv2.line(img, (points[i][0],points[i][1]), (points[i+1][0],points[i+1][1]), (255,0,0), 2)
                        ##draw line
                        ##line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None):
            img = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_BGR888)
            self.video_signal_2.emit(QPixmap.fromImage(img))
            time.sleep(0.05)

    @Slot(QImage)
    def video_slot_func(self, img):
        # 调用setPixmap函数设置显示Pixmap
        self.video_label.setPixmap(img)
        # 调用setScaledContents将图像比例化显示在QLabel上
        self.video_label.setScaledContents(True)
        
    @Slot(QImage)
    def video_slot_func_2(self, img):
        # 调用setPixmap函数设置显示Pixmap
        self.video_label_2.setPixmap(img)
        # 调用setScaledContents将图像比例化显示在QLabel上
        self.video_label_2.setScaledContents(True)   

    def thread_test(self):
        while True:
            print("thread_test")
            time.sleep(1)

    def show_pic(self):
        self.timer_video.timeout.connect(self.update_pic)
        
    def update_pic(self):
        #flag, img = self.cam.read()
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #img = redis_img_receiver.fromRedis(self.r,'image')
        
        ## 画矩形框
        #cv2.rectangle(img, (40,157), (180,350), (0,255,0), 4)
        ## 标注文本
        #font = cv2.FONT_HERSHEY_PLAIN
        #text = 'Object1'
        #cv2.putText(img, text, (40, 150), font, 2, (0,255,0), 1)
        
        img = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_BGR888)
        self.video_label.setPixmap(QPixmap.fromImage(img))
        self.video_label.setScaledContents(True)
        
    def get_image_pos(self, event):  ##重载鼠标点击事件
        if event.buttons () == Qt.LeftButton:
            if self.button == 'select_object':
                object_list = self.r.hget('object_list', 'one')
                object_list = str(object_list, encoding='utf-8')
                object_list = json.loads(object_list)
                object_list = self.from_camera_to_widget(object_list)
                x = event.pos().x()
                y = event.pos().y()
                for object_name in object_list:
                    is_within_box = self.is_within_box(x, y, object_list[object_name]['bounding_box'])
                    if is_within_box is True:
                        self.object_comboBox.setCurrentText(object_name)
                        print('Selected object is ' + object_name + ' .')
                        self.place_pt_plainTextEdit.setPlainText('')
                        break
            elif self.button == 'select_place_pt':
                self.place_pt_plainTextEdit.setPlainText("("+str(event.pos().x())+", "+str(event.pos().y())+")")
                print("Place point is"+"("+str(event.pos().x())+", "+str(event.pos().y())+")")
            elif self.button == '':
                print('Please click the button \"select_object\" or \"select_place_pt\"')
            self.button = ''
            self.select_object_Button.setStyleSheet("background-color: white")
            self.select_place_pt_Button.setStyleSheet("background-color: white")    
            
    def get_image_pos_2(self, event):
        if event.buttons () == Qt.LeftButton:
            print("left click")
            if self.button == 'set_path':
                x = event.pos().x()
                y = event.pos().y()
                self.selected_pts.append(self.from_widget_to_camera([x, y]))
            else:
                print("Please click the Set path button before selecting point. ")
            
    def is_within_box(self, x, y, box):
        if x > box[0] and x < box[2]:
            if y > box[1] and y < box[3]:
                return True
            else:
                return False
        else:
            return False        

    def from_camera_to_widget(self, object_list):
        for object_name in object_list:
            object_list[object_name]['bounding_box'][0] = int(self.video_label.width()*object_list[object_name]['bounding_box'][0]/camera_width)
            object_list[object_name]['bounding_box'][2] = int(self.video_label.width()*object_list[object_name]['bounding_box'][2]/camera_width)
            object_list[object_name]['bounding_box'][1] = int(self.video_label.height()*object_list[object_name]['bounding_box'][1]/camera_height)
            object_list[object_name]['bounding_box'][3] = int(self.video_label.height()*object_list[object_name]['bounding_box'][3]/camera_height)
        return object_list
    
    def from_widget_to_camera(self, pt):     
        pt[0] = int(camera_width*pt[0]/self.video_label.width())
        pt[1] = int(camera_height*pt[1]/self.video_label.height())
        return pt
    
    def exit(self):
        exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())