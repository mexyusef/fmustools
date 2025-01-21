import re
from schnell.app.videoutils import reverse_mp4, merge_videos, merge_videos_to_gif
from schnell.app.videoutils2 import add_overlay2, add_overlay3, write_shots, screenshots_grid, create_image_grid3, draw_rectangles_on_video
from schnell.app.videoutils3 import video_to_images, video_to_clip, video_to_clip_seconds, video_to_images_seconds
from schnell.app.videoutils4 import images_to_video
from schnell.app.mediautils import internal_video_viewer
from schnell.app.dirutils import bongkar


def reverse_video(request):
    '''
    /vidutils)rev|path
    /vidutils)rev|path|out
    /vidutils)rev|path|fps
    /vidutils)rev|path|out|fps
    '''
    parts = request.split('|')
    if len(parts)==2:
        _, video_inputpath = parts
        reverse_mp4(video_inputpath)
    elif len(parts)==3:
        _, video_inputpath, video_outputpath = parts
        if re.match(r'(\d+(\.\d+)?)', video_outputpath):
            fps = float(video_outputpath)
            reverse_mp4(video_inputpath, fps = fps)
        else:
            reverse_mp4(video_inputpath, video_output = video_outputpath)
    elif len(parts)==4:
        _, video_inputpath, video_outputpath, fps = parts
        reverse_mp4(video_inputpath, video_outputpath, float(fps))


def merge_video(request):
    '''
    /vidutils)merge|path1,path2,path3
    '''
    paths = request.removeprefix('merge').strip().removeprefix('|').strip()
    videos = [i.strip() for i in paths.split(',')]
    merge_videos(videos)


def video_to_gif(request):
    '''
    /vidutils)2gif|gifoutput|path1,path2,path3
    '''
    gifoutput, paths = [e.strip() for e in request.removeprefix('2gif').strip().removeprefix('|').strip().split('|',1)]
    videos = [i.strip() for i in paths.split(',')]
    merge_videos_to_gif(videos, gifoutput)



def image_to_video(request):
    '''
    /vidutils)
        img2vid|
            output|img1,img2,img3
            output|img1,img2,img3|fps
            output|>inputfolder
            output|>inputfolder|fps
    '''
    request = request.removeprefix('img2vid|').strip()
    print('img2vid => request:', request)
    parts = [e.strip() for e in request.split('|')]
    if request.count('|')==2:
        print("if request.count('|')==2:")
        vidoutput, vidinput, fps = parts
        extra_args = {}
        if ',' in fps:
            print("if ',' in fps:")
            for e in [e.strip() for e in fps.split(',')]:
                if '.' in e:
                    extra_args['fps'] = float(e)
                else:
                    extra_args['delay'] = int(e)
        else:
            if '.' in fps:
                extra_args['fps'] = float(fps)
            else:
                extra_args['delay'] = int(fps)
        if vidinput.startswith('>'):
            print("if vidinput.startswith('>'):")
            image_folder = vidinput.removeprefix('>')
            images_to_video(vidoutput, image_folder=image_folder, **extra_args)
        else:
            print('else vidinput.startswith('>')::')
            list_of_images = [e.strip() for e in vidinput.split(',')]
            images_to_video(vidoutput, list_of_images=list_of_images, fps=fps)
    else:
        vidoutput, vidinput = parts
        if vidinput.startswith('>'):
            image_folder = vidinput.removeprefix('>')
            images_to_video(vidoutput, image_folder=image_folder)
        else:
            list_of_images = [e.strip() for e in vidinput.split(',')]
            images_to_video(vidoutput, list_of_images=list_of_images)


def video_image_by_frames(request):
    '''
    video_to_images(video_input, start_frame=1, end_frame=-1, output_dir=None)
    /vidutils)images|c:/fr/pertama.mp4
    /vidutils)images|c:/fr/pertama.mp4|10,30
    /vidutils)images|c:/fr/pertama.mp4|10,30|output_images
    /vidutils)images|*c:/fr/pertama.mp4
    '''
    print_frameno = False
    request = request.removeprefix('images|')
    if request.startswith('*'):
        request = request.removeprefix('*').strip()
        print_frameno = True
    if '|' in request:
        if request.count('|')==2: # /vidutils)images|c:/fr/pertama.mp4|10,30|output_dir
            vidinput, frames, vidoutput = [e.strip() for e in request.split('|')]
            start, end = [int(e.strip()) for e in frames.split(',')]
            params = [vidinput, start, end, vidoutput]
            video_to_images(*params, print_frameno=print_frameno)
        else: # /vidutils)images|c:/fr/pertama.mp4|10,30
            vidinput, frames = [e.strip() for e in request.split('|')]
            start, end = [int(e.strip()) for e in frames.split(',')]
            params = [vidinput, start, end]
            video_to_images(*params, print_frameno=print_frameno)
    else: # /vidutils)images|c:/fr/pertama.mp4
        video_to_images(request, print_frameno=print_frameno)


