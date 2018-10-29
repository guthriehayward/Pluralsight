"""A module for dealing with BMP bitmap image files."""

def write_grayscale(filename, pixels):
    """Creates and writes a grayscale BMP file.

    Args:
        filename: The name of the BMP file to be created.

        pixels: A rectangular image stored as a sequence of rows.
                Each row must be an iterable series of integers in the range 0-255.

    Raises:
        OSError: If the file couldn't be written.
    """
    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        #BMP Header
        bmp.write(b'BM')

        size_bookmark = bmp.tell()      # The next four bytes hold the filesize as a 32-bit
        bmp.write(b'\x00\x00\x00\x00')  # little-endian integer. Zero placeholder for now.

        bmp.write(b'\x00\x00')  #Unused 16-bit integer - should be zero.
        bmp.write(b'\x00\x00')  #Unused 16-bit integer - should be zero.

        pixel_offset_bookmark = bmp.tell()
        bmp.write(b'\x00\x00\x00\x00')

        #Image Header
        bmp.write(b'\x28\x00\x00\x00')
        bmp.write(_int32_to_bytes(width))
        bmp.write(_int32_to_bytes(height))
        bmp.write(b'\x01\x00')
        bmp.write(b'\x08\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')

        #Color palette - A linear grayscale
        for c in range(256):
            bmp.write(bytes((c, c, c, 0))) #Blue, Green, Red, zero

        #Pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):
            row_data = bytes(row)
            bmp.write(row_data)
            padding = b'\x00' * (4 - (len(row) %4))
            bmp.write(padding)

        #End of file
        eof_bookmark = bmp.tell

        #Fill in file size placeholder
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        #Fill in pixel offset placeholder
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))
