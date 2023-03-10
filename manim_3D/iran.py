from manim import *
import pandas as pd
import numpy as np
import os
#from cha import chaghCreature
#from math import cos , sin 
df = pd.read_csv("/media/mohammadsaleh/bootcamp/project1/Quera_Data_Science/fidilio scrape/data.csv")
lat_lon = np.array(df[['latitude', 'longitude']])

class a3 (ThreeDScene):

    def construct(self):
        
        dirname = os.path.dirname(__file__)
        #self.camera.background_color = "#EEEEEE"
        #triangle = Triangle ()
        #triangle.scale(1)
        
        #self.play(Write(triangle))
        #self.wait(0.5)
        ir = SVGMobject(file_name = dirname +"/Iran.svg" , fill_opacity= 0.2 , stroke_color=WHITE , stroke_width=0.1 , stroke_opacity=100)
        ir.scale(8.17153527488908)
        #ir.move_to([53.16029934461913 , 31.63429934461913 , 0])
        self.play(Create(ir))
        self.wait(0.2)
        self.play(ir.animate.move_to([53.672524 ,32.410415 ,  0]) , 
                #self.camera.frame.animate.scale(3.5).move_to([53.672524 ,32.410415,0])
                )
        #d = Dot(color=RED ).move_to([ 51.834168,34.505956,0]).scale(5.005)
        #d2 = Dot(color=YELLOW).move_to([44.614578 , 39.782053, 0]).scale(0.092)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(circle,axes)
        self.begin_ambient_camera_rotation(rate=0.1)
        dots = []
        lines = []
        for j in range(110 
        #len(lat_lon)-1
        ):
            i = j*30
            if i%3 == 1:
                dd = Dot(color = GREEN , point = [lat_lon[i][1], lat_lon[i][0], 0 ] ).scale(0.045)
                #ll= Line([lat_lon[i+1][1], lat_lon[i+1][0], 0 ],[lat_lon[i][1], lat_lon[i][0], 0 ] ,color = GREEN , stroke_width = 0.1)
            elif i%3 ==2:
                dd = Dot(color = BLUE , point = [lat_lon[i][1], lat_lon[i][0], 0 ] ).scale(0.045)
                #ll = Line([lat_lon[i+1][1], lat_lon[i+1][0], 0 ],[lat_lon[i][1], lat_lon[i][0], 0 ] ,color = BLUE , stroke_width = 0.1)
            
            elif i%3 ==0:
                dd = Dot(color = RED , point = [lat_lon[i][1], lat_lon[i][0], 0 ] ).scale(0.045)
                #ll = Line([lat_lon[i+1][1], lat_lon[i+1][0], 0 ],[lat_lon[i][1], lat_lon[i][0], 0 ] ,color = RED , stroke_width = 0.1)

            dots.append(dd)
            #lines.append(ll)
        
        
        
        
        
        
        
        for i in range(len(dots)//50):
            #self.play(frame.animate.move_to(dots[50*i+25].get_center()),
            #          run_time = 0.3)
            self.play(Create(dots[50*i] ),
                      Create(dots[50*i+1] ),
                      Create(dots[50*i+2] ),
                      Create(dots[50*i+3] ),
                      Create(dots[50*i+4] ),
                      Create(dots[50*i+5] ),
                      Create(dots[50*i+6] ),
                      Create(dots[50*i+7] ),
                      Create(dots[50*i+8] ),
                      Create(dots[50*i+9] ),
                      Create(dots[50*i+10] ),
                      Create(dots[50*i+11] ),
                      Create(dots[50*i+12] ),
                      Create(dots[50*i+13] ),
                      Create(dots[50*i+14] ),
                      Create(dots[50*i+15] ),
                      Create(dots[50*i+16] ),
                      Create(dots[50*i+17] ),
                      Create(dots[50*i+18] ),
                      Create(dots[50*i+19] ),
                      Create(dots[50*i+20] ),
                      Create(dots[50*i+21] ),
                      Create(dots[50*i+22] ),
                      Create(dots[50*i+23] ),
                      Create(dots[50*i+24] ),
                      Create(dots[50*i+25] ),
                      Create(dots[50*i+26] ),
                      Create(dots[50*i+27] ),
                      Create(dots[50*i+28] ),
                      Create(dots[50*i+29] ),
                      Create(dots[50*i+30] ),
                      Create(dots[50*i+31] ),
                      Create(dots[50*i+42] ),
                      Create(dots[50*i+43] ),
                      Create(dots[50*i+44] ),
                      Create(dots[50*i+45] ),
                      Create(dots[50*i+46] ),
                      Create(dots[50*i+47] ),
                      Create(dots[50*i+48] ),
                      Create(dots[50*i+49] ),
                      
                      
                      #Create(lines[50*i] ),
                      #Create(lines[50*i+1] ),
                      #Create(lines[50*i+2] ),
                      #Create(lines[50*i+3] ),
                      #Create(lines[50*i+4] ),
                      #Create(lines[50*i+5] ),
                      #Create(lines[50*i+6] ),
                      #Create(lines[50*i+7] ),
                      #Create(lines[50*i+8] ),
                      #Create(lines[50*i+9] ),
                      #Create(lines[50*i+10] ),
                      #Create(lines[50*i+11] ),
                      #Create(lines[50*i+12] ),
                      #Create(lines[50*i+13] ),
                      #Create(lines[50*i+14] ),
                      #Create(lines[50*i+15] ),
                      #Create(lines[50*i+16] ),
                      #Create(lines[50*i+17] ),
                      #Create(lines[50*i+18] ),
                      #Create(lines[50*i+19] ),
                      #Create(lines[50*i+20] ),
                      #Create(lines[50*i+21] ),
                      #Create(lines[50*i+22] ),
                      #Create(lines[50*i+23] ),
                      #Create(lines[50*i+24] ),
                      #Create(lines[50*i+25] ),
                      #Create(lines[50*i+26] ),
                      #Create(lines[50*i+27] ),
                      #Create(lines[50*i+28] ),
                      #Create(lines[50*i+29] ),
                      #Create(lines[50*i+30] ),
                      #Create(lines[50*i+31] ),
                      #Create(lines[50*i+42] ),
                      #Create(lines[50*i+43] ),
                      #Create(lines[50*i+44] ),
                      #Create(lines[50*i+45] ),
                      #Create(lines[50*i+46] ),
                      #Create(lines[50*i+47] ),
                      #Create(lines[50*i+48] ),
                      #Create(lines[50*i+49] ),
                      
                      run_time = 0.5)
        
        
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        
        self.wait(3)



class av (ZoomedScene):
# contributed by TheoremofBeethoven, www.youtube.com/c/TheoremofBeethoven
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.2,
            zoomed_display_height=5,
            zoomed_display_width=5,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )
    def construct(self):
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame
        frame.set_color(YELLOW)
        zoomed_display_frame.set_color(RED)
        zoomed_display.move_to([43.0,33,0])
        dirname = os.path.dirname(__file__)
        #self.camera.background_color = "#EEEEEE"
        #triangle = Triangle ()
        #triangle.scale(1)
        
        #self.play(Write(triangle))
        #self.wait(0.5)
        ir = SVGMobject(file_name = dirname +"/Iran.svg" , fill_opacity= 0.2 , stroke_color=WHITE , stroke_width=0.1 , stroke_opacity=100)
        ir.scale(8.17153527488908)
        #ir.move_to([53.16029934461913 , 31.63429934461913 , 0])
        self.play(Create(ir))
        self.wait(0.2)
        self.play(ir.animate.move_to([53.672524 ,32.410415 ,  0]) , 
                self.camera.frame.animate.scale(3.5).move_to([53.672524 ,32.410415,0]))
        #d = Dot(color=RED ).move_to([ 51.834168,34.505956,0]).scale(5.005)
        #d2 = Dot(color=YELLOW).move_to([44.614578 , 39.782053, 0]).scale(0.092)
        
        dots = []
        lines = []
        for j in range(202 
        #len(lat_lon)-1
        ):
            i = j*20
            if i%3 == 1:
                dd = Dot(color = GREEN , point = [lat_lon[i][1], lat_lon[i][0], 0 ] ).scale(0.045)
                #ll= Line([lat_lon[i+1][1], lat_lon[i+1][0], 0 ],[lat_lon[i][1], lat_lon[i][0], 0 ] ,color = GREEN , stroke_width = 0.1)
            elif i%3 ==2:
                dd = Dot(color = BLUE , point = [lat_lon[i][1], lat_lon[i][0], 0 ] ).scale(0.045)
                #ll = Line([lat_lon[i+1][1], lat_lon[i+1][0], 0 ],[lat_lon[i][1], lat_lon[i][0], 0 ] ,color = BLUE , stroke_width = 0.1)
            
            elif i%3 ==0:
                dd = Dot(color = RED , point = [lat_lon[i][1], lat_lon[i][0], 0 ] ).scale(0.045)
                #ll = Line([lat_lon[i+1][1], lat_lon[i+1][0], 0 ],[lat_lon[i][1], lat_lon[i][0], 0 ] ,color = RED , stroke_width = 0.1)

            dots.append(dd)
            #lines.append(ll)
        
        self.activate_zooming()
        
        
        
        
        scale_factor = [3, 3, 0]
        self.play(
            frame.animate.scale(scale_factor),
            zoomed_display.animate.scale(scale_factor).move_to((self.camera.frame.get_center()+self.camera.frame.get_right()*2)/3),
            
            )
        for i in range(len(dots)//50):
            self.play(frame.animate.move_to(dots[50*i+25].get_center()),
                      run_time = 0.3)
            self.play(Create(dots[50*i] ),
                      Create(dots[50*i+1] ),
                      Create(dots[50*i+2] ),
                      Create(dots[50*i+3] ),
                      Create(dots[50*i+4] ),
                      Create(dots[50*i+5] ),
                      Create(dots[50*i+6] ),
                      Create(dots[50*i+7] ),
                      Create(dots[50*i+8] ),
                      Create(dots[50*i+9] ),
                      Create(dots[50*i+10] ),
                      Create(dots[50*i+11] ),
                      Create(dots[50*i+12] ),
                      Create(dots[50*i+13] ),
                      Create(dots[50*i+14] ),
                      Create(dots[50*i+15] ),
                      Create(dots[50*i+16] ),
                      Create(dots[50*i+17] ),
                      Create(dots[50*i+18] ),
                      Create(dots[50*i+19] ),
                      Create(dots[50*i+20] ),
                      Create(dots[50*i+21] ),
                      Create(dots[50*i+22] ),
                      Create(dots[50*i+23] ),
                      Create(dots[50*i+24] ),
                      Create(dots[50*i+25] ),
                      Create(dots[50*i+26] ),
                      Create(dots[50*i+27] ),
                      Create(dots[50*i+28] ),
                      Create(dots[50*i+29] ),
                      Create(dots[50*i+30] ),
                      Create(dots[50*i+31] ),
                      Create(dots[50*i+42] ),
                      Create(dots[50*i+43] ),
                      Create(dots[50*i+44] ),
                      Create(dots[50*i+45] ),
                      Create(dots[50*i+46] ),
                      Create(dots[50*i+47] ),
                      Create(dots[50*i+48] ),
                      Create(dots[50*i+49] ),
                      
                      
                      #Create(lines[50*i] ),
                      #Create(lines[50*i+1] ),
                      #Create(lines[50*i+2] ),
                      #Create(lines[50*i+3] ),
                      #Create(lines[50*i+4] ),
                      #Create(lines[50*i+5] ),
                      #Create(lines[50*i+6] ),
                      #Create(lines[50*i+7] ),
                      #Create(lines[50*i+8] ),
                      #Create(lines[50*i+9] ),
                      #Create(lines[50*i+10] ),
                      #Create(lines[50*i+11] ),
                      #Create(lines[50*i+12] ),
                      #Create(lines[50*i+13] ),
                      #Create(lines[50*i+14] ),
                      #Create(lines[50*i+15] ),
                      #Create(lines[50*i+16] ),
                      #Create(lines[50*i+17] ),
                      #Create(lines[50*i+18] ),
                      #Create(lines[50*i+19] ),
                      #Create(lines[50*i+20] ),
                      #Create(lines[50*i+21] ),
                      #Create(lines[50*i+22] ),
                      #Create(lines[50*i+23] ),
                      #Create(lines[50*i+24] ),
                      #Create(lines[50*i+25] ),
                      #Create(lines[50*i+26] ),
                      #Create(lines[50*i+27] ),
                      #Create(lines[50*i+28] ),
                      #Create(lines[50*i+29] ),
                      #Create(lines[50*i+30] ),
                      #Create(lines[50*i+31] ),
                      #Create(lines[50*i+42] ),
                      #Create(lines[50*i+43] ),
                      #Create(lines[50*i+44] ),
                      #Create(lines[50*i+45] ),
                      #Create(lines[50*i+46] ),
                      #Create(lines[50*i+47] ),
                      #Create(lines[50*i+48] ),
                      #Create(lines[50*i+49] ),
                      
                      run_time = 0.5)
        
        
        
        self.wait(3)
class a1 (MovingCameraScene):
    def construct(self):
        dirname = os.path.dirname(__file__)
        self.camera.background_color = "#111111"
        dots = []
        for i in range(5):
            dd = Dot([50*i , 0 , 0])
            dots.append(dd)
        for i in range(5):
            self.play(Create(dots[i]))
        self.wait(3)