def video_image_by_seconds(request):
    '''
    video_to_images_seconds(video_input, start_second=0, end_second=-1)
    /vidutils)images2|c:/fr/pertama.mp4
    /vidutils)images2|c:/fr/pertama.mp4|10,30
    /vidutils)images2|c:/fr/pertama.mp4|10,30|output_images
    '''
    request = request.removeprefix('images2|')
    print_frameno = False
    if request.startswith('*'):
        request = request.removeprefix('*').strip()
        print_frameno = True
    if '|' in request:
        # if request.count('|')==2: # /vidutils)images2|c:/fr/pertama.mp4|10,30|output_dir
        # 	vidinput, frames, vidoutput = [e.strip() for e in request.split('|')]
        # 	start, end = [int(e.strip()) for e in frames.split(',')]
        # 	params = [vidinput, start, end, vidoutput]
        # 	video_to_images_seconds(*params)
        # else: # /vidutils)images|c:/fr/pertama.mp4|10,30
            vidinput, frames = [e.strip() for e in request.split('|')]
            start, end = [int(e.strip()) for e in frames.split(',')]
            params = [vidinput, start, end]
            video_to_images_seconds(*params, print_frameno=print_frameno)
    else: # /vidutils)images|c:/fr/pertama.mp4
        video_to_images_seconds(request, print_frameno=print_frameno)


def video_clip_by_frames(request):
    '''
    video_to_clip(video_input, start_frame=1, end_frame=-1, output_dir=None)
    /vidutils)clip|c:/fr/pertama.mp4
    /vidutils)clip|c:/fr/pertama.mp4|10,30
    /vidutils)clip|c:/fr/pertama.mp4|10,30|output_images
    '''
    request = request.removeprefix('clip|')
    if '|' in request:
        if request.count('|')==2: # /vidutils)clip|c:/fr/pertama.mp4|10,30|output_dir => c:/fr/pertama.mp4|10,30|output_dir
            vidinput, frames, vidoutput = [e.strip() for e in request.split('|')]
            start, end = [int(e.strip()) for e in frames.split(',')]
            params = [vidinput, start, end, vidoutput]
            video_to_clip(*params)
        else: # /vidutils)clip|c:/fr/pertama.mp4|10,30 => c:/fr/pertama.mp4|10,30
            vidinput, frames = [e.strip() for e in request.split('|')]
            start, end = [int(e.strip()) for e in frames.split(',')]
            params = [vidinput, start, end]
            video_to_clip(*params)
    else: # /vidutils)clip|c:/fr/pertama.mp4
        video_to_clip(request)


def video_clip_by_seconds(request):
    '''
    video_to_clip_seconds(video_input, start_second=0, end_second=-1)
    /vidutils)clip2|c:/fr/pertama.mp4
    /vidutils)clip2|c:/fr/pertama.mp4|10,30
    /vidutils)clip2|c:/fr/pertama.mp4|10,30|output_images
    '''
    request = request.removeprefix('clip2|')
    if '|' in request:
        # if request.count('|')==2: # /vidutils)clip2|c:/fr/pertama.mp4|10,30|output_dir
        # 	vidinput, frames, vidoutput = [e.strip() for e in request.split('|')]
        # 	start, end = [int(e.strip()) for e in frames.split(',')]
        # 	params = [vidinput, start, end, vidoutput]
        # 	video_to_clip_seconds(*params)
        # else: # /vidutils)clip|c:/fr/pertama.mp4|10,30
            vidinput, frames = [e.strip() for e in request.split('|')]
            start, end = [int(e.strip()) for e in frames.split(',')]
            params = [vidinput, start, end]
            video_to_clip_seconds(*params)
    else: # /vidutils)clip|c:/fr/pertama.mp4
        video_to_clip_seconds(request)


