import cv2, math, os, time
import numpy as np

from schnell.app.dirutils import (
  isfile,
)

from .constants import (
  magenta, cyan, yellow, blue, red, green,
  tebal, default_loc,
)


# CAMERA_NO=-1
CAMERA_NO=0

def initialise(cam=CAMERA_NO):
  """
  cam selain no camera bisa juga filepath ke mp4 file.
  """
  cap = cv2.VideoCapture(cam)
  return cap


def initialise_wh(cam=-1, w=0, h=0):
  """
  cap, w, h = initialise_wh(w=1200, h=800)
  """
  capdevice = cv2.VideoCapture(cam)
  if w>0 and h>0:
    set_wh(capdevice, w, h)
  else:
    w, h = capdevice.get(3), capdevice.get(4)
  return capdevice, w, h


def set_wh(capdevice, w=900, h=600):
  capdevice.set(3, w)
  capdevice.set(4, h)


def get_w(capdevice):
  return capdevice.get(3)


def get_h(capdevice):
  return capdevice.get(4)


def get_wh(capdevice):
  return capdevice.get(3), capdevice.get(4)


def init_hands():
  import mediapipe as mp
  mpspace = mp.solutions.hands
  hands = mpspace.Hands()
  drawer = mp.solutions.drawing_utils
  return mpspace, hands, drawer


def show_wait(cvimage, title='Image'):
  cv2.imshow(title, cvimage)
  cv2.waitKey(1)


def show_wait_escape(cvimage, title='Image'):
  cv2.imshow(title, cvimage)
  k = cv2.waitKey(5) & 0xFF
  if k == 27:
    return True
  
  return False


def real_quit(cap):
  # Close the window
  cap.release()    
  # De-allocate any associated memory usage
  cv2.destroyAllWindows()


def draw_hand_landmarks(cvimage, m, h, d):
  imgRGB = cv2.cvtColor(cvimage, cv2.COLOR_BGR2RGB)
  results = h.process(imgRGB)
  # print(results.multi_hand_landmarks)
  if results.multi_hand_landmarks:
    for lm in results.multi_hand_landmarks:
      # draw.draw_landmarks(img, lm)
      d.draw_landmarks(cvimage, lm, m.HAND_CONNECTIONS)



def draw_hand_landmarks_wh(cvimage, m, h, d):
  imgRGB = cv2.cvtColor(cvimage, cv2.COLOR_BGR2RGB)
  results = h.process(imgRGB)
  # print(results.multi_hand_landmarks)
  if results.multi_hand_landmarks:
    for lm in results.multi_hand_landmarks:
      # draw.draw_landmarks(img, lm)
      d.draw_landmarks(cvimage, lm, m.HAND_CONNECTIONS)  


def doloop1(capdevice, m, h, d, success_callback, error_callback=lambda err: print(err)):
  while True:
    try:
      success, img = capdevice.read()
      success_callback(img, m, h, d)
      show_wait(img)
    except Exception as err:
      error_callback(err)


def doloop2(capdevice, m, h, d, success_callback, error_callback=lambda err: print(err)):
  while True:
    try:
      success, img = capdevice.read()

      success_callback(img, m, h, d)

      tulisan = f"{capdevice.get(3)} x {capdevice.get(4)}"

      cv2.putText(img, tulisan, default_loc, cv2.FONT_HERSHEY_PLAIN, 3, magenta, tebal)

      show_wait(img)
    except Exception as err:
      error_callback(err)


def quit_cv():
  cv2.destroyAllWindows()
  print('end')


def sample1():
  cap = initialise()
  m, h, d = init_hands()
  doloop2(cap, m, h, d, lambda a,b,c,d:draw_hand_landmarks(a,b,c,d))
  print('Quitting...')
  quit_cv()


def flip_image(cvimage, horiz_or_vert=1):
  cvimage = cv2.flip(cvimage, horiz_or_vert)
  return cvimage


def overlay_image(cvimage, filepath, start_height=0, image_height = 125, start_width=0, image_width = 1280):  
  overlay = cv2.imread(filepath)
  cvimage[start_height:image_height, start_width:image_width] = overlay


