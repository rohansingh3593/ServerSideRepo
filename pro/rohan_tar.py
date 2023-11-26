import stat
import tarfile
import tempfile
import os

tar_file = "decrypted-Test_FWDL_ColdStart_SecureBoot_FW10.5.787.1.AsicTestSecure_Gen5RivaAsic.GEN5RIVA_REL_3_1_Dev.tar.gz"

TMP = os.path.dirname(__file__)
# print(os.path.dirname(__file__))
# print(os.path.abspath(__file__))


INNER = os.path.join(TMP, "inner")
rfs = os.path.join(TMP, "rootfs")
l1 = os.path.join(TMP, "layer1")
l2 = os.path.join(TMP, "layer2")
# os.rmdir(rfs)
# os.rmdir(l1)
# os.rmdir(l2)
# os.rmdir(INNER)


os.mkdir(rfs)
os.mkdir(l1)
os.mkdir(l2)
os.mkdir(INNER)
os.remove(f'new_{tar_file}')

tar = tarfile.open(tar_file, mode="r:gz")
members = tar.getmembers()

file_permission = stat.S_IRUSR | stat.S_IWUSR
folder_permission = stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR


# Let's pretend we want to edit, and write to new tar
if len(members) > 0:
    fd, tmp_tar = tempfile.mkstemp(prefix=("%s.fixed." % tar_file))
    os.close(fd)
    fixed_tar = tarfile.open(tmp_tar, "w:gz")
    # Then process members
    for member in members:
        # add o+rwx for directories
        if member.isdir() and not member.issym():
            member.mode = folder_permission | member.mode
            extracted = tar.extractfile(member)
            fixed_tar.addfile(member, extracted)
        # add o+rw for plain files
        elif member.isfile() and not member.issym():
            member.mode = file_permission | member.mode
            extracted = tar.extractfile(member)
            fixed_tar.addfile(member, extracted)
        else:
            fixed_tar.addfile(member)
            
    fixed_tar.close()
    tar.close()
    # Rename the fixed tar to be the old name
    os.rename(tmp_tar,f'new_{tar_file}')
tar.close()

assert os.path.exists(os.path.join(l2, INNER))

print(os.listdir(l1))
with tarfile.open(name=f'new_{tar_file}', mode="r:gz") as t:
    t.extractall(l1)

print(os.listdir(INNER))

with tarfile.open(name=os.path.join(l1, '10.5.787.1.ColdStart.img.tar.gz'), mode='r:gz') as t:
    t.extractall(l2)

print(os.listdir(l2))


with tarfile.open(name=os.path.join(l2, 'rootfs.tar.gz'), mode='r:gz') as t:
    t.extractall(rfs)

print(os.listdir(rfs))