def video_play(request):
    request = request.removeprefix('play|').strip()
    if request:        
        internal_video_viewer(request)

def video_screenshot(request):
    '''
    /vidutils)shots|videopath
    /vidutils)shots|videopath|4
    '''
    code = request.removeprefix('shots').strip().removeprefix('|').strip()
    if '|' in code:
        videopath, jumlahshots = [e.strip() for e in code.split('|')]
        videopath = bongkar(videopath)
        write_shots(videopath, int(jumlahshots))
    else:
        videopath = bongkar(code)
        write_shots(videopath)


def video_draw_rectangle_on_video(request):
    '''
    /vidutils)rect|inputpath|specs
    /vidutils)rect|inputpath|specs|outputpath
    specs = x,y,w,h
    specs = x,y,w,h,color
    specs = x,y,w,h,color,thickness
    specs = x,y,w,h,color,thickness,fill
    '''
    # draw_rectangles_on_video(input_file, x_percent=0.25, y_percent=0.25, w_percent=0.5, h_percent=0.5, output_file=None, color=(0,255,0), thickness=1, fill=True)
    request = request.removeprefix('rect').strip().removeprefix('|').strip()
    # voutput = None
    allspecs = {
        'x_percent':0.25, 
        'y_percent':0.25, 
        'w_percent':0.5, 
        'h_percent':0.5, 
        'output_file':None, 
        'color':'red', 
        # 'thickness':2,
        'fill': True,
    }
    if '|' in request:
        if request.count('|')==2: # /vidutils)rect|inputpath|specs|outputpath
            vinput, specs, voutput = [e.strip() for e in request.split('|')]
            allspecs['output_file']=voutput
        else: # /vidutils)rect|inputpath|specs
            vinput, specsstr = [e.strip() for e in request.split('|')]
            specs = [e.strip() for e in specsstr.split(',')]
            if len(specs)==4:
                x,y,w,h=[float(e) for e in specs]
                allspecs['x_percent']=x
                allspecs['y_percent']=y
                allspecs['w_percent']=w
                allspecs['h_percent']=h
            elif len(specs)==5:
                x,y,w,h,color=specs
                allspecs['x_percent']=float(x)
                allspecs['y_percent']=float(y)
                allspecs['w_percent']=float(w)
                allspecs['h_percent']=float(h)
                allspecs['color']=color
            elif len(specs)==6:
                x,y,w,h,color,fill=specs
                allspecs['x_percent']=float(x)
                allspecs['y_percent']=float(y)
                allspecs['w_percent']=float(w)
                allspecs['h_percent']=float(h)
                allspecs['color']=color
                allspecs['fill']=bool(fill)
            # elif len(specs)==7:
            # 	x,y,w,h,color,thick,fill=specs
            # 	allspecs['x_percent']=float(x)
            # 	allspecs['y_percent']=float(y)
            # 	allspecs['w_percent']=float(w)
            # 	allspecs['h_percent']=float(h)
            # 	allspecs['color']=color
            # 	allspecs['thickness']=int(thick)
            # 	allspecs['fill']=bool(fill)
    else:
        vinput = request
    print(f'draw_rectangles_on_video => allspecs =', allspecs)
    draw_rectangles_on_video(vinput, **allspecs)



def video_create_grid(request):
    '''
    /vidutils)grid|imgpath1,imgpath2,imgpath3
    /vidutils)grid|imgpath1,imgpath2,imgpath3|0.3
    '''
    request = request.removeprefix('grid|').strip()
    if '|' in request:
        images, scale = [e.strip() for e in request.split('|')]
        create_image_grid3([e.strip() for e in images.split(',')], float(scale))
    else:
        create_image_grid3([e.strip() for e in request.split(',')])


