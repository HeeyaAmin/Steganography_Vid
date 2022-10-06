# take video input
# break it into frames
# calculate the vid parameters
# then hide two images in it
# using LSB technique
# phir recompile the vid frames
# show final vid

# problem:
# lsb technique se frame m kaise hide krein
# aur phir recompile kaise krein

# modules kaunsi chahiye rahegi

# ye code pehle ek image ko dusri image m hide krne ka hai
import argparse
from PIL import Image

class Steganography:
    BLACK_PIXEL = (0,0,0)

    # convert integer tuple to binary(string) tuple
    def _int_to_bin(self, rgb):
        r,g,b = rgb
        return f'{r:08b}',f'{g:08b}',f'{b:08b}'

    # convert binary tuple to integer tuple
    def _bin_to_int(self,rgb):
        r,g,b = rgb
        return int(r,2),int(g,2),int(b,2)

    # merge two rgb tuples
    def _merge_rgb(self,rgb1,rgb2):
        r1, g1, b1 = self._int_to_bin(rgb1)
        r2, g2, b2 = self._int_to_bin(rgb2)
        rgb = r1[:4] + r2[:4], g1[:4] + g2[:4], b1[:4] + b2[:4]
        return self._bin_to_int(rgb)

    # unmerge rgb
    def _unmerge_rgb(self,rgb):
        r,g,b = self._int_to_bin(rgb)
        new_rgb = r[4:]+'0000', g[4:]+'0000', b[4:]+'0000'
        return self._bin_to_int(new_rgb)

    # merge image1 into image2
    def merge(self,image1,image2):
        if image2.size[0]>image1.size[0] or image2.size[1]>image1.size[1]:
            raise ValueError('Image 2 should be smaller than image 1')

        # get pixel map of the two images
        map1 = image1.load()
        map2 = image2.load()

        new_image = Image.new(image1.mode, image1.size)
        new_map = new_image.load()

        for i in range(image1.size[0]):
            for j in range(image1.size[1]):
                is_valid= lambda: i<image2.size[0] and j<image2.size[1]
                rgb1 = map1[i,j]
                rgb2 = map2[i,j] if is_valid() else self.BLACK_PIXEL
                new_map[i,j] = self._merge_rgb(rgb1,rgb2)

        return new_image

    def unmerge(self,image):
        pixel_map = image.load()
        new_image = Image.new(image.mode, image.size)
        new_map = new_image.load()

        for i in range(image.size[0]):
            for j in range(image.size[1]):
                new_map[i,j]=self._unmerge_rgb(pixel_map[i,j])
        return new_image


def main():
    parser = argparse.ArgumentParser(description='Steganography')
    subparser = parser.add_subparsers(dest='command')

    merge = subparser.add_parser('merge')
    merge.add_argument('--image1',required=True, help='Image1 path')
    merge.add_argument('--image2',required=True, help='Image2 path')
    merge.add_argument('output',required=True, help='Output path')

    unmerge = subparser.add_parser('unmerge')
    unmerge.add_argument('--image',required=True,help='Image path')
    unmerge.add_argument('--output',required=True,help='Output path')

    args = parser.parse_args()

    if args.command == 'merge':
        image1 = Image.open(args.image1)
        image2 = Image.open(args.image2)
        Steganography().merge(image1, image2).save(args.output)

if __name__=='__main__':
    main()