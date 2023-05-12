from PIL import Image
import os
from pathlib import Path

BASE_DIR = str(Path(__file__).resolve().parent)
main_path = 'source_images/'
export_path = 'output_images/'
target_size = 1080
quality = 90
filters = {
    'NEAREST': 0,
    'LANCZOS': 1,
    'BILINEAR': 2,
    'BICUBIC': 3,
    'BOX': 4,
    'HAMMING': 5,
}
# Select what filter the conversion will resample at
resample = filters.get('BILINEAR')
allowed_ext = ['png', 'jpg']

def set_filename(filename):
    output_filename = filename.split('.')
    output_filename.pop()
    output_filename = '.'.join(output_filename)
    return output_filename

def get_file_ext(filename):
    return filename.split('.')[-1]

def get_image_orientation(w, h):
    #return True if image is landscape, returns false if its portrait.
    if w > h:
        return True
    else:
        return False

def resize_image(image, w, h):
    # Resize image
    return image.resize((w, h), resample=resample)

def convert_images():
    pathlist = Path(main_path).glob('**/*')
    for path in pathlist:
        # only iterate over files
        if not path.is_dir() and path.name != '.gitignore':
            filename = path.name
            # because path is object not string
            path_in_str = str(path)
            # will check subfolders and maintain the hierarchy for the output_images
            parent_folder = str(path.parents[0]).split('\\')
            parent_folder.pop(0)
            parent_folder = '/'.join(parent_folder)
            output_path = export_path + parent_folder
            # output_path = BASE_DIR + output_path.replace('/', '\\')
            output_file = output_path+'/'+ set_filename(filename) + '.webp' # check if the file exists, otherwise don't optimize it again, just skip that file. 

            if not os.path.exists(output_path):
                os.makedirs(output_path)

            # check if the file exists, otherwise don't optimize it again, just skip that file. 
            if os.path.isfile(output_file):
                # print('File exists in output_images')
                pass
            else:

                image_name = set_filename(filename)
                image_ext = get_file_ext(filename)
                if (image_ext in allowed_ext):
                    image = Image.open(path_in_str)
                    w, h = image.size

                    #check if images are in a landscape or a portrait format:
                    if get_image_orientation(w,h):
                        #landscape resize
                        if w != target_size:
                            height_percent = (target_size / float(h))
                            width_size = int( float(w) * float(height_percent))
                            image = resize_image(image, width_size, target_size)
                        
                    else:
                        #portrait resize
                        if h != target_size:
                            width_percent = (target_size / float(w))
                            height_size = int( float(h) * float(width_percent))
                            image = resize_image(image, target_size, height_size)
                    
                    print(f'Converted {image_name} and saved in: {parent_folder}')
                    # Save image
                    image.save(output_path+'/'+image_name+ '.webp', 'webp', optimize=True, quality=quality)
                    pass

def main():
    convert_images()

if __name__ == '__main__':
    main()