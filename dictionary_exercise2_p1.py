# Problem 1
# Create a dictionary to store encryption values.
encryption_codes = {'A':'+','B':')','C':'*','D':'^','E':'$','F':'@',
                    'G':'~','H':'!','I':'#','J':'%','K':'&','L':'(',
                    'M':'=','N':'0','O':'8','P':'6','Q':'4','R':'2',
                    'S':'`','T':'1','U':'3','V':'5','W':'7','X':'9',
                    'Y':'-','Z':'|','a':'{','b':'O','c':'U','d':'T',
                    'e':'E','f':'Q','g':'W','h':'R','i':'Y','j':'I',
                    'k':'P','l':'}','m':']','n':'p','o':'i','p':'y',
                    'q':'r','r':'w','s':'q','t':'e','u':'t','v':'u',
                    'w':'z','x':'a','y':'b','z':'>'}

original_file = open('info_security.txt','r')
read_og_file = original_file.read()
original_file.close()

encrypt_og_file = open('info_sec_encrypted.txt','w')

for c in read_og_file:

    if c in encryption_codes:
        encrypt_og_file.write(encryption_codes[c])

    else:
        encrypt_og_file.write(c)

encrypt_og_file.close()

decryption_codes = {'+':'A',')':'B','*':'C','^':'D','$':'E','@':'F',
                    '~':'G','!':'H','#':'I','%':'J','&':'K','(':'L',
                    '=':'M','0':'N','8':'O','6':'P','4':'Q','2':'R',
                    '`':'S','1':'T','3':'U','5':'V','7':'W','9':'X',
                    '-':'Y','|':'Z','{':'a','O':'b','U':'c','T':'d',
                    'E':'e','Q':'f','W':'g','R':'h','Y':'i','I':'j',
                    'P':'k','}':'l',']':'m','p':'n','i':'o','y':'p',
                    'r':'q','w':'r','q':'s','e':'t','t':'u','u':'v',
                    'z':'w','a':'x','b':'y','>':'z'}

og_file_encrypted = open('info_sec_encrypted.txt','r')
read_encrypt_file = og_file_encrypted.read()
og_file_encrypted.close()

decrpyt_encrypt_file = open('encrypted_info_sec_decrypt.txt','w')

for d in read_encrypt_file:

    if d in decryption_codes:
        decrpyt_encrypt_file.write(decryption_codes[d])

    else:
        decrpyt_encrypt_file.write(d)

decrpyt_encrypt_file.close()