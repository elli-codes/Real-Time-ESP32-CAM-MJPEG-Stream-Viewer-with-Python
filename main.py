from tkinter import*
import requests
from PIL import Image,ImageTk
from io import BytesIO

class my_class:
    def __init__(self):
        self.buffer=b""
        self.root=Tk()
        self.root.title("Real-Time ESP32-CAM Video Streaming")
        self.root.geometry("400x350+550+300")
        self.txt1= Label(self.root)
        self.txt1.pack()
        self.txt1.place(x=50,y=50)
        
        result=requests.get("http://192.168.137.60:81/stream" , stream=True)
    
        print(result.status_code)
        print (result.headers)
        
        self.chunks=result.iter_content(chunk_size=8192)
        print(type(self.chunks))
        self.fr()
    def fr(self):
            chunks=next(self.chunks)
            self.buffer+=chunks
            
            
            position=self.buffer.find(b"\r\n\r\n")
            
            if (position==-1):
                self.root.after(1,self.fr)
                return
            else:
                header=self.buffer[:position]
                
            content=header.find(b"Content-Length:")
            a=len(b"Content-Length:")
            number_start = content + a
            end = header.find(b"\r\n", number_start)
            content_num=header[number_start:end]
            content_number=int (content_num)
            jpeg=self.buffer[position+4:]
            jpeg_size=len(jpeg)
            
            if (jpeg_size < content_number):
                 self.root.after(1, self.fr)
                 return
            if (jpeg_size == content_number):
               part1=jpeg[:content_number]
               image_data = BytesIO(part1)
               image=Image.open(image_data)
               #print (type(image))
               photo = ImageTk.PhotoImage(image)
               self.img=photo
               self.txt1.config(image=self.img)
               self.buffer=b""
               self.root.after(1, self.fr)

               
            if (jpeg_size> content_number):
                
                part1=jpeg[:content_number]
                image_data = BytesIO(part1)
                image=Image.open(image_data)
                photo = ImageTk.PhotoImage(image)
                self.img=photo
                self.txt1.config(image=self.img)

                
                
                end_frame=(position+4)+content_number
                self.buffer=self.buffer[end_frame:]
                self.root.after(1, self.fr)
                
           

def main():
    x=my_class()
    x.root.mainloop()

if __name__ =="__main__":main()   
