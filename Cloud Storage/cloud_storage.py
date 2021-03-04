import dropbox
class TranseferData:
       def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)
def main():
    access_token='sl.AsUjgqCUhOwfHuQFQD-z05HxMAUauRaj66SosQ81gh2gkdGrB2wD0sL4CDsL1B4jJirT9DtM-nW5XzBl2IA89rs7U1qMWj8Jd440YWxVi4_BUgL1F5cLDkTlSEHtjeOiu9dpUlg'
    transferData = TransferData(access_token)
file_from =input("Enter the file pathto transfer:-")
 file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")
    
    main()