def video_create_grid_screenshot(request):
    '''
    /vidutils)shotgrid|videopath
    /vidutils)shotgrid|videopath|4
    /vidutils)shotgrid|videopath|4,.25
    /vidutils)shotgrid|videopath|4,.25|outputpath
    '''
    code = request.removeprefix('shotgrid').strip().removeprefix('|').strip()
    if '|' in code:
        # videopath, jumlahshots = [e.strip() for e in code.split('|')]
        # videopath = bongkar(videopath)
        # write_shots(videopath, int(jumlahshots))
        video_output = None
        scale = 0.25
        numshots = 8
        if code.count('|')==2: # jk ada numshots/scale + outpath
            video_input, spec, video_output = [e.strip() for e in code.split('|')]
            if ',' in spec:
                for item in [e.strip() for e in spec.split(',')]:
                    if '.' in item:
                        scale = float(item)
                    else:
                        numshots = int(item)
        else:
            video_input, spec = [e.strip() for e in code.split('|')]
            if ',' in spec:
                for item in [e.strip() for e in spec.split(',')]:
                    if '.' in item:
                        scale = float(item)
                    else:
                        numshots = int(item)
        videopath = bongkar(video_input)
        screenshots_grid(videopath, numshots, scale, video_output)
    else:
        videopath = bongkar(code)
        write_shots(videopath)

