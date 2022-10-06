from stegano import lsb
secret=lsb.hide('apple.jpg','heeya')
secret.save('./encoded_image.jpg')
print(lsb.reveal('./encoded_image.jpg'))