def jarix(jari):
  return jari[1]

def jariy(jari):
  return jari[2]

def jarixy(jari):
  return jari[1], jari[2]


def beda_tinggi(landmarks, jari, threshold=0):
  """
  pastikan jari adlh tip -> telunjuk0
  shg jari-2 adlh pip
  """
  ruas1 = landmarks[jari]
  ruas2 = landmarks[jari-2]

  # return abs(jariy(ruas1) - jariy(ruas2)) > threshold
  return jariy(ruas1) < jariy(ruas2)


def beda_lebar(landmarks, jari, kiri=True, front=True, threshold=0):
  """
  utk jari = jempol tip -> jempol0
  shg jari-1 adlh dip

  front adlh tapak menghadap kamera
  """
  ruas1 = landmarks[jari]
  ruas2 = landmarks[jari-1]

  # return abs(jarix(ruas1) - jarix(ruas2)) > threshold
  if kiri and front:
    return jarix(ruas1) > jarix(ruas2)
  elif not kiri and not front:
    return jarix(ruas1) > jarix(ruas2)
  else:
    return jarix(ruas1) < jarix(ruas2)


def ruas_in_rect(lm, x1, y1, x2, y2):
  dalam_x = jarix(lm) >= x1 and jarix(lm) <= x2
  dalam_y = jariy(lm) >= y1 and jariy(lm) <= y2
  if dalam_x and dalam_y:
    return True

  return False


def ruas_in_kotak(w, h, lm, no_kotak=0, nrows=5, ncols=5):
  # w,h = get_wh(capdevice)
  kw = int(w/nrows)
  kh = int(h/ncols)
  # x1,y1,x2,y2 = no_kotak*kw, no_kotak*h, (no_kotak+1)*kw, (no_kotak+1)*kh
  x1,y1 = no_kotak*kw, no_kotak*h
  x2,y2 = x1 + kw, y1 + kh
  # return x1,y1,x2,y2
  hasil = ruas_in_rect(lm, x1,y1,x2,y2)
  # print(f'w,h = {w},{h} => kw,kh = {kw},{kh} ruas_in_kotak {lm} ->{x1},{y1} {x2},{y2}')
  return hasil