def vidutils(code):
    request = code.removeprefix('vidutils)').strip()

    if request:
        request = request.strip()
        if request.startswith('['):
            pass
        else:
            if request.startswith('rev'):
                # '''
                # /vidutils)rev|path
                # /vidutils)rev|path|out
                # /vidutils)rev|path|fps
                # /vidutils)rev|path|out|fps
                # '''
                # parts = request.split('|')
                # if len(parts)==2:
                #     _, video_inputpath = parts
                #     reverse_mp4(video_inputpath)
                # elif len(parts)==3:
                #     _, video_inputpath, video_outputpath = parts
                #     if re.match(r'(\d+(\.\d+)?)', video_outputpath):
                #         fps = float(video_outputpath)
                #         reverse_mp4(video_inputpath, fps = fps)
                #     else:
                #         reverse_mp4(video_inputpath, video_output = video_outputpath)
                # elif len(parts)==4:
                #     _, video_inputpath, video_outputpath, fps = parts
                #     reverse_mp4(video_inputpath, video_outputpath, float(fps))
                reverse_video(request)

            elif request.startswith('merge'):
                merge_video(request)

            elif request.startswith('2gif'):
                # '''
                # /vidutils)2gif|gifoutput|path1,path2,path3
                # '''
                # gifoutput, paths = [e.strip() for e in request.removeprefix('2gif').strip().removeprefix('|').strip().split('|',1)]
                # videos = [i.strip() for i in paths.split(',')]
                # merge_videos_to_gif(videos, gifoutput)
                video_to_gif(request)

            elif request.startswith('img2vid'):
                # '''
                # /vidutils)
                #     img2vid|
                #         output|img1,img2,img3
                #         output|img1,img2,img3|fps
                #         output|>inputfolder
                #         output|>inputfolder|fps
                # '''
                # request = request.removeprefix('img2vid|').strip()
                # print('img2vid => request:', request)
                # parts = [e.strip() for e in request.split('|')]
                # if request.count('|')==2:
                #     print("if request.count('|')==2:")
                #     vidoutput, vidinput, fps = parts
                #     extra_args = {}
                #     if ',' in fps:
                #         print("if ',' in fps:")
                #         for e in [e.strip() for e in fps.split(',')]:
                #             if '.' in e:
                #                 extra_args['fps'] = float(e)
                #             else:
                #                 extra_args['delay'] = int(e)
                #     else:
                #         if '.' in fps:
                #             extra_args['fps'] = float(fps)
                #         else:
                #             extra_args['delay'] = int(fps)
                #     if vidinput.startswith('>'):
                #         print("if vidinput.startswith('>'):")
                #         image_folder = vidinput.removeprefix('>')
                #         images_to_video(vidoutput, image_folder=image_folder, **extra_args)
                #     else:
                #         print('else vidinput.startswith('>')::')
                #         list_of_images = [e.strip() for e in vidinput.split(',')]
                #         images_to_video(vidoutput, list_of_images=list_of_images, fps=fps)
                # else:
                #     vidoutput, vidinput = parts
                #     if vidinput.startswith('>'):
                #         image_folder = vidinput.removeprefix('>')
                #         images_to_video(vidoutput, image_folder=image_folder)
                #     else:
                #         list_of_images = [e.strip() for e in vidinput.split(',')]
                #         images_to_video(vidoutput, list_of_images=list_of_images)
                image_to_video(request)

            elif request.startswith('ovl'):
                '''
                /vidutils)ovl|image_to_overlay|videopath
                /vidutils)ovl|image_to_overlay|videopath|x,y
                /vidutils)ovl|image_to_overlay|videopath|scale = 0-100
                /vidutils)ovl|image_to_overlay|videopath|trans = 0.0-1.0
                '''
                request = request.removeprefix('ovl|').strip()
                # image_to_overlay, videopath = [e.strip() for e in request.removeprefix('ovl').strip().removeprefix('|').strip().split('|',1)]
                if request.count('|')==2: # a|b|c
                    image_to_overlay, videopath, xy = [e.strip() for e in request.split('|')]
                    if ',' in xy:
                        if xy.count(',')==1: # ...|x,y
                            x,y = [float(e.strip()) for e in xy.split(',')]
                            add_overlay2(videopath, image_to_overlay, x=x, y=y)
                        elif xy.count(',')==2: # ...|x,y,scale
                            x,y,scale = [float(e.strip()) for e in xy.split(',')]
                            add_overlay3(videopath, image_to_overlay, x=x,y=y,scale_percent=int(scale))
                        elif xy.count(',')==3: # ...|x,y,scale,trans
                            x,y,scale,trans = [float(e.strip()) for e in xy.split(',')]
                            add_overlay3(videopath, image_to_overlay, x=x,y=y,scale_percent=int(scale), transparency=trans)
                    elif '.' in xy:
                        # 0.0-1.0 = trans
                        add_overlay3(videopath, image_to_overlay, transparency=float(xy))
                    else:
                        # 0-100 = scale
                        add_overlay2(videopath, image_to_overlay, scale_percent=int(xy))
                else: # a|b
                    image_to_overlay, videopath = [e.strip() for e in request.split('|')]
                    add_overlay2(videopath, image_to_overlay)

            elif request.startswith('shots'):
                # '''
                # /vidutils)shots|videopath
                # /vidutils)shots|videopath|4
                # '''
                # code = request.removeprefix('shots').strip().removeprefix('|').strip()
                # if '|' in code:
                #     videopath, jumlahshots = [e.strip() for e in code.split('|')]
                #     videopath = bongkar(videopath)
                #     write_shots(videopath, int(jumlahshots))
                # else:
                #     videopath = bongkar(code)
                #     write_shots(videopath)
                video_screenshot(request)

            elif request.startswith('grid'):
                # '''
                # /vidutils)grid|imgpath1,imgpath2,imgpath3
                # /vidutils)grid|imgpath1,imgpath2,imgpath3|0.3
                # '''
                # request = request.removeprefix('grid|').strip()
                # if '|' in request:
                #     images, scale = [e.strip() for e in request.split('|')]
                #     create_image_grid3([e.strip() for e in images.split(',')], float(scale))
                # else:
                #     create_image_grid3([e.strip() for e in request.split(',')])
                video_create_grid(request)

            elif request.startswith('shotgrid'):
                # '''
                # /vidutils)shotgrid|videopath
                # /vidutils)shotgrid|videopath|4
                # /vidutils)shotgrid|videopath|4,.25
                # /vidutils)shotgrid|videopath|4,.25|outputpath
                # '''
                # code = request.removeprefix('shotgrid').strip().removeprefix('|').strip()
                # if '|' in code:
                #     # videopath, jumlahshots = [e.strip() for e in code.split('|')]
                #     # videopath = bongkar(videopath)
                #     # write_shots(videopath, int(jumlahshots))
                #     video_output = None
                #     scale = 0.25
                #     numshots = 8
                #     if code.count('|')==2: # jk ada numshots/scale + outpath
                #         video_input, spec, video_output = [e.strip() for e in code.split('|')]
                #         if ',' in spec:
                #             for item in [e.strip() for e in spec.split(',')]:
                #                 if '.' in item:
                #                     scale = float(item)
                #                 else:
                #                     numshots = int(item)
                #     else:
                #         video_input, spec = [e.strip() for e in code.split('|')]
                #         if ',' in spec:
                #             for item in [e.strip() for e in spec.split(',')]:
                #                 if '.' in item:
                #                     scale = float(item)
                #                 else:
                #                     numshots = int(item)
                #     videopath = bongkar(video_input)
                #     screenshots_grid(videopath, numshots, scale, video_output)
                # else:
                #     videopath = bongkar(code)
                #     write_shots(videopath)
                video_create_grid_screenshot(request)

            elif request.startswith('rect'):
                # '''
                # /vidutils)rect|inputpath|specs
                # /vidutils)rect|inputpath|specs|outputpath
                # specs = x,y,w,h
                # specs = x,y,w,h,color
                # specs = x,y,w,h,color,thickness
                # specs = x,y,w,h,color,thickness,fill
                # '''
                # # draw_rectangles_on_video(input_file, x_percent=0.25, y_percent=0.25, w_percent=0.5, h_percent=0.5, output_file=None, color=(0,255,0), thickness=1, fill=True)
                # request = request.removeprefix('rect').strip().removeprefix('|').strip()
                # # voutput = None
                # allspecs = {
                #     'x_percent':0.25, 
                #     'y_percent':0.25, 
                #     'w_percent':0.5, 
                #     'h_percent':0.5, 
                #     'output_file':None, 
                #     'color':'red', 
                #     # 'thickness':2,
                #     'fill': True,
                # }
                # if '|' in request:
                #     if request.count('|')==2: # /vidutils)rect|inputpath|specs|outputpath
                #         vinput, specs, voutput = [e.strip() for e in request.split('|')]
                #         allspecs['output_file']=voutput
                #     else: # /vidutils)rect|inputpath|specs
                #         vinput, specsstr = [e.strip() for e in request.split('|')]
                #         specs = [e.strip() for e in specsstr.split(',')]
                #         if len(specs)==4:
                #             x,y,w,h=[float(e) for e in specs]
                #             allspecs['x_percent']=x
                #             allspecs['y_percent']=y
                #             allspecs['w_percent']=w
                #             allspecs['h_percent']=h
                #         elif len(specs)==5:
                #             x,y,w,h,color=specs
                #             allspecs['x_percent']=float(x)
                #             allspecs['y_percent']=float(y)
                #             allspecs['w_percent']=float(w)
                #             allspecs['h_percent']=float(h)
                #             allspecs['color']=color
                #         elif len(specs)==6:
                #             x,y,w,h,color,fill=specs
                #             allspecs['x_percent']=float(x)
                #             allspecs['y_percent']=float(y)
                #             allspecs['w_percent']=float(w)
                #             allspecs['h_percent']=float(h)
                #             allspecs['color']=color
                #             allspecs['fill']=bool(fill)
                #         # elif len(specs)==7:
                #         # 	x,y,w,h,color,thick,fill=specs
                #         # 	allspecs['x_percent']=float(x)
                #         # 	allspecs['y_percent']=float(y)
                #         # 	allspecs['w_percent']=float(w)
                #         # 	allspecs['h_percent']=float(h)
                #         # 	allspecs['color']=color
                #         # 	allspecs['thickness']=int(thick)
                #         # 	allspecs['fill']=bool(fill)
                # else:
                #     vinput = request
                # print(f'draw_rectangles_on_video => allspecs =', allspecs)
                # draw_rectangles_on_video(vinput, **allspecs)
                video_draw_rectangle_on_video(request)

            elif request.startswith('play'):
                # request = request.removeprefix('play|').strip()
                # if request:
                #     from schnell.app.mediautils import internal_video_viewer
                #     internal_video_viewer(request)
                video_play(request)

            elif request.startswith('images|'):
                # '''
                # video_to_images(video_input, start_frame=1, end_frame=-1, output_dir=None)
                # /vidutils)images|c:/fr/pertama.mp4
                # /vidutils)images|c:/fr/pertama.mp4|10,30
                # /vidutils)images|c:/fr/pertama.mp4|10,30|output_images
                # /vidutils)images|*c:/fr/pertama.mp4
                # '''
                # print_frameno = False
                # request = request.removeprefix('images|')
                # if request.startswith('*'):
                #     request = request.removeprefix('*').strip()
                #     print_frameno = True
                # if '|' in request:
                #     if request.count('|')==2: # /vidutils)images|c:/fr/pertama.mp4|10,30|output_dir
                #         vidinput, frames, vidoutput = [e.strip() for e in request.split('|')]
                #         start, end = [int(e.strip()) for e in frames.split(',')]
                #         params = [vidinput, start, end, vidoutput]
                #         video_to_images(*params, print_frameno=print_frameno)
                #     else: # /vidutils)images|c:/fr/pertama.mp4|10,30
                #         vidinput, frames = [e.strip() for e in request.split('|')]
                #         start, end = [int(e.strip()) for e in frames.split(',')]
                #         params = [vidinput, start, end]
                #         video_to_images(*params, print_frameno=print_frameno)
                # else: # /vidutils)images|c:/fr/pertama.mp4
                #     video_to_images(request, print_frameno=print_frameno)
                video_image_by_frames(request)

            elif request.startswith('images2'):
                # '''
                # video_to_images_seconds(video_input, start_second=0, end_second=-1)
                # /vidutils)images2|c:/fr/pertama.mp4
                # /vidutils)images2|c:/fr/pertama.mp4|10,30
                # /vidutils)images2|c:/fr/pertama.mp4|10,30|output_images
                # '''
                # request = request.removeprefix('images2|')
                # print_frameno = False
                # if request.startswith('*'):
                #     request = request.removeprefix('*').strip()
                #     print_frameno = True
                # if '|' in request:
                #     # if request.count('|')==2: # /vidutils)images2|c:/fr/pertama.mp4|10,30|output_dir
                #     # 	vidinput, frames, vidoutput = [e.strip() for e in request.split('|')]
                #     # 	start, end = [int(e.strip()) for e in frames.split(',')]
                #     # 	params = [vidinput, start, end, vidoutput]
                #     # 	video_to_images_seconds(*params)
                #     # else: # /vidutils)images|c:/fr/pertama.mp4|10,30
                #         vidinput, frames = [e.strip() for e in request.split('|')]
                #         start, end = [int(e.strip()) for e in frames.split(',')]
                #         params = [vidinput, start, end]
                #         video_to_images_seconds(*params, print_frameno=print_frameno)
                # else: # /vidutils)images|c:/fr/pertama.mp4
                #     video_to_images_seconds(request, print_frameno=print_frameno)
                video_image_by_seconds(request)

            elif request.startswith('clip|'):
                # '''
                # video_to_clip(video_input, start_frame=1, end_frame=-1, output_dir=None)
                # /vidutils)clip|c:/fr/pertama.mp4
                # /vidutils)clip|c:/fr/pertama.mp4|10,30
                # /vidutils)clip|c:/fr/pertama.mp4|10,30|output_images
                # '''
                # request = request.removeprefix('clip|')
                # if '|' in request:
                #     if request.count('|')==2: # /vidutils)clip|c:/fr/pertama.mp4|10,30|output_dir => c:/fr/pertama.mp4|10,30|output_dir
                #         vidinput, frames, vidoutput = [e.strip() for e in request.split('|')]
                #         start, end = [int(e.strip()) for e in frames.split(',')]
                #         params = [vidinput, start, end, vidoutput]
                #         video_to_clip(*params)
                #     else: # /vidutils)clip|c:/fr/pertama.mp4|10,30
                #         vidinput, frames = [e.strip() for e in request.split('|')]
                #         start, end = [int(e.strip()) for e in frames.split(',')]
                #         params = [vidinput, start, end]
                #         video_to_clip(*params)
                # else: # /vidutils)clip|c:/fr/pertama.mp4
                #     video_to_clip(request)
                video_clip_by_frames(request)

            elif request.startswith('clip2'):
                # '''
                # video_to_clip_seconds(video_input, start_second=0, end_second=-1)
                # /vidutils)clip2|c:/fr/pertama.mp4
                # /vidutils)clip2|c:/fr/pertama.mp4|10,30
                # /vidutils)clip2|c:/fr/pertama.mp4|10,30|output_images
                # '''
                # request = request.removeprefix('clip2|')
                # if '|' in request:
                #     # if request.count('|')==2: # /vidutils)clip2|c:/fr/pertama.mp4|10,30|output_dir
                #     # 	vidinput, frames, vidoutput = [e.strip() for e in request.split('|')]
                #     # 	start, end = [int(e.strip()) for e in frames.split(',')]
                #     # 	params = [vidinput, start, end, vidoutput]
                #     # 	video_to_clip_seconds(*params)
                #     # else: # /vidutils)clip|c:/fr/pertama.mp4|10,30
                #         vidinput, frames = [e.strip() for e in request.split('|')]
                #         start, end = [int(e.strip()) for e in frames.split(',')]
                #         params = [vidinput, start, end]
                #         video_to_clip_seconds(*params)
                # else: # /vidutils)clip|c:/fr/pertama.mp4
                #     video_to_clip_seconds(request)
                video_clip_by_seconds(request)
