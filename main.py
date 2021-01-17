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

import rospy
from std_msgs.msg import *
from industry_library_robot.srv import *
from ultrasound_robot.srv import *
from geometry_msgs.msg import Pose, PoseArray
import inspect
import ctypes

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

bouding_box_color = []
for i in range(15):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)    
    bouding_box_color.append((r,g,b))

camera_width = 640
camera_height = 480

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
        self.ros_setup()
        self.start_process_picking()
        self.start_process_polishing()
    
    def ros_setup(self):
        self.pub = rospy.Publisher('chatter', String, queue_size=1)
        self.tf_transfer_pub = rospy.Publisher('/camera_object_position', Pose, queue_size=1)
        rospy.init_node('gui', anonymous=True)
        self.rate = rospy.Rate(10)
        self.ros_grasp = False
        self.ros_move_home = False
        self.wipe_bb = False
    
    def pick_and_place_client(self, object_position, place_point):
        rospy.wait_for_service('pick_and_place_service')
        try:
            pap = rospy.ServiceProxy('pick_and_place_service', pick_and_place)
            pose = Pose()
            pose.position.x = object_position[0]
            pose.position.y = object_position[1]
            pose.position.z = object_position[2]
            pose.orientation.w = 1
            self.tf_transfer_pub.publish(pose)
            resp1 = pap(pose, place_point)
            return resp1.is_successful
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

    def move_home_client(self):
        rospy.wait_for_service('move_home_pose_service')
        try:
            pap = rospy.ServiceProxy('move_home_pose_service', pick_and_place)
            pose = Pose()
            resp1 = pap(pose, 0)
            return resp1.is_successful
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

    def wipe_blackboard_client(self, waypoints):
        rospy.wait_for_service('wipe_blackboard_service')
        try:
            wbb = rospy.ServiceProxy('wipe_blackboard_service', wipe_bb)
            pose_array = PoseArray()
            for pt in waypoints:
                pose = Pose()
                pose.position.x = pt[0]
                pose.position.y = pt[1]
                pose_array.poses.append(pose)
            resp1 = wbb(pose_array)
            return resp1.is_successful
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

    def ros_service_thread(self):
        while True:
            if self.ros_grasp is True:
                object = self.object_comboBox.currentText()
                place_pt = self.place_pt_comboBox.currentText()
                self.pick_and_place_client(self.object_list[object]['position'][0:3], int(place_pt[-1]))
                self.ros_grasp = False
                print("grasp object: " + object)

            if self.ros_move_home is True:
                self.move_home_client()
                self.ros_move_home = False
                print("move home")

            if self.wipe_bb is True:
                print("self.wipe_bb", self.wipe_bb)
                waypoints = self.selected_pts
                self.wipe_blackboard_client(waypoints)
                self.selected_pts.clear()
                self.wipe_bb = False
                print("wipe blackboard")
                
            time.sleep(0.1)

    # def ros_broadcast_tf(self):
    #     while self.ros_grasp is True:
    #         br = tf.TransformBroadcaster()
    #         object = self.object_comboBox.currentText()
    #         p = self.object_list[object]['position']
    #         br.sendTransform((p[0], p[1], p[2]),
    #                         tf.transformations.quaternion_from_euler(0, 0, 0),
    #                         rospy.Time.now(),
    #                         "target_object",
    #                         "camera_frame")
    #         time.sleep(0.001)

    def self_defined_ui_variables(self):
        self.video_signal.connect(self.video_slot_func)
        self.video_signal_2.connect(self.video_slot_func_2)
    
    def start_process_polishing(self):
        self.selected_pts = []
        self.video_label_2.mousePressEvent = self.get_image_pos_2
        self.set_path_button.clicked.connect(self.click_set_path_button)
        self.confirm_path_button.clicked.connect(self.click_confirm_path_button)
        self.send_path_button.clicked.connect(self.click_send_path_button)
        self.emergency_stop_button_2.setStyleSheet("background-color: red")
        
        self.t3 = threading.Thread(target=self.update_video_2)
        self.t3.start()
        
    def start_process_picking(self):
        self.object_list = dict()
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
        self.t1 = threading.Thread(target=self.update_combobox)
        self.t1.start()
        self.t2 = threading.Thread(target=self.update_video)
        self.t2.start()
        self.t4 = threading.Thread(target=self.ros_service_thread)
        self.t4.start()

    def click_select_object_Button(self):
        self.button = 'select_object'
        self.select_object_Button.setStyleSheet("background-color: green")
    
    def click_select_place_pt_Button(self):
        self.button = 'select_place_pt'
        self.select_place_pt_Button.setStyleSheet("background-color: green")
        
    def object_comboBox_selection_change(self):
        self.object_info_TextEdit.setPlainText("样品名称:  "+ self.object_comboBox.currentText() + "\n")

    def click_move2home_button(self):
        self.ros_move_home = True
        print("click_move2home_button")    

    def click_grasp_button(self):
        self.ros_grasp = True
        print("click_grasp_button")
        
    def click_place_button(self):
        #place_point = self.place_pt_plainTextEdit.toPlainText()
        #place_point = place_point[1:-1].split(',')
        #place_point = self.from_widget_to_camera([int(place_point[0]), int(place_point[1])])
        # place_pt = self.place_pt_comboBox.currentText()
        # print("click_place_button")
        # print("place point: " + place_pt)
        stop_thread(self.t1)
        stop_thread(self.t2)
        stop_thread(self.t3)
        stop_thread(self.t4)
        exit()




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
        self.wipe_bb = True
        # self.selected_pts.clear()
        
    def update_combobox(self):
        while True:
            object_list = self.r.hget('object_list', 'one')
            object_list = str(object_list, encoding='utf-8')
            object_list = json.loads(object_list)
            # print("object_list:{}, self.object_list:{}".format(object_list.keys(), self.object_list.keys()))
            if operator.eq(object_list.keys(), self.object_list.keys()) is False:
                self.object_comboBox.clear()
                #self.object_comboBox.addItem("--Select--")
                self.object_comboBox.addItems(list(object_list.keys()))
                self.object_list = object_list
                print("change combobox")
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
            '''for object_name in object_list:
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
                del draw'''
            raw_img = np.asarray(img)
            img = QImage(raw_img.data, raw_img.shape[1], raw_img.shape[0], QImage.Format_BGR888)
            self.video_signal.emit(QPixmap.fromImage(img))
            time.sleep(0.03)
            
    def update_video_2(self):
        radius = 3 # 3 pixel
        while True:
            raw_img = redis_img_receiver.fromRedis(self.r,'image')
            #img = cv2.resize(img, (camera_width, camera_height))
            img = Image.fromarray(raw_img, 'RGB')
            points = self.selected_pts
            draw = ImageDraw.Draw(img)
            if len(points) > 0:
                for pt in points:
                    # cv2.circle(img, (), 8, (255,0,0), 3)
                    draw.ellipse((pt[0]-radius,pt[1]-radius, pt[0]+radius,pt[1]+radius), fill = (255, 0, 0))
                    #draw circle
                if len(points) > 1:
                    for i in range(len(points)-1):
                        # cv2.line(img, (points[i][0],points[i][1]), (points[i+1][0],points[i+1][1]), (255,0,0), 2)
                        draw.line((points[i][0],points[i][1], points[i+1][0],points[i+1][1]), fill = 128)
                        #draw line
                        #line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None):
            raw_img = np.asarray(img)
            img = QImage(raw_img.data, raw_img.shape[1], raw_img.shape[0], QImage.Format_BGR888)
            self.video_signal_2.emit(QPixmap.fromImage(img))
            time.sleep(0.03)

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
        # print("pt:{} {}    video_label{} {}".format(pt[0], pt[1], self.video_label.width(), self.video_label.height()))
        pt[0] = int(camera_width*pt[0]/self.video_label_2.width())
        pt[1] = int(camera_height*pt[1]/self.video_label_2.height())
        # print("pt:{} {}    video_label{} {}".format(pt[0], pt[1], self.video_label.width(), self.video_label.height()))
        return pt
    
    def exit(self):
        exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())