def ruas_in_which_kotak(w, h, lm, nrows=5, ncols=5):
  """
  """
  # w,h = get_wh(capdevice)
  kw = int(w/nrows)
  kh = int(h/ncols)
  # x1,y1,x2,y2 = no_kotak*kw, no_kotak*h, (no_kotak+1)*kw, (no_kotak+1)*kh
  # return x1,y1,x2,y2
  # hasil = ruas_in_rect(lm, x1,y1,x2,y2)
  # print(f'w,h = {w},{h} => kw,kh = {kw},{kh} ruas_in_kotak {lm} ->{x1},{y1} {x2},{y2}')
  # return hasil

  # kotak 0,1,2,3,4 akan hasilkan row 0
  whichkotak = (lm[1] // kw) * nrows
  whichkotak += lm[2] // kh
  return whichkotak

def ruas_in_which_kotak_faster(lm, kw, kh, nrows):
  """
  """
  whichkotak = (lm[1] // kw) * nrows
  whichkotak += lm[2] // kh
  return whichkotak



def rect_center(x1,y1,x2,y2):
  return int((x1+x2)/2), int((y1+y2)/2)


def divide_screen(capdevice, cvimg, rows=5, cols=5, warna=yellow, tulisan=blue, thick=tebal):
  """
  cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)

  cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)

  cv2.putText(img, fps, default_loc, cv2.FONT_HERSHEY_PLAIN, 3, magenta, tebal)

  kotak1
  kw = w/nrows
  kh = h/ncols
  n=0
  x1,y1,x2,y2=n*kw,n*h,(n+1)*kw,(n+1)*kh
  """
  w,h = get_wh(capdevice)
  # lebar tiap row
  wrow = int(w/rows)
  # tinggi tiap col
  hcol = int(h/cols)
  # baris = [int(wrow * n) for n in range(rows)]
  # kolom = [int(hcol * n) for n in range(cols)]
  counter = 0
  for r in range(rows):
    for c in range(cols):
      x1, y1 = r*wrow, c*hcol
      x2, y2 = x1+wrow, y1+hcol
      center = rect_center(x1,y1,x2,y2)
      # cv2.rectangle(cvimg, (x1, y1), (x2, y2), drawColor, cv2.FILLED)
      cv2.rectangle(cvimg, (x1, y1), (x2, y2), warna, 2)
      cv2.putText(cvimg, str(counter), center, cv2.FONT_HERSHEY_PLAIN, 3, tulisan, tebal-1)
      counter += 1


def kotak(cvimg, x1,y1,x2,y2,warna=cyan,fill=True):
  """
  https://opencv-tutorial.readthedocs.io/en/latest/draw/draw.html
  contoh bikin volume yg bergerak ke atas (y berkurang)
  x1min = 50
  y1min = 150
  x2max = 100
  y2max = 600
  kotak(cvimg, (x1min, y1min), (x2max, y2max), green, False)
  kotak(cvimg, (x1min, int(dynamicValue)), (x2max, y2max), green, True)
  """
  filled = cv2.FILLED if fill else 2
  cv2.rectangle(cvimg, (x1, y1), (x2, y2), warna, filled)


def bulat(cvimg, x1,y1,radius=15,warna=cyan,fill=True):
  filled = cv2.FILLED if fill else 2
  cv2.circle(cvimg, (x1, y1), radius, warna, filled)


def garis(cvimg, x1,y1,x2,y2,warna=cyan,tebal=3):
  cv2.line(cvimg, (x1,y1), (x2,y2), warna, tebal)


def center(x1,y1,x2,y2):
  """
  nama tengah sudah dipake utk jari
  """
  return (x1+x2)//2,(y1+y2)//2


def jarak(x1,y1,x2,y2):
  return math.hypot(x2-x1, y2-y1)


def convert_value(value, range1=[0,100], range2=[0,50]):
  """
  contoh:
  range_jarak_jempol_telunjuk = [50,300]
  volume = convert_value(val, range_jarak_jempol_telunjuk, [minVol, maxVol])
  volumeBar = convert_value(val, range_jarak_jempol_telunjuk, [400, 150])
  volumePercent = convert_value(val, range_jarak_jempol_telunjuk, [0, 100])
  """
  return np.interp(value, range1, range2)


def calc_fps(prevTime):
  currentTime = time.time()
  fps = 1 / (currentTime - prevTime) # float
  prevTime = currentTime
  return currentTime, prevTime, int(fps)


def lm_xy(lmList, target, delta_x=0, delta_y=0):
  """
  lmList[target] = (target_index, target_x, target_y)
  """
  return lmList[target][1]+delta_x, lmList[target][2]+delta_y


def empty_image(w, h, greyscale=False):
  if greyscale:
    img = np.zeros((w,h), np.uint8)
  else:
    img = np.zeros((w,h, 3), np.uint8)
  
  # cv2.imshow('RGB', img)
  return img


def show_image(cvimg, title='Image'):
  cv2.imshow(title, cvimg)


def save_image(cvimg, filepath='gambar.jpg'):
  cv2.imwrite(filepath, cvimg)


def edge_detect():
  """
  https://www.geeksforgeeks.org/python-program-to-detect-the-edges-of-an-image-using-opencv-sobel-edge-detection/?ref=rp
  https://www.geeksforgeeks.org/real-time-edge-detection-using-opencv-python/?ref=rp
  """
  pass


def test_camera(camera_no=0):
  vid = cv2.VideoCapture(camera_no)
  while(True):    
    # Capture the video frame by frame
    ret, frame = vid.read()
    # Display the resulting frame
    cv2.imshow('frame', frame)    
    # 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  # After the loop release the cap object
  vid.release()
  # Destroy all the windows
  cv2.destroyAllWindows()
