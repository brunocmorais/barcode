from contracts.barcode_options import BarcodeOptions


class Bitmap:
    def to_bitmap(self, pixels : list[list[int]]):

        image_size = len(pixels) * len(pixels[0])
        bmp_header = bytearray()
        dib_header = bytearray()
        data = bytearray()
        bytes = bytearray()

        # Data
        for y in (pixels):
            padding = ((len(y) * 3) % 4)

            for x in y:
                data.extend((x).to_bytes(3, 'little'))

            if padding > 0:
                data.extend(([0x00] * (4 - padding)))
        
        # BMP header
        bmp_header.extend([0x42, 0x4D])
        bmp_header.extend((54 + image_size * 3).to_bytes(4, 'little'))
        bmp_header.extend(([0x00] * 4))
        bmp_header.extend([0x36, *([0x00] * 3)])

        # DIB header
        dib_header.extend([0x28, *([0x00] * 3)])
        dib_header.extend((len(pixels[0])).to_bytes(4, 'little'))
        dib_header.extend((len(pixels)).to_bytes(4, 'little'))
        dib_header.extend([0x01, 0x00, 0x18, 0x00])
        dib_header.extend(([0x00] * 4))
        dib_header.extend(len(data).to_bytes(4, 'little'))
        dib_header.extend(([0x13, 0x0B, 0x00, 0x00] * 2))
        dib_header.extend(([0x00] * 8))
        
        bytes.extend(bmp_header)
        bytes.extend(dib_header)
        bytes.extend(data)

        return bytes

    def to_pixels(self, barcode : list[bool], opt : BarcodeOptions):

        pixel_line = [
            *([0xFFFFFF] * opt.quiet_zone_x), 
            *([0x000000 if bar else 0xFFFFFF for bar in barcode]), 
            *([0xFFFFFF] * opt.quiet_zone_x)
        ]
        
        scaled_line : list[int] = []

        for pixel in pixel_line:
            scaled_line.extend([pixel] * opt.scale_factor)

        return [
            *([[0xFFFFFF] * len(scaled_line) for _ in range(opt.quiet_zone_y * opt.scale_factor)]),
            *(scaled_line for _ in range(opt.height)),
            *([[0xFFFFFF] * len(scaled_line) for _ in range(opt.quiet_zone_y * opt.scale_factor)])
        ]
